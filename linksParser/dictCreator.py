#!/usr/bin/env python3
# -*- coding: utf-8 -*

# External module
import simplejson as json

# My module
import linksParser
from linksParser import getLinks

# Greater recursion number !
from sys import setrecursionlimit
setrecursionlimit(10000)

# Set language
linksParser.website = "https://fr.wikipedia.org/wiki/"

# Creating words_to_fetch

words_to_fetch = []
# with open('words_to_fetch.txt', 'r', encoding='utf-8') as f:
    # txt = f.read().split('\n')
    # for t in txt:
        # # Removing number of occurences
        # t = t.split('\t')[0]
        # # Replacing " " by "_"
        # t = t.replace(" ", "_")
        # words_to_fetch.append(t)
        
with open('dictin.json', 'r', encoding='utf-8') as f:
    dict = json.loads(f.read(), strict=False)
    
for w in dict:
    words_to_fetch.append(w)

del(dict)

# Reading words_dict

words_dict = {}

# Reload whats done
with open('dict.json', 'r', encoding='utf-8') as f:
    words_dict = json.loads(f.read(), strict=False)
        
def rec_fetch(word, prog):
    word = word.capitalize()
    if(not (word in words_dict)):
        
        # Prints progression
        print("Word : " + word, ' | Prog : ' + str(int(prog * 100 / len(words_to_fetch))) + '%', ' | Total nb of words : ' + str(len(words_dict)))
        
        homonymie, out_words, occ_nb = getLinks(word, 2, -1)

        error_test = homonymie == "error"
        none_homonymie = homonymie and (not out_words)
        
        if((not error_test) and (not none_homonymie)):
        
            words_dict[word] = {
              "word":word,
              "out_words":[],
              "homonymie":homonymie,
              "relevance":[]
              }
          
            occ_total = 0.0
            i = 0
            for w in out_words:
                w = w.capitalize()
                rec_fetch(w, prog)
                
                if w in words_dict:
                    words_dict[word]["out_words"].append(w)
                    words_dict[word]["relevance"].append(occ_nb[i])
                    occ_total += occ_nb[i]
                    
                i += 1
                
            print("Word finished : " + word)

            # Preventing division by 0
            if(occ_total == 0):
                occ_total = 1.0
            
            for i in range(len(words_dict[word]["relevance"])):
                words_dict[word]["relevance"][i] /= occ_total
                
            print("Out words : " + str(words_dict[word]["out_words"]))
            print("Relevance : " + str(words_dict[word]["relevance"]))
            
            # Saves the results for each 100 words, in case you lose connection. 
            if(len(words_dict) % 100 == 0):
                with open('dict.json', 'w') as f:
                    print("\n Saving ...")
                    json.dump(words_dict, f, sort_keys=True, indent=4)
                    print("Saved \n")

prog = 0
for word in words_to_fetch:
    rec_fetch(word, prog)
    prog += 1

with open('dict.json', 'w') as f:
    json.dump(words_dict, f, sort_keys=True, indent=4)

# Vrification of relevance
for word in words_dict:
    for r in words_dict[word]["relevance"]:
        if(r > 1.0):
            print("Too much relevance (" + str(r)  + ") with word : " + word)
