# SMWL

Search for the Minimum set of Words of a Language.
The current work is done for the French Language and currently not working.

## REQUIREMENTS

You will need Python3 to parse wikipedia.
You will need Beautifulsoup4 to parse html5 data. Install it using :

```
pip3 install beautifulsoup4
```

## Principle

The software aims to parse Wikipedia and to return the smallest amount of words that are needed to define all french words.
In order to rebuild correctly dependencies, the relevance of the words in the definitions are needed. 
To estimate this quantity, the number of occurence of those words in the whole article where used.

## Use

### Parsing Wikipedia

Move to the `linksParser` folder and execute the file createDict.py with python3.

```
python3 createDict.py
```

This will read all words stored in ***dictin.json*** file and parse wikipedia until all of them and their dependencies are processed.
The result will be stored in the ***dict.json*** file. 
During the process data is saved several times in the output file so that the process can be stoped and resumed.

### Creating dictionary

Move to the `min_words_search` folder and execute the file app.py with python3.

```
python3 app.py
```

This will read the words stored in the ***dict.json*** file. Then it will use the Tarjan Algorithme to convert the ***graph*** obtained when parsing wikipedia into a ***forest***.
This will remove all cycles in the graph that we do not want. When we have this, all leafs of all trees can be considered as all the words that need to be defined to define the whole language.

The result will be stored in ***words.json*** and ***parts.json***. The first will contained the formed ***forest***. And the second will contain all strongly connected components (called here a "part") that are leaves.

## TODO

* Test with all links in page.
* Test with all words in first sentence. (but ambigutïe ?)
