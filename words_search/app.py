# -*- coding: utf-8 -*
import sys
sys.setrecursionlimit(10000)

from reader import *
from graph_to_tree_converter import *

r = reader()
g2t = graph_to_tree_converter()

words = r.compute('input/dict.json')
words, partitions = g2t.compute(words, 'output/ax_words.txt')

print("Storing result dictionary to : output/words.json")

with open('output/words.json', 'w') as f:
    json.dump(words, f, sort_keys=True, indent=4)
	
print("Storing result dictionary to : output/parts.json")
	
with open('output/parts.json', 'w') as f:
    json.dump(partitions, f, sort_keys=True, indent=4)