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
output[str(("vegetal", "ADJ"))]={"concepts":{0:{'name':'vegetal', 'type':{'adj':1.0}, 'used':False}}, "mods":{0:{"vegetal":1.0}}, "relations":{0:[]}} # + sentence relations
#output[str(("body", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"body", "val":1.0, 'arg':{'index':0}}]}
#output[str(("static", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"static", "val":1.0, 'arg':{'index':0}}]}
#output[str(("burning", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"burning", "val":1.0, 'arg':{'index':0}}]}
#output[str(("fluid", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
#output[str(("vehicle", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"vehicle", "val":1.0, 'arg':{'index':0}}]}
#output[str(("transport", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"vehicle", "val":1.0, 'arg':{'index':0}}]}
#output[str(("animal", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"animal", "val":1.0, 'arg':{'index':0}}]}
#output[str(("edible", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"edible", "val":1.0, 'arg':{'index':0}}]}
#output[str(("weapon", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"weapon", "val":1.0, 'arg':{'index':0}}]}
#output[str(("group", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
#output[str(("plural", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
#output[str(("moving", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"moving", "val":1.0, 'arg':{'index':0}}]}
#output[str(("solid", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"solid", "val":1.0, 'arg':{'index':0}}]}
#output[str(("exit", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"exit", "val":1.0, 'arg':{'index':0}}]}

# Verbs
output[str(("cause", "VERB"))]={"concepts":{0:{'name':'cause', 'type':{'action':1.0}, 'used':False}}, "mods":{0:{"cause":1.0}}, "relations":{0:[]}} # + sentence relations
output[str(("have", "VERB"))]={"concepts":{0:{'name':'have', 'type':{'action':1.0}, 'used':False}}, "mods":{0:{"have":1.0}}, "relations":{0:[]}} # + sentence relations
output[str(("grab", "VERB"))]={"concepts":{0:{'name':'grab', 'type':{'action':1.0}, 'used':False}}, "mods":{0:{"have":1.0}}, "relations":{0:[]}} # + sentence relations
output[str(("take", "VERB"))]={"concepts":{0:{'name':'take', 'type':{'action':1.0}, 'used':False}}, "mods":{0:{"have":1.0}}, "relations":{0:[]}} # + sentence relations
output[str(("hold", "VERB"))]={"concepts":{0:{'name':'hold', 'type':{'action':1.0}, 'used':False}}, "mods":{0:{"have":1.0}}, "relations":{0:[]}} # + sentence relations
output[str(("drop", "VERB"))]={"concepts":{0:{'name':'drop', 'type':{'action':1.0}, 'used':False}}, "mods":{0:{"drop":1.0}}, "relations":{0:[]}} # + sentence relations
output[str(("release", "VERB"))]={"concepts":{0:{'name':'release', 'type':{'action':1.0}, 'used':False}}, "mods":{0:{"drop":1.0}}, "relations":{0:[]}} # + sentence relations
#output[str(("be", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"be", "val":1.0, 'arg':{'index':0}}]}
#output[str(("move", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"move", "val":1.0, 'arg':{'index':0}}]}
#output[str(("use", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"use", "val":1.0, 'arg':{'index':0}}]}
#output[str(("become", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"become", "val":1.0, 'arg':{'index':0}}]}
#output[str(("consume", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"consume", "val":1.0, 'arg':{'index':0}}]}
#output[str(("attack", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"hit", "val":1.0, 'arg':{'index':0}}]}
#output[str(("turn", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"turn", "val":1.0, 'arg':{'index':0}}]}
#output[str(("hit", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"hit", "val":1.0, 'arg':{'index':0}}]}
#output[str(("create", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"create", "val":1.0, 'arg':{'index':0}}]}
#output[str(("build", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"create", "val":1.0, 'arg':{'index':0}}]}
#output[str(("produce", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"create", "val":1.0, 'arg':{'index':0}}]}
#output[str(("enter", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"enter", "val":1.0, 'arg':{'index':0}}]}
#output[str(("exit", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"exit", "val":1.0, 'arg':{'index':0}}]}

