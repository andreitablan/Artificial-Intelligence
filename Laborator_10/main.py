import pprint

import rdflib.term
from rdflib import Graph
import nltk
from nltk.corpus import wordnet as wn


def ok_nlth():
    # nltk.download('omw-1.4')
    # nltk.download('wordnet')
    wn.synsets('dog')
    wn.synsets('dog', pos=wn.VERB)
    wn.synset('dog.n.01')
    print(wn.synset('dog.n.01').definition())
    print(wn.synset('dog.n.01').examples()[0])


def print_rdf():
    g = Graph()
    g.parse("food.rdf")
    for stmt in g:
        for index in range(0,len(stmt)):
            if str(type(stmt[index])) != '<class \'rdflib.term.BNode\'>':
                print(stmt[index])
        print("-----------------------AAA---------------")


if __name__ == '__main__':
    print_rdf()
