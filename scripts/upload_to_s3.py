"""Upload key artifacts to S3. Uses AWS credentials from env vars.
Usage: python scripts/upload_to_s3.py --bucket my-bucket --prefix prophet
"""
import argparse
import boto3
import os
from botocore.exceptions import ClientError


def upload_file(s3_client, local_path, bucket, key):
    try:
        s3_client.upload_file(local_path, bucket, key)
        print(f'Uploaded {local_path} -> s3://{bucket}/{key}')
    except ClientError as e:
        print('Upload failed:', e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', required=True)
    parser.add_argument('--prefix', default='')
    args = parser.parse_args()

    s3 = boto3.client('s3')

    # upload model if present
    model_path = os.path.join('Models', 'model.pkl')
    if os.path.exists(model_path):
        key = os.path.join(args.prefix, 'models', 'model.pkl')
        upload_file(s3, model_path, args.bucket, key)

    # upload mlruns folder
    if os.path.exists('mlruns'):
        for root, dirs, files in os.walk('mlruns'):
            for f in files:
                full = os.path.join(root, f)
                rel = os.path.relpath(full, 'mlruns')
                key = os.path.join(args.prefix, 'mlruns', rel)
                upload_file(s3, full, args.bucket, key)

if __name__ == '__main__':
    main()
