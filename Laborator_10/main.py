import pprint
import rdflib
import lightrdf
from owlready2 import *
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
    graph = rdflib.Graph()
    graph.open("store", create=True)
    graph.parse("food.rdf")
    # print out all the triples in the graph
    for subject, predicate, object in graph:
        print(subject, predicate, object)
        print("------------------------------")

    g = rdflib.Graph()
    g.parse("food.rdf")
    for stmt in g:
        for index in range(0, len(stmt)):
            if str(type(stmt[index])) != '<class \'rdflib.term.BNode\'>':
                print(stmt[index])

        print("-----------------------AAA---------------")

    f = open('food.rdf', 'rb')
    doc = lightrdf.RDFDocument(f, parser=lightrdf.xml.PatternParser)
    for (s, p, o) in doc.search_triples(None, None, None):
        print(s, p, o)


if __name__ == '__main__':
    print_rdf()
