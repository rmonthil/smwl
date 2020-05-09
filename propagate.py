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
output[str(("vegetal", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"vegetal", "val":1.0, 'arg':{'index':0}}]}
output[str(("body", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"body", "val":1.0, 'arg':{'index':0}}]}
output[str(("static", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"static", "val":1.0, 'arg':{'index':0}}]}
output[str(("burning", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"burning", "val":1.0, 'arg':{'index':0}}]}
output[str(("fluid", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
output[str(("vehicle", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"vehicle", "val":1.0, 'arg':{'index':0}}]}
output[str(("transport", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"vehicle", "val":1.0, 'arg':{'index':0}}]}
output[str(("animal", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"animal", "val":1.0, 'arg':{'index':0}}]}
output[str(("edible", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"edible", "val":1.0, 'arg':{'index':0}}]}
output[str(("weapon", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"weapon", "val":1.0, 'arg':{'index':0}}]}
output[str(("group", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
output[str(("plural", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
output[str(("moving", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"moving", "val":1.0, 'arg':{'index':0}}]}
output[str(("solid", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"solid", "val":1.0, 'arg':{'index':0}}]}
output[str(("exit", "ADJ"))]={"concepts":[{'name':'adj', 'args':[]}], "relations":[{"name":"exit", "val":1.0, 'arg':{'index':0}}]}

# Verbs
output[str(("cause", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"cause", "val":1.0, 'arg':{'index':0}}]} # Can have an other relation as an argument ?
output[str(("have", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"have", "val":1.0, 'arg':{'index':0}}]}
output[str(("grab", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"have", "val":1.0, 'arg':{'index':0}}]}
output[str(("take", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"have", "val":1.0, 'arg':{'index':0}}]}
output[str(("hold", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"have", "val":1.0, 'arg':{'index':0}}]}
output[str(("be", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"be", "val":1.0, 'arg':{'index':0}}]}
output[str(("move", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"move", "val":1.0, 'arg':{'index':0}}]}
output[str(("use", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"use", "val":1.0, 'arg':{'index':0}}]}
output[str(("become", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"become", "val":1.0, 'arg':{'index':0}}]}
output[str(("consume", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"consume", "val":1.0, 'arg':{'index':0}}]}
output[str(("attack", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"hit", "val":1.0, 'arg':{'index':0}}]}
output[str(("turn", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"turn", "val":1.0, 'arg':{'index':0}}]}
output[str(("drop", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"drop", "val":1.0, 'arg':{'index':0}}]}
output[str(("hit", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"hit", "val":1.0, 'arg':{'index':0}}]}
output[str(("create", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"create", "val":1.0, 'arg':{'index':0}}]}
output[str(("build", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"create", "val":1.0, 'arg':{'index':0}}]}
output[str(("produce", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"create", "val":1.0, 'arg':{'index':0}}]}
output[str(("enter", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"enter", "val":1.0, 'arg':{'index':0}}]}
output[str(("exit", "VERB"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"exit", "val":1.0, 'arg':{'index':0}}]}

# Nouns
output[str(("member", "NOUN"))]={"concepts":[{'name':'member', 'args':[]}], "relations":[{"name":"being", "val":1.0, 'arg':{'index':0}}]}
output[str(("object", "NOUN"))]={"concepts":[{'name':'object', 'args':[]}], "relations":[{"name":"object", "val":1.0, 'arg':{'index':0}}]}
output[str(("plant", "NOUN"))]={"concepts":[{'name':'plant', 'args':[]}], "relations":[{"name":"vegetal", "val":0.33, 'arg':{'index':0}}, {"name":"body", "val":0.33, 'arg':{'index':0}}, {"name":"static", "val":0.33, 'arg':{'index':0}}]}
output[str(("body", "NOUN"))]={"concepts":[{'name':'body', 'args':[]}], "relations":[{"name":"body", "val":1.0, 'arg':{'index':0}}]}
output[str(("item", "NOUN"))]={"concepts":[{'name':'item', 'args':[]}], "relations":[{"name":"body", "val":1.0, 'arg':{'index':0}}]}
output[str(("fire", "NOUN"))]={"concepts":[{'name':'fire', 'args':[]}], "relations":[{"name":"burning", "val":1.0, 'arg':{'index':0}}]}
output[str(("fluid", "NOUN"))]={"concepts":[{'name':'fluid', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
output[str(("liquid", "NOUN"))]={"concepts":[{'name':'liquid', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
output[str(("water", "NOUN"))]={"concepts":[{'name':'water', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
output[str(("vehicle", "NOUN"))]={"concepts":[{'name':'vehicle', 'args':[]}], "relations":[{"name":"vehicle", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
output[str(("transport", "NOUN"))]={"concepts":[{'name':'transport', 'args':[]}], "relations":[{"name":"vehicle", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
output[str(("animal", "NOUN"))]={"concepts":[{'name':'animal', 'args':[]}], "relations":[{"name":"animal", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
output[str(("being", "NOUN"))]={"concepts":[{'name':'being', 'args':[]}], "relations":[{"name":"animal", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
output[str(("food", "NOUN"))]={"concepts":[{'name':'food', 'args':[]}], "relations":[{"name":"edible", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
output[str(("weapon", "NOUN"))]={"concepts":[{'name':'weapon', 'args':[]}], "relations":[{"name":"weapon", "val":0.5, 'arg':{'index':0}}, {"name":"body", "val":0.5, 'arg':{'index':0}}]}
output[str(("group", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
output[str(("tract", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
output[str(("extent", "NOUN"))]={"concepts":[{'name':'group', 'args':[]}], "relations":[{"name":"group", "val":1.0, 'arg':{'index':0}}]}
output[str(("stream", "NOUN"))]={"concepts":[{'name':'stream', 'args':[]}], "relations":[{"name":"stream", "val":1.0, 'arg':{'index':0}}]}
output[str(("source", "NOUN"))]={"concepts":[{'name':'source', 'args':[]}], "relations":[{"name":"source", "val":1.0, 'arg':{'index':0}}]}
output[str(("air", "NOUN"))]={"concepts":[{'name':'air', 'args':[]}], "relations":[{"name":"fluid", "val":1.0, 'arg':{'index':0}}]}
output[str(("movement", "NOUN"))]={"concepts":[{'name':'movement', 'args':[]}], "relations":[{"name":"group", "val":0.5, 'arg':{'index':0}}, {"name":"moving", "val":0.5, 'arg':{'index':0}}]}
output[str(("motion", "NOUN"))]={"concepts":[{'name':'motion', 'args':[]}], "relations":[{"name":"group", "val":0.5, 'arg':{'index':0}}, {"name":"moving", "val":0.5, 'arg':{'index':0}}]}
output[str(("action", "NOUN"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"action", "val":1.0, 'arg':{'index':0}}]}
output[str(("act", "NOUN"))]={"concepts":[{'name':'action', 'args':[]}], "relations":[{"name":"action", "val":1.0, 'arg':{'index':0}}]}
output[str(("building", "NOUN"))]={"concepts":[{'name':'building', 'args':[]}], "relations":[{"name":"body", "val":0.33, 'arg':{'index':0}}, {"name":"location", "val":0.33, 'arg':{'index':0}}, {"name":"static", "val":0.33, 'arg':{'index':0}}]}
output[str(("location", "NOUN"))]={"concepts":[{'name':'location', 'args':[]}], "relations":[{"name":"location", "val":1.0, 'arg':{'index':0}}]}
output[str(("place", "NOUN"))]={"concepts":[{'name':'place', 'args':[]}], "relations":[{"name":"location", "val":1.0, 'arg':{'index':0}}]}
output[str(("region", "NOUN"))]={"concepts":[{'name':'region', 'args':[]}], "relations":[{"name":"location", "val":1.0, 'arg':{'index':0}}]}
output[str(("area", "NOUN"))]={"concepts":[{'name':'area', 'args':[]}], "relations":[{"name":"location", "val":1.0, 'arg':{'index':0}}]}
output[str(("exit", "NOUN"))]={"concepts":[{'name':'exit', 'args':[]}], "relations":[{"name":"exit", "val":1.0, 'arg':{'index':0}}]}

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

def process_sentence(w):
    out = output[w]
    if 'fsentence' in out:
        # Init
        out['sentence'] = deepcopy(out['fsentence'])
        out['concepts'] = []
        out['relations'] = []
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
            out['sentence'][sw]['addc'] = [] # add concepts : concepts added using the sentence
            out['sentence'][sw]['addr'] = [] # add relations : relations added using the sentence
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
                        sdict['concepts'][-1]['index'] = len(sdict['concepts']) - 1
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
                                hdict['addc'][-1]['index'] = len(hdict['addc']) - 1
                                if 'args' in hdict['addc'][-1]:
                                    for a in hdict['addc'][-1]['args']:
                                        a['index'] += offset
                                if not 'is_arg' in c or not c['is_arg']:
                                    for hc in hdict['concepts']:
                                        if 'args' in hc and (not 'is_arg' in hc or not hc['is_arg']):
                                            hc['args'].append({'dep':sdict['dep'], 'chain':sdict['chain'], 'index':offset + len(hdict['addc']) - 1})
                            for r in sdict['relations']:
                                hdict['addr'].append(deepcopy(r))
                                hdict['addr'][-1]['arg']['index'] += offset
                        hdict['unready'] -= 1
                    sdict['unready'] -= 1
                    # Big finish, add all concepts and relations if main
                    if sdict['main']:
                        offset = len(out['concepts'])
                        for c in sdict['concepts']:
                            out['concepts'].append(deepcopy(c))
                            out['concepts'][-1]['index'] = len(out['concepts']) - 1
                            if 'args' in out['concepts'][-1]:
                                for a in out['concepts'][-1]['args']:
                                    a['index'] += offset
                        for r in sdict['relations']:
                            out['relations'].append(r)
                            out['relations'][-1]['arg']['index'] += offset

def transform_final(w):
    out = output[w]
    ## Concepts to fconcepts
    fisargs = {}
    fconcepts = {}
    for c in out['concepts']:
        index = 0
        if 'index' in c:
            index = c['index']
        if index in fconcepts:
            if c['name'] in fconcepts[index]:
                fconcepts[index][c['name']] += 1.0 # hum should be + val TODO
            else:
                fconcepts[index][c['name']] = 1.0 # same TODO
        else:
            fconcepts[index] = {c['name']:1.0} # same TODO
        #if 'is_arg' in c:
        #    if c['is_arg']:
        #        fisargs[index] = True
    ## Concepts args to frelations
    frelations = {}
    for c in out['concepts']:
        index = 0
        if 'index' in c:
            index = c['index']
        frelations[index] = [a for a in c['args']]
    ## Relations to fmods
    fmods = {}
    for r in out['relations']:
        if r['arg']['index'] in fmods:
            if r['name'] in fmods[r['arg']['index']]:
                fmods[r['arg']['index']][r['name']] += r['val']
            else:
                fmods[r['arg']['index']][r['name']] = r['val']
        else:
            fmods[r['arg']['index']] = {r['name']:r['val']}
    ## Recompute is_arg
    for index in frelations:
        for r in frelations[index]:
            fisargs[r['index']] = True
    ## Setup final
    out['fmods'] = fmods
    out['fconcepts'] = fconcepts
    out['frelations'] = frelations
    out['fisargs'] = fisargs

def synonym(w, first, second):
    out = output[w]
    if first != second and second in out["fconcepts"] and first in out["fconcepts"]:
        ## concepts
        for fc in out["fconcepts"][second]:
            if fc in out["fconcepts"][first]:
                out["fconcepts"][first][fc] += out["fconcepts"][second][fc]
            else:
                out["fconcepts"][first][fc] = out["fconcepts"][second][fc]
        ## mods
        if second in out["fmods"]:
            for mod in out["fmods"][second]:
                if first in out["fmods"]:
                    if mod in out["fmods"][first]:
                        out["fmods"][first][mod] += out["fmods"][second][mod]
                    else:
                        out["fmods"][first][mod] = out["fmods"][second][mod]
                else:
                    out["fmods"][first] = {mod:out["fmods"][second][mod]}
        ## relations
        #### Update other indexs
        for index in out["frelations"]:
            for r in out["frelations"][index]:
                if r["index"] == second:
                    r["index"] = first
        ### Update relation dealing with new synonyms
        relations_first = deepcopy(out["frelations"][first])
        relations_ids = [(r['dep'], r['chain']) for r in relations_first]
        for r in out["frelations"][second]:
            if not (r['dep'], r['chain']) in relations_ids:
                out["frelations"][first].append(r)
        for r in out["frelations"][second]: # TODO, should be always !
            if (r['dep'], r['chain']) in relations_ids:
                synonym(w, relations_first[relations_ids.index((r['dep'], r['chain']))]['index'], r['index'])
        ## pop
        out["fmods"].pop(second, None)
        out["fconcepts"].pop(second, None)
        out["frelations"].pop(second, None)

def normalization(w):
    out = output[w]
    for c in out["fconcepts"]:
        tot = sum([out["fconcepts"][c][name] for name in out["fconcepts"][c]])
        out["fconcepts"][c] = {name:out["fconcepts"][c][name]/tot for name in out["fconcepts"][c]}
    for m in out["fmods"]:
        tot = sum([out["fmods"][m][name] for name in out["fmods"][m]])
        out["fmods"][m] = {name:out["fmods"][m][name]/tot for name in out["fmods"][m]}

def back_to_sentence_processing(w):
    out = output[w]
    ## Back to concepts
    out['concepts'] = []
    for index in out["fconcepts"]:
        name = max(out["fconcepts"][index], key=out["fconcepts"][index].get)
        out['concepts'].append({"name":name, "index":index, "args":out["frelations"][index]})
        if index in out["fisargs"]:
            out['concepts'][-1]['is_arg'] = out["fisargs"][index]
    out.pop('fisargs')
    ## Back to relations
    out['relations'] = []
    for index in out["fmods"]:
        for name in out["fmods"][index]:
            out['relations'].append({"name":name, "val":out["fmods"][index][name], "arg":{"index":index}})

def remove_concept(w, index):
    out = output[w]
    if index in out["fmods"]:
        out["fmods"].pop(index)
    out["fconcepts"].pop(index)
    for i in range(len(out["frelations"][index])):
        if out["frelations"][index][i] != None:
            remove_relation(w, index, i)

def remove_relation(w, index, i):
    out = output[w]
    if out["frelations"][index][i]["index"] in out["fconcepts"]:
        remove_concept(w, out["frelations"][index][i]["index"])
    out["frelations"][index][i] = None

def clean_relations(w):
    out = output[w]
    # Clean relations
    pops = []
    for index in out["frelations"]:
        if index in out["fconcepts"]:
            out["frelations"][index] = [a for a in out["frelations"][index] if a != None]
        else:
            pops.append(index)
    for p in pops:
        out["frelations"].pop(p)
    # Clean mods also
    pops = []
    for index in out["fmods"]:
        if not index in out["fconcepts"]:
            pops.append(index)
    for p in pops:
        out["fmods"].pop(p)

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
            ## Transform to final state
            transform_final(w)
            ## Synonym management
            if pos == 'VERB' or pos == 'ADJ':
                for index in list(out['fconcepts'].keys()):
                    if index != 0 and (not index in out['fisargs'] or not out['fisargs'][index]):
                        synonym(w, 0, index)
            ## TODO Process relations, dep treatement, amod, verbs and compress data !!!
            for index in out['frelations']:
                if index in out['fconcepts']:
                    name = max(out['fconcepts'][index], key=out['fconcepts'][index].get) # TODO use this !
                    for i in range(len(out['frelations'][index])):
                        r = out['frelations'][index][i]
                        treated = False
                        if r != None:
                            if r['index'] in out['fconcepts']:
                                if name == 'action':
                                    treated = True
                                    if r['dep'] == 'nsubj' and r['chain'] == []:
                                        nsubj_index = r['index']
                                        nsubj_name = max(out['fconcepts'][nsubj_index], key=out['fconcepts'][nsubj_index].get)
                                        if nsubj_name != 'action' and nsubj_name != 'adj':
                                            pass
                                        else:
                                            remove_relation(w, index, i)
                                    elif r['dep'] == 'nsubjpass' and r['chain'] == []:
                                        nsubjpass_index = r['index']
                                        nsubjpass_name = max(out['fconcepts'][nsubjpass_index], key=out['fconcepts'][nsubjpass_index].get)
                                        if nsubjpass_name != 'action' and nsubjpass_name != 'adj':
                                            pass
                                        else:
                                            remove_relation(w, index, i)
                                    elif r['dep'] == 'dobj' and r['chain'] == []:
                                        dobj_index = r['index']
                                        dobj_name = max(out['fconcepts'][dobj_index], key=out['fconcepts'][dobj_index].get)
                                        if dobj_name != 'action' and dobj_name != 'adj':
                                            pass
                                        else:
                                            remove_relation(w, index, i)
                                    else:
                                        remove_relation(w, index, i)
                                else:
                                    if r['dep'] == 'amod':
                                        # Treat
                                        treated = True
                                        amod_index = r['index']
                                        amod_name = max(out['fconcepts'][amod_index], key=out['fconcepts'][amod_index].get)
                                        ## if amod is a adj (mostly adjectives)
                                        if amod_name == 'adj':
                                            ## Share mods TODO code refactoring
                                            if amod_index in out["fmods"]:
                                                for mod in out["fmods"][amod_index]:
                                                    if index in out["fmods"]:
                                                        if mod in out["fmods"][index]:
                                                            out["fmods"][index][mod] += out["fmods"][amod_index][mod]
                                                        else:
                                                            out["fmods"][index][mod] = out["fmods"][amod_index][mod]
                                                    else:
                                                        out["fmods"][index] = {mod:out["fmods"][amod_index][mod]}
                                            # And remove relation
                                            remove_relation(w, index, i)
                                        # if amod is a action (mostly verbs)
                                        elif amod_name == 'action': # TODO depend of mods
                                            remove_relation(w, index, i)
                                        # if amod is an other concept (mostly nouns)
                                        else: # TODO depend of mods
                                            remove_relation(w, index, i)
                            else:
                                treated = True
                                remove_relation(w, index, i)
                        else:
                            treated = True
                        if not treated:
                            remove_relation(w, index, i)
            clean_relations(w)
            ## Normalize concepts and mods
            normalization(w)
            ## Back to "normal"
            back_to_sentence_processing(w)

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
    # Clean old
    output[w].pop('concepts')
    output[w].pop('relations')
    # Rename
    if 'fconcepts' in output[w]:
        output[w]['concepts'] = output[w]['fconcepts']
        output[w].pop('fconcepts')
        output[w]['relations'] = output[w]['frelations']
        output[w].pop('frelations')
        output[w]['mods'] = output[w]['fmods']
        output[w].pop('fmods')

print("STORING : output.json")
with open('output.json', 'w') as f:
    json.dump(output, f, sort_keys=True, indent=4)
