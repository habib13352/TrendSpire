import csv
import json
import os
from collections import defaultdict

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
LOG_FORMAT = os.getenv('API_LOG_FORMAT', 'csv').lower()
LOG_FILE = os.path.join(LOG_DIR, f'api_usage.{LOG_FORMAT}')

def main() -> None:
    usage = defaultdict(lambda: {'prompt': 0, 'completion': 0, 'cost': 0.0})
    if not os.path.exists(LOG_FILE):
        print('No API usage log found.')
        return
    if LOG_FORMAT == 'csv':
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                model = row['model']
                usage[model]['prompt'] += int(row['prompt_tokens'])
                usage[model]['completion'] += int(row['completion_tokens'])
                usage[model]['cost'] += float(row['cost_usd'])
    elif LOG_FORMAT == 'json':
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for row in data:
            model = row['model']
            usage[model]['prompt'] += int(row['prompt_tokens'])
            usage[model]['completion'] += int(row['completion_tokens'])
            usage[model]['cost'] += float(row['cost_usd'])
    else:  # txt
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 6:
                    continue
                _, _service, model, prompt, completion, cost = parts
                usage[model]['prompt'] += int(prompt)
                usage[model]['completion'] += int(completion)
                usage[model]['cost'] += float(cost)
    for model, stats in usage.items():
        total_tokens = stats['prompt'] + stats['completion']
        print(f"Model: {model}\n  Prompt tokens: {stats['prompt']}\n  Completion tokens: {stats['completion']}\n  Total tokens: {total_tokens}\n  Cost: ${stats['cost']:.6f}\n")

if __name__ == '__main__':
    main()
