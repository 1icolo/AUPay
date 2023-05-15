from cgi import print_exception
from collections import Counter
import csv

def item_counter(*descriptions: str):
    all_items = []
    for description in descriptions:
        lines = description.split('\n')
        items = [line.split(',')[0] for line in lines]
        all_items.extend(items)
    item_counts = Counter(all_items)
    results = []
    for item, count in item_counts.items():
        price = next(line.split(',')[1] for description in descriptions for line in description.split('\n') if line.startswith(item))
        results.append(f'{item},{price},{count}')
    result_string = '\n'.join(results)
    return convert_to_dict(result_string)
    # return result_string

def item_counter_deductive(*descriptions: str):
    first_description = descriptions[0]
    first_lines = first_description.split('\n')
    items_and_counts = [line.split(',')[:2] for line in first_lines]
    items_count = {}
    for item, count in items_and_counts:
        items_count[item] = items_count.get(item, 0) + 1
    for description in descriptions[1:]:
        lines = description.split('\n')
        items_and_counts = [line.split(',')[:2] for line in lines]
        for item, count in items_and_counts:
            items_count[item] = items_count.get(item, 0) - 1
    prices = {}
    for description in descriptions:
        for line in description.split('\n'):
            item, price = line.split(',')
            prices[item] = price
    results = {}
    for item, count in items_count.items():
        results[item] = (item, prices[item], count)
    result_string = '\n'.join([f'{item},{price},{count}' for item, price, count in results.values()])
    return convert_to_dict(result_string)
    # return result_string

def convert_to_dict(csv_string: str):
  items = csv_string.split('\n')
  final_list = []
  for item in items:
      final_list.append({'name':item.split(',')[0], 'price': item.split(',')[1], 'quantity': item.split(',')[2]})
  return final_list
