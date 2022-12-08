import pprint

from rdflib import Graph
import nltk
from nltk.corpus import treebank

def test_nlth():
    sentence = """At eight o'clock on Thursday morning
    ... Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    nltk.chunk.ne_chunk(tagged)
    t = treebank.parsed_sents('wsj_0001.mrg')[0]
    t.draw()

def print_rdf():
    g = Graph()
    g.parse("food.rdf")
    for stmt in g:
        pprint.pprint(stmt)


if __name__ == '__main__':
    print_rdf()
    test_nlth()