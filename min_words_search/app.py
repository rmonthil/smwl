# -*- coding: utf-8 -*
import sys
sys.setrecursionlimit(10000)

from reader import *
from graph_to_tree_converter import *

r = reader()
g2t = graph_to_tree_converter()

words = r.compute('dict.json')
words, partitions = g2t.compute(words, 'ax_words.txt')

print("Storing result dictionary to : words.json")

with open('words.json', 'w') as f:
    json.dump(words, f, sort_keys=True, indent=4)
	
print("Storing result dictionary to : parts.json")
	
with open('parts.json', 'w') as f:
    json.dump(partitions, f, sort_keys=True, indent=4)
