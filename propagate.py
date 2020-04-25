#!/usr/bin/env python3

import simplejson as json
import spacy
from copy import deepcopy
# Init
nlp = spacy.load("en_core_web_md")

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
output[str(("vegetal", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"vegetal", "val":1.0, 'args':[]}]}
output[str(("body", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"body", "val":1.0, 'args':[]}]}
output[str(("static", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"static", "val":1.0, 'args':[]}]}
output[str(("burning", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"burning", "val":1.0, 'args':[]}]}
output[str(("fluid", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"fluid", "val":1.0, 'args':[]}]}
output[str(("vehicle", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"vehicle", "val":1.0, 'args':[]}]}
output[str(("transport", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"vehicle", "val":1.0, 'args':[]}]}
output[str(("animal", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"animal", "val":1.0, 'args':[]}]}
output[str(("edible", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"edible", "val":1.0, 'args':[]}]}
output[str(("weapon", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"weapon", "val":1.0, 'args':[]}]}
output[str(("group", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"group", "val":1.0, 'args':[]}]}
output[str(("plural", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"group", "val":1.0, 'args':[]}]}
output[str(("moving", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"moving", "val":1.0, 'args':[]}]}
output[str(("solid", "ADJ"))]={"concepts":[{'name':'adj'}], "relations":[{"name":"solid", "val":1.0, 'args':[]}]}

# Verbs
output[str(("cause", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"cause", "val":1.0, 'args':[{'index':0}]}]} # Can have an other relation as an argument ?
output[str(("have", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"have", "val":1.0, 'args':[{'index':0}]}]}
output[str(("grab", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"have", "val":1.0, 'args':[{'index':0}]}]}
output[str(("take", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"have", "val":1.0, 'args':[{'index':0}]}]}
output[str(("hold", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"have", "val":1.0, 'args':[{'index':0}]}]}
output[str(("be", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"be", "val":1.0, 'args':[{'index':0}]}]}
output[str(("move", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"move", "val":1.0, 'args':[{'index':0}]}]}
output[str(("use", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"use", "val":1.0, 'args':[{'index':0}]}]}
output[str(("become", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"become", "val":1.0, 'args':[{'index':0}]}]}
output[str(("consume", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"consume", "val":1.0, 'args':[{'index':0}]}]}
output[str(("attack", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"hit", "val":1.0, 'args':[{'index':0}]}]}
output[str(("turn", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"turn", "val":1.0, 'args':[{'index':0}]}]}
output[str(("drop", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"drop", "val":1.0, 'args':[{'index':0}]}]}
output[str(("hit", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"hit", "val":1.0, 'args':[{'index':0}]}]}

