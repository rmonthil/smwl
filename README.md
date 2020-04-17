# SMWL

**Search for the Minimum set of Words of a Language.**

The aim of this project is to find the minimum set of words to define in a language, to be able to reconstruct all of it based on a dictionary. The result of this project would be the basis of a game where the player can write words. The worlds would then appear and gain the physical properties of the meaning of the word. If verbs are well enough defined, they could be used to interact with the surrounding world.
So the less you have basis words to define, the less work it will be for the game programmer (me) to define them ! And this is good !

I think it is a problem linked to the problem of finding the minimum leaf spanning tree in a graph but it is not that simple.

Problems :
* **Cycles** : To define **river**, I may want to use the word **stream**. But to define **stream** you may want to use the word river. So if there are 'cycles' in you dictionary, more than only defining all the 'leaves' of the graph, you may need to define at least one word per cycle if you want to define completely the language. Finding these 'cycles' may be done using the Tarjan algorithm.
* **Relations** : It is really important to understand the relations between words in their definition. For example if **forest** is defined as "group of trees". You can not just classify the **Forest** into the same class as **group** or neither **tree**. You need to understand that **group** can take an argument, and that if the argument has the preposition of, then it will have this specify meaning that can be translated in something in a game. This a simple example but you can imagine really
  complicated definitions, using verbs and other stuff, so you really need to keep track of things.
* **Ambiguity** : This is maybe the worst problem. Words may have several meanings. And when used in a definition, it is very difficult to understand which definition you refer to.

Finally it seems that, it is more a problem about building a 'perfect' dictionary without any cycles but why would anyone do that ? (If you know a dictionary like that, please tell me !) And it is far to beyond my competences to do this myself.

Other Problems :

* **Context** : Definitions can be quite simple. Let's say that a **Forest** is a 'group of trees'. It is kind of correct but when you think about the trees. You know that there are mushrooms, animals, grass, different kinds of plants for example. So definitions are not fully sufficient to describe completely a word.
* **Many Others** ...

So finally what is this about ? I'm not a programmer, I'm not a mathematician neither and I really for from a scientist in linguistics. I just want to create a game so I just try to tackle each problem, one at a time and see how it goes. I already have idea to tackle other problems, but let's stick to the main one first : **finding the main properties of a word** that can describe it's behaviour and interactions. For this I obviously need to create big classes and keep a bit the track of the
relations between words in definitions (for the **group** concept for example).

My work so far has be to create the two python files you can find here and it is really far from finished. If you want to help me with this, please feel free do so !

The files :
* **fetchdict.py** basically download recursively part of the wiktionary based on the part of speech (for now, I just get nouns, adjectives and verbs) and on their presence in a specific wanted list. It is a simple script made using the great python module **wiktionaryparser**. It is done in a very bad way so that it does a lot of requests ...
* **propagate.py** defines a set of 'modifiers' and attach them to some words and finally propagate them in the whole dictionary. The propagation uses Natural Language Processing using the python module spaCy. The 'propagation' is kind of an iterative version of a graph search in order(to have a better control on the depth of the search and because I think Python don't like so much recursivity.

## REQUIREMENTS

You will need Python3, wikitionaryparser and spaCy.

## Use

### Fetching the wiktionary

```
python3 fetchdict.py
```
The result will be stored in the ***dict.json*** file. 
During the process data is saved several times in the output file so that the process can be stopped and resumed.

### Creating dictionary

```
python3 propagate.py
```

This will read the words stored in the ***dict.json*** file.
The result will be stored in ***output.json***.

## TODO

* To many things !
