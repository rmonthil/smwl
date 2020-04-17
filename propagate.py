#!/usr/bin/env python3

import simplejson as json
import spacy
from copy import deepcopy
# Init
nlp = spacy.load("en_core_web_sm")

in_file = 'dict.json'
print("READ : Reading json file : " + in_file)
with open(in_file, 'r', encoding='utf-8') as f:
    data_text = f.read()
print("READ : Parsing json file")
words = json.loads(data_text, strict=False)
print("READ : End, words nb : ", len(words))

output = {}

print("INPUT : Defining some words")
# Adjs
output[str(("vegetal", "ADJ"))]={"is":{"adj":1.0}, "mods":{"vegetal":{"val":1.0}}}
output[str(("body", "ADJ"))]={"is":{"adj":1.0}, "mods":{"body":{"val":1.0}}}
output[str(("static", "ADJ"))]={"is":{"adj":1.0}, "mods":{"static":{"val":1.0}}}
output[str(("burning", "ADJ"))]={"is":{"adj":1.0}, "mods":{"burning":{"val":1.0}}}
output[str(("fluid", "ADJ"))]={"is":{"adj":1.0}, "mods":{"fluid":{"val":1.0}}}
output[str(("vehicle", "ADJ"))]={"is":{"adj":1.0}, "mods":{"vehicle":{"val":1.0}}}
output[str(("transport", "ADJ"))]={"is":{"adj":1.0}, "mods":{"vehicle":{"val":1.0}}}
output[str(("animal", "ADJ"))]={"is":{"adj":1.0}, "mods":{"animal":{"val":1.0}}}
output[str(("edible", "ADJ"))]={"is":{"adj":1.0}, "mods":{"edible":{"val":1.0}}}
output[str(("weapon", "ADJ"))]={"is":{"adj":1.0}, "mods":{"weapon":{"val":1.0}}}
output[str(("group", "ADJ"))]={"is":{"adj":1.0}, "mods":{"group":{"val":1.0}}}

# Verbs
output[str(("cause", "VERB"))]={"is":{"cause":1.0}, "mods":{"cause":{"val":1.0, "args":[]}}}
output[str(("have", "VERB"))]={"is":{"have":1.0}, "mods":{"have":{"val":1.0}}}
output[str(("grab", "VERB"))]={"is":{"have":1.0}, "mods":{"have":{"val":1.0}}}
output[str(("take", "VERB"))]={"is":{"have":1.0}, "mods":{"have":{"val":1.0}}}
output[str(("hold", "VERB"))]={"is":{"have":1.0}, "mods":{"have":{"val":1.0}}}
output[str(("be", "VERB"))]={"is":{"be":1.0}, "mods":{"be":{"val":1.0}}}
output[str(("affect", "VERB"))]={"is":{"affect":1.0}, "mods":{"affect":{"val":1.0}}}
output[str(("move", "VERB"))]={"is":{"move":1.0}, "mods":{"move":{"val":1.0}}}
output[str(("use", "VERB"))]={"is":{"use":1.0}, "mods":{"use":{"val":1.0}}}
output[str(("become", "VERB"))]={"is":{"become":1.0}, "mods":{"become":{"val":1.0}}}
output[str(("consume", "VERB"))]={"is":{"consume":1.0}, "mods":{"consume":{"val":1.0}}}
output[str(("attack", "VERB"))]={"is":{"attack":1.0}, "mods":{"attack":{"val":1.0}}}
output[str(("turn", "VERB"))]={"is":{"turn":1.0}, "mods":{"turn":{"val":1.0}}}
output[str(("drop", "VERB"))]={"is":{"drop":1.0}, "mods":{"drop":{"val":1.0}}}