# Nouns
output[str(("object", "NOUN"))]={"concepts":[{'name':'object'}], "relations":[{"name":"object", "val":1.0, 'args':[{'index':0}]}]}
output[str(("plant", "NOUN"))]={"concepts":[{'name':'plant'}], "relations":[{"name":"vegetal", "val":0.33, 'args':[{'index':0}]}, {"name":"body", "val":0.33, 'args':[{'index':0}]}, {"name":"static", "val":0.33, 'args':[{'index':0}]}]}
output[str(("body", "NOUN"))]={"concepts":[{'name':'body'}], "relations":[{"name":"body", "val":1.0, 'args':[{'index':0}]}]}
output[str(("item", "NOUN"))]={"concepts":[{'name':'item'}], "relations":[{"name":"body", "val":1.0, 'args':[{'index':0}]}]}
output[str(("fire", "NOUN"))]={"concepts":[{'name':'fire'}], "relations":[{"name":"burning", "val":1.0, 'args':[{'index':0}]}]}
output[str(("fluid", "NOUN"))]={"concepts":[{'name':'fluid'}], "relations":[{"name":"fluid", "val":1.0, 'args':[{'index':0}]}]}
output[str(("liquid", "NOUN"))]={"concepts":[{'name':'liquid'}], "relations":[{"name":"fluid", "val":1.0, 'args':[{'index':0}]}]}
output[str(("water", "NOUN"))]={"concepts":[{'name':'water'}], "relations":[{"name":"fluid", "val":1.0, 'args':[{'index':0}]}]}
output[str(("vehicle", "NOUN"))]={"concepts":[{'name':'vehicle'}], "relations":[{"name":"vehicle", "val":0.5, 'args':[{'index':0}]}, {"name":"body", "val":0.5, 'args':[{'index':0}]}]}
output[str(("transport", "NOUN"))]={"concepts":[{'name':'transport'}], "relations":[{"name":"vehicle", "val":0.5, 'args':[{'index':0}]}, {"name":"body", "val":0.5, 'args':[{'index':0}]}]}
output[str(("animal", "NOUN"))]={"concepts":[{'name':'animal'}], "relations":[{"name":"animal", "val":0.5, 'args':[{'index':0}]}, {"name":"body", "val":0.5, 'args':[{'index':0}]}]}
output[str(("being", "NOUN"))]={"concepts":[{'name':'being'}], "relations":[{"name":"animal", "val":0.5, 'args':[{'index':0}]}, {"name":"body", "val":0.5, 'args':[{'index':0}]}]}
output[str(("food", "NOUN"))]={"concepts":[{'name':'food'}], "relations":[{"name":"edible", "val":0.5, 'args':[{'index':0}]}, {"name":"body", "val":0.5, 'args':[{'index':0}]}]}
output[str(("weapon", "NOUN"))]={"concepts":[{'name':'weapon'}], "relations":[{"name":"weapon", "val":0.5, 'args':[{'index':0}]}, {"name":"body", "val":0.5, 'args':[{'index':0}]}]}
output[str(("group", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'args':[{'index':0}]}]}
output[str(("tract", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'args':[{'index':0}]}]}
output[str(("extent", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'args':[{'index':0}]}]}
output[str(("stream", "NOUN"))]={"concepts":[{'name':'stream', 'args':[]}], "relations":[{"name":"stream", "val":1.0, 'args':[{'index':0}]}]}
output[str(("source", "NOUN"))]={"concepts":[{'name':'source', 'args':[]}], "relations":[{"name":"source", "val":1.0, 'args':[{'index':0}]}]}
output[str(("air", "NOUN"))]={"concepts":[{'name':'air'}], "relations":[{"name":"fluid", "val":1.0, 'args':[{'index':0}]}]}
output[str(("movement", "NOUN"))]={"concepts":[{'name':'movement'}], "relations":[{"name":"group", "val":0.5, 'args':[{'index':0}]}, {"name":"moving", "val":0.5, 'args':[{'index':0}]}]}
output[str(("motion", "NOUN"))]={"concepts":[{'name':'motion'}], "relations":[{"name":"group", "val":0.5, 'args':[{'index':0}]}, {"name":"moving", "val":0.5, 'args':[{'index':0}]}]}
output[str(("action", "NOUN"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"action", "val":1.0, 'args':[{'index':0}]}]}
output[str(("act", "NOUN"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"action", "val":1.0, 'args':[{'index':0}]}]}
output[str(("building", "NOUN"))]={"concepts":[{'name':'building'}], "relations":[{"name":"body", "val":0.33, 'args':[{'index':0}]}, {"name":"location", "val":0.33, 'args':[{'index':0}]}, {"name":"building", "val":0.33, 'args':[{'index':0}]}]}
output[str(("location", "NOUN"))]={"concepts":[{'name':'location'}], "relations":[{"name":"location", "val":1.0, 'args':[{'index':0}]}]}
output[str(("place", "NOUN"))]={"concepts":[{'name':'place'}], "relations":[{"name":"location", "val":1.0, 'args':[{'index':0}]}]}
output[str(("region", "NOUN"))]={"concepts":[{'name':'region'}], "relations":[{"name":"location", "val":1.0, 'args':[{'index':0}]}]}
output[str(("area", "NOUN"))]={"concepts":[{'name':'area'}], "relations":[{"name":"location", "val":1.0, 'args':[{'index':0}]}]}

id_rank = -1
def id():
    global id_rank
    id_rank += 1
    return id_rank

def preprocess_word(definition):
        # Language processing
        doc = nlp(definition)
        sentence = {}
        for token in doc:
            if token.pos_ in ['NOUN', 'ADJ']:
                sentence[(token.lemma_, token.pos_)] = {'state':'undefined', 'main':False, 'unready':0}
            elif token.pos_ == 'VERB':
                sentence[(token.lemma_, token.pos_)] = {'state':'undefined', 'main':False, 'unready':0}
        for token in doc:
            if token.pos_ in ['NOUN', 'ADJ', 'VERB']:
                sentence[(token.lemma_, token.pos_)]['dep'] = token.dep_
                sentence[(token.lemma_, token.pos_)]['chain'] = []
                if token.dep_ != "ROOT":
                    search = True
                    stoken = token
                    while search:
                        if stoken.head.pos_ in ['NOUN', 'ADJ', "VERB"]:
                            sentence[(token.lemma_, token.pos_)]['shead'] = (stoken.head.lemma_, stoken.head.pos_)
                            sentence[(stoken.head.lemma_, stoken.head.pos_)]['unready'] += 1
                            search = False
                        elif stoken.dep_ == 'ROOT':
                            sentence[(token.lemma_, token.pos_)]['main'] = True
                            search = False
                        else:
                            sentence[(token.lemma_, token.pos_)]['chain'].append({'lemma':stoken.head.lemma_, 'dep':stoken.head.dep_})
                        stoken = stoken.head
                else:
                    sentence[(token.lemma_, token.pos_)]['main'] = True
        return {"concepts":[], "relations":[], "fsentence":sentence}