# Nouns
output[str(("member", "NOUN"))]={"concepts":{0:{'name':'member', 'type':{'object':1.0}, 'used':False}}, "mods":{0:{"being":1.0}}, "relations":{0:[]}}
output[str(("plant", "NOUN"))]={"concepts":{0:{'name':'plant', 'type':{'object':1.0}, 'used':False}}, "mods":{0:{"vegetal":0.33, "body":0.33, "static":0.33}}, "relations":{0:[]}} # + sentence relations
output[str(("body", "NOUN"))]={"concepts":{0:{'name':'body', 'type':{'object':1.0}, 'used':False}}, "mods":{0:{"body":1.0}}, "relations":{0:[]}}
output[str(("item", "NOUN"))]={"concepts":{0:{'name':'item', 'type':{'object':1.0}, 'used':False}}, "mods":{0:{"body":1.0}}, "relations":{0:[]}}
#output[str(("object", "NOUN"))]={"concepts":[{'name':'object', 'args':[]}], "relations":[{"name":"object", "val":1.0, 'arg':{'index':0}}]}
#output[str(("fire", "NOUN"))]={"concepts":[{'name':'fire', 'args':[]}], "relations":[{"name":"burning", "val":1.0, 'arg':{'index':0}}]}
#output[str(("fluid", "NOUN"))]={"concepts":[{'name':'fluid', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
#output[str(("liquid", "NOUN"))]={"concepts":[{'name':'liquid', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
#output[str(("water", "NOUN"))]={"concepts":[{'name':'water', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
#output[str(("vehicle", "NOUN"))]={"concepts":[{'name':'vehicle', 'args':[]}], "relations":[{"name":"vehicle", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
#output[str(("transport", "NOUN"))]={"concepts":[{'name':'transport', 'args':[]}], "relations":[{"name":"vehicle", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
#output[str(("animal", "NOUN"))]={"concepts":[{'name':'animal', 'args':[]}], "relations":[{"name":"animal", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
#output[str(("being", "NOUN"))]={"concepts":[{'name':'being', 'args':[]}], "relations":[{"name":"animal", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
#output[str(("food", "NOUN"))]={"concepts":[{'name':'food', 'args':[]}], "relations":[{"name":"edible", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
#output[str(("weapon", "NOUN"))]={"concepts":[{'name':'weapon', 'args':[]}], "relations":[{"name":"weapon", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
#output[str(("group", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
#output[str(("tract", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
#output[str(("extent", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
#output[str(("stream", "NOUN"))]={"concepts":[{'name':'stream', 'args':[]}], "relations":[{"name":"stream", "val":1.0, 'arg':{'index':0}}]}
#output[str(("source", "NOUN"))]={"concepts":[{'name':'source', 'args':[]}], "relations":[{"name":"source", "val":1.0, 'arg':{'index':0}}]}
#output[str(("air", "NOUN"))]={"concepts":[{'name':'air', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
#output[str(("movement", "NOUN"))]={"concepts":[{'name':'movement', 'args':[]}], "relations":[{"name":"group", "val":0.5, 'arg':{'index':0}}, {"name":"moving", "val":0.5, 'arg':{'index':0}}]}
#output[str(("motion", "NOUN"))]={"concepts":[{'name':'motion', 'args':[]}], "relations":[{"name":"group", "val":0.5, 'arg':{'index':0}}, {"name":"moving", "val":0.5, 'arg':{'index':0}}]}
#output[str(("action", "NOUN"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"action", "val":1.0, 'arg':{'index':0}}]}
#output[str(("act", "NOUN"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"action", "val":1.0, 'arg':{'index':0}}]}
#output[str(("building", "NOUN"))]={"concepts":[{'name':'building', 'args':[]}], "relations":[{"name":"body", "val":0.33, 'arg':{'index':0}}, {"name":"location", "val":0.33, 'arg':{'index':0}}, {"name":"static", "val":0.33, 'arg':{'index':0}}]}
#output[str(("location", "NOUN"))]={"concepts":[{'name':'location', 'args':[]}], "relations":[{"name":"location", "val":1.0, 'arg':{'index':0}}]}
#output[str(("place", "NOUN"))]={"concepts":[{'name':'place', 'args':[]}], "relations":[{"name":"location", "val":1.0, 'arg':{'index':0}}]}
#output[str(("region", "NOUN"))]={"concepts":[{'name':'region', 'args':[]}], "relations":[{"name":"location", "val":1.0, 'arg':{'index':0}}]}
#output[str(("area", "NOUN"))]={"concepts":[{'name':'area', 'args':[]}], "relations":[{"name":"location", "val":1.0, 'arg':{'index':0}}]}
#output[str(("exit", "NOUN"))]={"concepts":[{'name':'exit', 'args':[]}], "relations":[{"name":"exit", "val":1.0, 'arg':{'index':0}}]}

