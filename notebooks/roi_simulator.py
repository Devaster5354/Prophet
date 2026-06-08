"""ROI simulator
Usage: python notebooks/roi_simulator.py --cost 10000 --mean_incremental_clv 1.2 --n_target 10000
"""
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cost', type=float, required=True)
    parser.add_argument('--mean_incremental_clv', type=float, required=True)
    parser.add_argument('--n_target', type=int, required=True)
    args = parser.parse_args()

    total_incremental = args.mean_incremental_clv * args.n_target
    roi = (total_incremental - args.cost) / args.cost
    print(f'Total incremental value: ${total_incremental:,.2f}')
    print(f'ROI: {roi:.2%}')

if __name__ == '__main__':
    main()
