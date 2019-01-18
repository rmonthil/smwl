#!/usr/bin/env python3
# -*- coding: utf-8 -*

# External module
import simplejson as json

# My module
from linksParser import getLinks

# Greater recursion number !
from sys import setrecursionlimit
setrecursionlimit(10000)

words_to_fetch = []
with open('words_to_fetch.txt', 'r', encoding='utf-8') as f:
	txt = f.read().split('\n')
	for t in txt:
		# Removing number of occurences
		t = t.split('\t')[0]
		# Replacing " " by "_"
		t = t.replace(" ", "_")
		words_to_fetch.append(t)

words_dict = {}

# Reload whats done
with open('dict.json', 'r', encoding='utf-8') as f:
	words_dict = json.loads(f.read(), strict=False)
		
def rec_fetch(word, prog):
	word = word.capitalize()
	if(not (word in words_dict)):
		
		# Prints progression
		print("Mot : " + word, str(prog) + '/' + str(len(words_to_fetch)), ' | Total nb of words : ' + str(len(words_dict)))
		
		homonymie, out_words = getLinks(word, 1, 1)
		
		error_test = homonymie == "error"
		none_homonymie = homonymie and (not out_words)
		
		if((not error_test) and (not none_homonymie)):
		
			words_dict[word] = {
			  "word":word,
			  "out_words":[],
			  "homonymie":homonymie
			  }
		  
			for w in out_words:
				w = w.capitalize()
				rec_fetch(w, prog)
				if w in words_dict:
					words_dict[word]["out_words"].append(w)
			
			# Saves the results for each 1000 words, in case you lose connection. 
			if(len(words_dict) % 1000 == 0):
				with open('ouput/dict.json', 'w') as f:
					json.dump(words_dict, f, sort_keys=True, indent=4)
		
prog = 0
for word in words_to_fetch:
	rec_fetch(word, prog)
	prog += 1

with open('dict.json', 'w') as f:
	json.dump(words_dict, f, sort_keys=True, indent=4)