# Nouns
output[str(("plant", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "static":{"val":1.0}, "vegetal":{"val":1.0}}}
output[str(("body", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}}}
output[str(("item", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}}}
output[str(("fire", "NOUN"))]={"is":{"object":1.0}, "mods":{"burning":{"val":1.0}}}
output[str(("fluid", "NOUN"))]={"is":{"object":1.0}, "mods":{"fluid":{"val":1.0}}}
output[str(("liquid", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "fluid":{"val":1.0}}}
output[str(("vehicle", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "vehicle":{"val":1.0}}}
output[str(("transport", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "vehicle":{"val":1.0}}}
output[str(("animal", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "animal":{"val":1.0}}}
output[str(("being", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "animal":{"val":1.0}}}
output[str(("food", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "edible":{"val":1.0}}}
output[str(("weapon", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "weapon":{"val":1.0}}}
output[str(("group", "NOUN"))]={"is":{"group":1.0}, "mods":{"group":{"val":1.0, "args":[]}}}
output[str(("tract", "NOUN"))]={"is":{"group":1.0}, "mods":{"group":{"val":1.0, "args":[]}}}
output[str(("extent", "NOUN"))]={"is":{"group":1.0}, "mods":{"group":{"val":1.0, "args":[]}}}
output[str(("stream", "NOUN"))]={"is":{"stream":1.0}, "mods":{"stream":{"val":1.0}}} # Can be defined as a moving group, source ?
output[str(("source", "NOUN"))]={"is":{"source":1.0}, "mods":{"source":{"val":1.0}}}
output[str(("air", "NOUN"))]={"is":{"object":1.0}, "mods":{"body":{"val":1.0}, "fluid":{"val":1.0}}}
# TODO : think about it
output[str(("movement", "NOUN"))]={"is":{"action":1.0}, "mods":{"movement":{"val":1.0, "args":[]}}}
output[str(("motion", "NOUN"))]={"is":{"action":1.0}, "mods":{"movement":{"val":1.0, "args":[]}}}
#output[str(("action", "NOUN"))]={"is":{"action":1.0}, "mods":{"action":{"val":1.0}}}
#output[str(("act", "NOUN"))]={"is":{"action":1.0}, "mods":{"action":{"val":1.0}}}
output[str(("construction", "NOUN"))]={"is":{"construction":1.0}, "mods":{"construction":{"val":1.0}}}
output[str(("building", "NOUN"))]={"is":{"construction":1.0}, "mods":{"construction":{"val":1.0}}}
output[str(("location", "NOUN"))]={"is":{"location":1.0}, "mods":{"location":{"val":1.0}}}
output[str(("place", "NOUN"))]={"is":{"location":1.0}, "mods":{"location":{"val":1.0}}}
output[str(("region", "NOUN"))]={"is":{"location":1.0}, "mods":{"location":{"val":1.0}}}
output[str(("area", "NOUN"))]={"is":{"location":1.0}, "mods":{"location":{"val":1.0}}}
# Test
#output[str(("wind", "NOUN"))]={"is":{"test":1.0}, "mods":{"test":{"val":1.0}}}

mod_nouns = ['object, construction, location']
mod_verbs = ['be', 'become']

# TODO : Replace sentence by relation
def preprocess_word(definition):
        # Language processing
        doc = nlp(definition)
        sentence = {}
        for token in doc:
            if token.pos_ in ['NOUN', 'ADJ']:
                sentence[(token.lemma_, token.pos_)] = {'state':'undefined', 'main':True, 'args':[]}
            elif token.pos_ == 'VERB':
                sentence[(token.lemma_, token.pos_)] = {'state':'undefined', 'main':True, 'args':[]}
        for token in doc:
            if token.pos_ in ['NOUN', 'ADJ', 'VERB']:
                if token.dep_ != "ROOT":
                    search = True
                    stoken = token
                    while search:
                        if stoken.head.pos_ in ['NOUN', 'ADJ', "VERB"]:
                            if token.dep_ == 'pobj':
                                sentence[(stoken.head.lemma_, stoken.head.pos_)]['args'].append((token.lemma_, token.pos_, token.dep_, token.head.lemma_))
                            else:
                                sentence[(stoken.head.lemma_, stoken.head.pos_)]['args'].append((token.lemma_, token.pos_, token.dep_))
                            search = False
                        elif stoken.dep_ == 'ROOT':
                            search = False
                        stoken = stoken.head
        return {"is":{}, "mods":{}, "args":[], "sentence":sentence}

def preprocess_sentence(w, sentence):
    word, pos = w
    state = sentence[w]["state"]
    args = sentence[w]['args']
    if state == 'undefined':
        sentence[w]['state'] = 'defining'
        # Dealing with args
        for i, arg in enumerate(args):
            new_arg = (arg, deepcopy(preprocess_sentence((arg[0], arg[1]), sentence)))
            args[i] = new_arg
            sentence[(arg[0], arg[1])]['main'] = False
    elif state == 'defining':
        return {'state':'defining', "main":sentence[w]['main'], "args":{}} # TODO : to think, could just remove undefined args ?
    sentence[w] = {'state':'defined', "main":sentence[w]['main'], "args":args}
    return sentence[w]

# Noun = mods
# Adj = mods
# Verb = mods -> as definition ! But different as use in sentence for others !

def propagate_mods(w): # TODO, deal with dep
    (wprop, wdict) = w
    word, pos, args = wprop[0], wprop[1], wdict['args']
    sword = str((word, pos))
    if sword in output:
        mods = deepcopy(output[sword]['mods']) # Equivalent of is
        for arg in args:
            (aprop, adict) = arg
            aword, apos, adep = aprop[0], aprop[1], aprop[2]
            if pos == 'NOUN':
                if apos == 'ADJ': # Simple add mods
                    for key,val in propagate_mods(arg).items():
                        if key in mods:
                            mods[key]['val'] += val['val'] # TODO, arg treatement ?
                        else:
                            mods[key] = deepcopy(val)
                elif apos == 'NOUN': # Pass it as an argument to. TODO, works ! Improvement : Prepositions !
                    for key,val in mods.items():
                        if 'args' in val:
                            if adep == 'pobj':
                                aprep = aprop[3]
                                if not aprep in [prop[3] for (prop, dic) in mods[key]['args'] if len(prop) > 3]:
                                    mods[key]['args'].append(arg) # TODO, what happens if there is no available ?
                elif apos == 'VERB': # TODO need to be defined
                    pass
            if pos == 'ADJ':
                if apos == 'ADJ': # Simple add mods
                    for key,val in propagate_mods(arg).items():
                        if key in mods:
                            mods[key]['val'] += val['val'] # TODO, arg treatement ?
                        else:
                            mods[key] = deepcopy(val)
            if pos == 'VERB':
                if apos == 'VERB':
                    for key,val in mods.items():
                        if 'args' in val:
                            if 'args' in mods[key] and mods[key]["args"] == []:
                                mods[key]['args'].append(arg) # TODO, what happens if there is no available ?
                pass # TODO need to be defined
        return mods
    else:
        return {}

def compute(input_words, nb):
    words = input_words
    print("COMPUTE : Preprocess")
    for w in words:
        word, pos = eval(w)
        definition = words[w]
        if definition[0] == '(':
            definition = definition[definition.find(')') + 2:]
        if not (w in output):
            output[w] = preprocess_word(definition)
        else:
            print("Word already defined !", word, pos)
    # Propagation
    print("COMPUTE : Preprocess Sentence")
    for w in words:
        word, pos = eval(w)
        out = output[w]
        if 'sentence' in out:
            # Init
            sentence = out['sentence']
            for w in sentence:
                preprocess_sentence(w, sentence)
            out['sentence'] = {k:v for k,v in sentence.items() if v['main']}
            out['full_sentence'] = sentence
    print("COMPUTE : Propagation")
    for i in range(nb):
        print("COMPUTE :", i, "/", nb)
        for w in words:
            word, pos = eval(w)
            out = output[w]
            if 'sentence' in out:
                # Init
                sentence = out['sentence']
                out['mods'] = {}
                # First propagate mods # TODO : args ?
                for sentence_w in out['sentence'].items():
                    sentence_pos = sentence_w[0][1]
                    sentence_args = sentence_w[1]['args']
                    if pos == sentence_pos:
                        for key,val in propagate_mods(sentence_w).items():
                            if key in out['mods']:
                                out['mods'][key]['val'] += val['val']
                            else:
                                out['mods'][key] = deepcopy(val)
                    else:
                        if pos == 'NOUN':
                            if sentence_pos == 'ADJ':
                                # Check for mods
                                for key,val in propagate_mods(sentence_w).items():
                                    if key in out['mods']:
                                        out['mods'][key]['val'] += val['val']
                                    else:
                                        out['mods'][key] = deepcopy(val)
                                # Check for subj # TODO check if not because of aux ? Case : arthropod, insect
                                for psubj in sentence_args:
                                    psubj_dep = psubj[0][2]
                                    if 'nsubj' in psubj_dep:
                                        for key,val in propagate_mods(psubj).items():
                                            if key in out['mods']:
                                                out['mods'][key]['val'] += val['val']
                                            else:
                                                out['mods'][key] = deepcopy(val)
                            elif sentence_pos == 'VERB':
                                # Check for subj
                                for psubj in sentence_args:
                                    psubj_dep = psubj[0][2]
                                    if 'nsubj' in psubj_dep:
                                        for key,val in propagate_mods(psubj).items():
                                            if key in out['mods']:
                                                out['mods'][key]['val'] += val['val']
                                            else:
                                                out['mods'][key] = deepcopy(val)
                # Normalize mods
                sum_mods = sum([out['mods'][mod]['val'] for mod in out['mods']])
                for mod in out['mods']:
                    out['mods'][mod]['val'] /= sum_mods

# Test
test = [str((w, 'NOUN')) for w in ['insect', 'wind']]
testv = [str((w, 'VERB')) for w in ['burn', 'fly']]

print("COMPUTE : Start")
compute(words, 100)
print("COMPUTE : End")

print("CLEANING : Reformating output")
for w in output:
    if 'sentence' in output[w]:
        # Test
        if w in test or w in testv:
            print(output[w]['sentence'])
        # Clean sentence
        #output[w]['sentence'] = {str(t):output[w]['sentence'][t] for t in output[w]['sentence']}
        output[w].pop('sentence')
        # Clean full sentence
        #output[w]['full_sentence'] = {str(t):output[w]['full_sentence'][t] for t in output[w]['full_sentence']}
        output[w].pop('full_sentence')

print("STORING : output.json")
with open('output.json', 'w') as f:
    json.dump(output, f, sort_keys=True, indent=4)
