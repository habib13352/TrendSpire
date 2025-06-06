import csv
import os
from collections import defaultdict

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'api_usage.csv')

def main() -> None:
    usage = defaultdict(lambda: {'prompt': 0, 'completion': 0, 'cost': 0.0})
    if not os.path.exists(LOG_FILE):
        print('No API usage log found.')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            model = row['model']
            usage[model]['prompt'] += int(row['prompt_tokens'])
            usage[model]['completion'] += int(row['completion_tokens'])
            usage[model]['cost'] += float(row['cost_usd'])
    for model, stats in usage.items():
        total_tokens = stats['prompt'] + stats['completion']
        print(f"Model: {model}\n  Prompt tokens: {stats['prompt']}\n  Completion tokens: {stats['completion']}\n  Total tokens: {total_tokens}\n  Cost: ${stats['cost']:.6f}\n")

if __name__ == '__main__':
    main()
