"""Simple batch scoring helper. Usage:
python scripts_score_batch.py data/input.csv
"""
import sys
import pandas as pd
from Models.serialize import load_model


def main():
    if len(sys.argv) < 2:
        print('Usage: scripts_score_batch.py <csv_path>')
        return
    path = sys.argv[1]
    df = pd.read_csv(path)
    model = None
    try:
        model = load_model()
    except Exception as e:
        print('No model found:', e)
        return
    preds = model.predict(df.values)
    out = pd.DataFrame({'prediction': preds})
    out.to_csv('scores.csv', index=False)
    print('Wrote scores.csv')

if __name__ == '__main__':
    main()
