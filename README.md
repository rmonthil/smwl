# SMWL

**Search for the Minimum set of Words of a Language.**

The aim of this project is to find the minimum set of words to define in a language, to be able to reconstruct all of it based on a dictionary. This project would be the basis of a game where the player can create objects while writting words. The words would appear and gain physical properties based on it's meaning. And if verbs are well enough defined, they could be used to interact with the surrounding words.

The less words are found to be essential to define, the less words the game programmer will need to define.

This problem may be linked in some way to the problem of finding the minimum leaf spanning tree in a graph but it is not that simple.

Problems :
* **Cycles** : To define **river**, I may want to use the word **stream**. But to define **stream** I may want to use the word river. So if there are 'cycles' in you dictionary, more than only defining all the 'leaves' of the graph, you may need to define at least one word per cycle if you want to define completely the language. Finding these **cycles** may be done using the Tarjan algorithm.
* **Relations** : It is really important to understand the relations between words in their definition. For example if **forest** is defined as "group of trees". You can not just classify the **forest** into the same class as **group** or neither **tree**. You need to understand that **group** can take an argument, and that if the argument has the preposition of, then it will have this specific meaning that can be translated in something in the game. This a simple example but you can imagine really complicated definitions, using verbs where relations between words are really important.
* **Ambiguity** : This is maybe the worst problem. Words may have several meanings. And when used in a definition, it is very difficult to understand which definition is used.

Finally it seems that, it is more a problem about building a 'perfect' dictionary, but I think it is impossible.

Other Problems :

* **Context** : Definitions can be quite simple. Let's say that a **forest** is a **group of trees**. It is kind of correct but when you think about the forest, you know that there are mushrooms in a it, animals, grass, other different kinds of plants... So definitions are not fully sufficient to describe completely a concept. We may need to refer to an encylopedia.
* **Many Others** ...

I'm not a computer scientist, I'm not a mathematician neither and know almost nothing of the field of linguistics. It is maybe the wrong approach but we'll see where this goes.

The files you can find in this project :
* **fetchdict.py** basically downloads recursively part of the wiktionary based on its part of speech (for now, I just get nouns, adjectives and verbs) and on their presence in a specific list. It is a simple script made using the great python module **wiktionaryparser**.
* **propagate.py** defines a set of 'modifiers' and attach them to some words and finally propagate them in the whole dictionary. The propagation uses Natural Language Processing using the python module spaCy. The 'propagation' is kind of an iterative version of a graph search in order to have a better control on the depth of the search and because I think Python don't like so much recursivity.

## Requirements

If you want to run the python files, you will need **Python3**, **wikitionaryparser** and **spaCy**.

## Use

This is an active work in progress, the master branch may not work always work properly. Carefull when running the following scripts, at the moment it is very unsafe and it may use all your memory, making your computer freeze. Run it at your own risks.

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

## Todo

* Clean used bat not arg neither has subj

## Why the Godot project files are not here ?

Most of the hardest work is here, then it is just about creating a game based on the generated database. Each game designer may want to create different games based on this. In my case, I am still not sure what I really want to do so, for now at least, the Godot project will stay private. When it will be finished, it might be open-source though.

## License

This project is licensed under the Unlicense - see the [LICENSE](./LICENSE) file for details