### Word Preprocessing
# Simply creates a word defining dictionary
# This dictionary is composed of :
# - concepts : an empty dictionary
# - mods : an empty dictionary
# - relations : an empty dictionary
# - sentence : dictionary of each word of the definition, each element is componsed of :
#   - key : (word, pos), dictionary :
#       - main : boolean representing if the word if the word is not an argument of another
#       - unready : integral representing the number of undefined arguments of the word
#       - shead : (sword, spos), tuple representing the sentence head of the word
#       - dep : string representing the dependance relative to its head, ex: "amod"
#       - chain : list of dictionaries adding information to dependance, ex: [{"lemma":"lemma", "dep":"dep"}, ...]

def preprocess_word(definition):
        # Language processing
        doc = nlp(definition)
        sentence = {}
        for token in doc:
            if token.pos_ in ['NOUN', 'ADJ', 'VERB']:
                sentence[(token.lemma_, token.pos_)] = {'main':False, 'unready':0}
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
        return {"concepts":{}, "mods":{}, "relations":{}, "sentence":sentence}

### Sentence processing

def get_next_key(dictionary):
    i = 0
    keys = list(dictionary.keys())
    if keys:
        i = max(keys) + 1
    return i

def process_sentence(w):
    out = output[w]
    if 'sentence' in out:
        # Init
        out['phrase'] = deepcopy(out['sentence'])
        out['concepts'] = {}
        out['mods'] = {}
        out['relations'] = {}
        # First propagate
        for sw in out['phrase']:
            ssw = str(sw)
            if ssw in output:
                sout = output[ssw]
                out['phrase'][sw]['concepts'] = deepcopy(sout['concepts'])
                out['phrase'][sw]['mods'] = deepcopy(sout['mods'])
                out['phrase'][sw]['relations'] = deepcopy(sout['relations'])
            else:
                out['phrase'][sw]['concepts'] = {}
                out['phrase'][sw]['mods'] = {}
                out['phrase'][sw]['relations'] = {}
            out['phrase'][sw]['addc'] = {} # add concepts : concepts added using the phrase
            out['phrase'][sw]['addm'] = {} # add mods : mods added using the phrase
            out['phrase'][sw]['addr'] = {} # add relations : relations added using the phrase
        # Process phrase
        sentence_processing = True
        while sentence_processing:
            sentence_processing = False
            for sw in out['phrase']:
                sdict = out['phrase'][sw]
                if sdict['unready'] == 0:
                    # Continue computation
                    sentence_processing = True
                    # Add addc, addr to self
                    # Find i
                    i = get_next_key(sdict['concepts'])
                    # Construct sdict
                    for addi in sdict['addc']:
                        sdict['concepts'][i + addi] = deepcopy(sdict['addc'][addi])
                        sdict['mods'][i + addi] = deepcopy(sdict['addm'][addi])
                        sdict['relations'][i + addi] = deepcopy(sdict['addr'][addi])
                        for r in sdict['relations'][i + addi]:
                            r['index'] += i
                    # Add self to shead addc, addr
                    if not sdict['main']:
                        hdict = out['phrase'][sdict['shead']]
                        # Find addi
                        addi = get_next_key(hdict['addc'])
                        # Find hi
                        hi = get_next_key(hdict['concepts'])
                        # Construct hdict
                        for i in sdict['concepts']:
                            hdict['addc'][addi +  i] = deepcopy(sdict['concepts'][i])
                            hdict['addm'][addi +  i] = deepcopy(sdict['mods'][i])
                            hdict['addr'][addi +  i] = deepcopy(sdict['relations'][i])
                            for r in hdict['addr'][addi +  i]:
                                r['index'] += addi
                            # If added concept has not already been used
                            if not hdict['addc'][addi +  i]['used']:
                                for j in hdict['concepts']:
                                    # If head concept has not already been used
                                    if not hdict['concepts'][j]['used']:
                                        # Relate them with dependance and chain
                                        hdict['relations'][j].append({'dep':sdict['dep'], 'chain':sdict['chain'], 'index':hi + addi + i})
                        hdict['unready'] -= 1
                    sdict['unready'] -= 1
                    # Big finish, add all concepts and relations if main
                    if sdict['main']:
                        # Find i
                        i = get_next_key(out['concepts'])
                        # Construct out
                        for si in sdict['concepts']:
                            out['concepts'][i + si] = deepcopy(sdict['concepts'][si])
                            out['mods'][i + si] = deepcopy(sdict['mods'][si])
                            out['relations'][i + si] = deepcopy(sdict['relations'][si])
                            for r in out['relations'][i + si]:
                                r['index'] += i
