#!/usr/bin/env python3

import os
from wiktionaryparser import WiktionaryParser
import simplejson as json
import spacy

# Init
wikparser = WiktionaryParser()
nlp = spacy.load("en_core_web_sm")
trad = {
        "NOUN":"noun",
        "ADJ":"adjective",
        "VERB":"verb",
        }

words_to_fetch = [
        ("apple", "NOUN"),
        ("dragon", "NOUN"),
        ("lion", "NOUN"),
        ("house", "NOUN"),
        ("town", "NOUN"),
        ("plane", "NOUN"),
        ("cloud", "NOUN"),
        ("weather", "NOUN"),
        ("pirate", "NOUN"),
        ("yeti", "NOUN"),
        ("truck", "NOUN"),
        ("star", "NOUN"),
        ("dinosaur", "NOUN"),
        ("fairy", "NOUN"),
        ("ogre", "NOUN"),
        ("forest", "NOUN"),
        ("elf", "NOUN"),
        ("orc", "NOUN"),
        ("demon", "NOUN"),
        ("earth", "NOUN"),
        ("ground", "NOUN"),
        ("table", "NOUN"),
        ("chair", "NOUN"),
        ("insect", "NOUN"),
        ("beach", "NOUN"),
        ("ocean", "NOUN"),
        ("river", "NOUN"),
        ("sea", "NOUN"),
        ("cactus", "NOUN"),
        ("baobab", "NOUN"),
        ("spider", "NOUN"),
        ("volcano", "NOUN"),
        ("robot", "NOUN"),
        ("heater", "NOUN"),
        ("cave", "NOUN"),
        ("torch", "NOUN"),
        ("tank", "NOUN"),
        ("lion", "NOUN"),
        ("unicorn", "NOUN"),
        ("skeleton", "NOUN"),
        ("monster", "NOUN"),
        ("goose", "NOUN"),
        ("univers", "NOUN"),
        ("world", "NOUN"),
        ("cake", "NOUN"),
        ("hero", "NOUN"),
        ("castle", "NOUN"),
        ("dungeon", "NOUN"),
        ("ant", "NOUN"),
        ("carpet", "NOUN"),
        ("hell", "NOUN"),
        ("jungle", "NOUN"),
        ("ghost", "NOUN"),
        ("vampire", "NOUN"),
        ]
out_dict = {}

if os.path.exists('dict.json'):
    print("Reading dict.json")
    with open('dict.json', 'r') as f:
        out_dict = json.load(f)
    print("Updating words_to_fetch")
    for w in out_dict:
        tw = eval(w)
        if tw in words_to_fetch:
            words_to_fetch.remove(tw)
        # Language processing
        doc = nlp(out_dict[w])
        for token in doc:
            if token.pos_ in trad:
                child = (token.lemma_, token.pos_)
                if not str(child) in out_dict and not child in words_to_fetch:
                    words_to_fetch.append(child)

def fetch(word, part):
    # Requesting word on the dictionary
    try:
        wikword = wikparser.fetch(word)
    except:
        print("Couldn't fetch word :", word)
        return
    
    # Finding first definition
    definition = None
    for eth in wikword:
        definitions = eth["definitions"]
        for d in definitions:
            if d['partOfSpeech'] == trad[part]:
                definition = d['text'][1]
                break
        if definition:
            break
    
    if not definition:
        print("Getting first definition", (word, part))
        for eth in wikword:
            definitions = eth["definitions"]
            for d in definitions:
                definition = d['text'][1]
                break
            if definition:
                break

    if definition:
        out_dict[str((word, part))] = definition
        
        # Language processing
        doc = nlp(definition)
        for token in doc:
            if token.pos_ in trad:
                child = (token.lemma_, token.pos_)
                if not str(child) in out_dict and not child in words_to_fetch:
                    words_to_fetch.append(child)
    else:
        print("Couldn't find definition", (word, part))

print("Fetching : ", words_to_fetch)
for word, part in words_to_fetch:
    fetch(word, part)
    if len(out_dict) % 100 == 0:
        print("Saving : {}".format(len(out_dict)))
        with open('dict.json', 'w') as f:
            json.dump(out_dict, f, sort_keys=True, indent=4)

print("Saving : {}".format(len(out_dict)))
with open('dict.json', 'w') as f:
    json.dump(out_dict, f, sort_keys=True, indent=4)