def compute(input_words, nb):
    words = input_words
    print("COMPUTE : Preprocess")
    for w in words:
        word, pos = eval(w)
        definition = words[w]
        if definition[0] == '(':
            definition = definition[definition.find(')') + 2:]
        # Removing (s)
        definition = definition.replace('(s)', '') # fix for the word 'furniture'
        # Replacing ; by .
        definition = definition.replace(';', '.') # fix for the word 'throw'
        # Preprocessing
        if not (w in output):
            output[w] = preprocess_word(definition)
        else:
            print("Word already defined !", word, pos)
    print("COMPUTE : Propagation")
    for i in range(nb):
        print("COMPUTE :", i, "/", nb)
        for w in words:
            word, pos = eval(w)
            out = output[w]
            if 'fsentence' in out:
                # Init
                out['sentence'] = deepcopy(out['fsentence'])
                out['concepts'] = []
                out['relations'] = []
                if True: # TODO Maybe only for nouns ? Verbs and adj shouldn't have ?
                    # First propagate
                    for sw in out['sentence']:
                        ssw = str(sw)
                        if ssw in output:
                            sout = output[ssw]
                            out['sentence'][sw]['concepts'] = deepcopy(sout['concepts'])
                            out['sentence'][sw]['relations'] = deepcopy(sout['relations'])
                        else:
                            out['sentence'][sw]['concepts'] = []
                            out['sentence'][sw]['relations'] = []
                        out['sentence'][sw]['addc'] = []
                        out['sentence'][sw]['addr'] = []
                    # Process sentence
                    sentence_processing = True
                    while sentence_processing:
                        sentence_processing = False
                        for sw in out['sentence']:
                            sdict = out['sentence'][sw]
                            if sdict['unready'] == 0:
                                # Continue computation
                                sentence_processing = True
                                # Add addc, addr to self
                                for c in sdict['addc']:
                                    sdict['concepts'].append(c)
                                    sdict['concepts'][-1]['is_arg'] = True
                                    sdict['concepts'][-1]['index'] = len(sdict['concepts']) - 1 # TODO : useful for debug
                                for r in sdict['addr']:
                                    sdict['relations'].append(r)
                                # Add self to shead addc, addr
                                if not sdict['main']:
                                    hdict = out['sentence'][sdict['shead']]
                                    # Check if it can accept arg
                                    can_arg = False
                                    for hc in hdict['concepts']:
                                        if 'args' in hc and (not 'is_arg' in hc or not hc['is_arg']):
                                            can_arg = True
                                            break
                                    # If it can, add all concepts and relations
                                    if can_arg:
                                        offset = len(hdict['concepts'])
                                        for c in sdict['concepts']: # TODO RESOLVE DEP (conj = synonym ?)
                                            hdict['addc'].append(deepcopy(c))
                                            hdict['addc'][-1]['index'] = len(hdict['addc']) - 1 # TODO : useful for debug
                                            if 'args' in hdict['addc'][-1]:
                                                for a in hdict['addc'][-1]['args']:
                                                    a['index'] += offset
                                            if not 'is_arg' in c or not c['is_arg']:
                                                for hc in hdict['concepts']:
                                                    if 'args' in hc and (not 'is_arg' in hc or not hc['is_arg']):
                                                        hc['args'].append({'dep':sdict['dep'], 'chain':sdict['chain'], 'index':offset + len(hdict['addc']) - 1})
                                        for r in sdict['relations']:
                                            hdict['addr'].append(deepcopy(r))
                                            for a in hdict['addr'][-1]['args']:
                                                a['index'] += offset
                                    hdict['unready'] -= 1
                                sdict['unready'] -= 1
                                # Big finish, add all concepts and relations if main
                                if sdict['main']:
                                    offset = len(out['concepts'])
                                    for c in sdict['concepts']:
                                        out['concepts'].append(c)
                                        out['concepts'][-1]['index'] = len(out['concepts']) - 1 # TODO : useful for debug
                                    for r in sdict['relations']:
                                        out['relations'].append(r)
                                        for a in out['relations'][-1]['args']:
                                            a['index'] += offset
                    # TODO PROCESS RELATIONS IF POSSIBLE (take examples)
                    # Then normalize relations
                    tot = sum([relation['val'] for relation in out['relations']])
                    out['relations'] = [{'name':relation['name'], 'val':relation['val']/tot, 'args':relation['args']} for relation in out['relations']]

# Test
test = str(('throw', 'VERB'))
definition = words[test].replace('(s)', '')
doc = nlp(definition)
print(test, definition)
for token in doc:
    print('WORD :', token.lemma_, token.pos_, token.dep_, 'HEAD :', token.head.lemma_, token.head.pos_, token.head.dep_)

print("COMPUTE : Start")
compute(words, 3)
print("COMPUTE : End")

print("CLEANING : Reformating output")
for w in output:
    if 'sentence' in output[w]:
        # Clean sentence
        #output[w]['fsentence'] = {str(t):output[w]['fsentence'][t] for t in output[w]['fsentence']}
        output[w].pop('fsentence')
        #output[w]['sentence'] = {str(t):output[w]['sentence'][t] for t in output[w]['sentence']}
        output[w].pop('sentence')

print("STORING : output.json")
with open('output.json', 'w') as f:
    json.dump(output, f, sort_keys=True, indent=4)