### Relations processing

def process_relations(w):
    word, pos = eval(w)
    out = output[w]
    # Loop on concepts
    for concept_index in out['concepts']:
        # Get the concept type
        concept_type = max(out['concepts'][concept_index]['type'], key=out['concepts'][concept_index]['type'].get)
        # Loop in relation of this specific concept, using iterator in order to use the remove_relation function
        for i in range(len(out['relations'][concept_index])):
            relation_i = out['relations'][concept_index][i]
            # Getting relation concept info
            relation_dep = relation_i['dep']
            relation_chain = relation_i['chain']
            relation_concept_index = relation_i['index']
            relation_concept_type = max(out['concepts'][relation_concept_index]['type'], key=out['concepts'][relation_concept_index]['type'].get)
            # If concept has a subject then concept is used
            if relation_dep == 'nsubj' or relation_dep == 'nsubjpass':
                out['concepts'][concept_index]['used'] = True
            else:
                out['concepts'][relation_concept_index]['used'] = True
        # Second step remove the used concept that you can process (i.e adj with dep amod)

def compute(input_words, nb):
    words = input_words
    print("COMPUTE : Preprocess")
    for w in words:
        if not (w in output):
            word, pos = eval(w)
            definition = words[w]
            if definition[0] == '(':
                definition = definition[definition.find(')') + 2:]
            # Removing (s)
            definition = definition.replace('(s)', '') # fix for the word 'furniture'
            # Replacing ; by .
            definition = definition.replace(';', '.') # fix for the word 'throw'
            # Preprocessing
            output[w] = preprocess_word(definition)
        else:
            print("Word already defined !", w)
    print("COMPUTE : Propagation")
    for i in range(nb):
        print("COMPUTE :", i, "/", nb)
        for w in words:
            word, pos = eval(w)
            out = output[w]
            ## Process sentence
            process_sentence(w)
            ## Process relations
            process_relations(w)
            ## Process synonyms TODO

## Test
#test = str(('throw', 'VERB'))
#definition = words[test].replace('(s)', '')
#doc = nlp(definition)
#print(test, definition)
#for token in doc:
#    print('WORD :', token.lemma_, token.pos_, token.dep_, 'HEAD :', token.head.lemma_, token.head.pos_, token.head.dep_)

print("COMPUTE : Start")
compute(words, 1)
print("COMPUTE : End")

print("CLEANING : Reformating output")
for w in output:
    if 'sentence' in output[w]:
        # Clean sentence
        #output[w]['phrase'] = {str(t):output[w]['phrase'][t] for t in output[w]['phrase']}
        output[w].pop('phrase')
        #output[w]['sentence'] = {str(t):output[w]['sentence'][t] for t in output[w]['sentence']}
        output[w].pop('sentence')

print("STORING : output.json")
with open('output.json', 'w') as f:
    json.dump(output, f, sort_keys=True, indent=4)
