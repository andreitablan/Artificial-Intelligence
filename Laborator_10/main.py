import pprint
import rdflib
import lightrdf
from owlready2 import *
import rdflib.term
from rdflib import Graph
from random import randint
import nltk
from nltk.corpus import wordnet as wn


def exemple_nlth():
    # nltk.download('omw-1.4')
    # nltk.download('wordnet')
    wn.synsets('dog')
    wn.synsets('dog', pos=wn.VERB)
    wn.synset('dog.n.01')
    print(wn.synset('dog.n.01').definition())
    print(wn.synset('dog.n.01').examples()[0])


def get_synset(word):
    '''
    :param word: a string parameter
    :return: the synsets of the word(complete form)
    '''
    return wn.synsets(word)


def get_first_synonim(word):
    '''
    :param word:
    :return: the name of the most common synonyms of a word if it exists
    '''
    if len(wn.synsets(word)) > 1:
        syn = wn.synsets(word)[1]
        name = syn.name()
    elif len(wn.synsets(word)) == 0:
        return word
    else:
        syn = wn.synsets(word)[0]
        name = syn.name()
    return name.split(".")[0]


def print_synset():
    '''
    Display the synsets a word entered at the command line belongs to
    '''
    answer = input("Write a word to get it's synsets: ")
    print(get_synset(answer.lower()))


def get_relations():
    '''
    Prints and returns triplets
    :return: a list with triplets: concept1-relation-concept2
    '''
    graph = Graph()
    graph.parse("food.rdf")
    triplet_relation = []
    for subject, predicate, object in graph:
        if isinstance(subject, rdflib.term.URIRef):
            s = subject.split('#')[-1]
        else:
            s = None
        if isinstance(predicate, rdflib.term.URIRef):
            p = predicate.split('#')[-1]
        else:
            p = None
        if isinstance(object, rdflib.term.URIRef):
            o = object.split('#')[-1]
        else:
            o = None
        if s is not None and p is not None and o is not None:
            triplet_relation.append((s, p, o))
            print(f"{s} -- {p} -- {o}")
    return triplet_relation


def ask_user(relations):
    '''
    It generates random questions for the user using concept1-relation-concept2
    There are two cases:
        -It doesn't search for the synonyms of every word in Wordnet
        -It searches for the first synonym of concept1/relation/concept2 and for every synonym of <answer>
    :param relations: triplets concept1-relation-concept2
    '''
    answer = ""
    while answer != "quit":
        random_index = randint(0, len(relations))
        triplet = relations[random_index]
        expected_answer = ""
        random_question_type = randint(0, 2)
        random_use_synset = randint(0, 1)
        random_use_synset = 1
        if random_use_synset == 0:
            expected_answer = triplet[random_question_type].lower()
            if random_question_type == 0:
                print("Who is in relation <", triplet[1], "> with <", triplet[2], ">?")
            elif random_question_type == 1:
                print("What is the relation between <", triplet[0], "> and <", triplet[2], ">?")
            elif random_question_type == 2:
                print("Who is <", triplet[0], "> in relation <", triplet[1], "> with?")
        else:
            expected_answer = get_first_synonim(triplet[random_question_type].lower())
            synonim_concept1 = get_first_synonim(triplet[0])
            synonim_relation = get_first_synonim(triplet[1])
            synonim_concept2 = get_first_synonim(triplet[2])

            if random_question_type == 0:
                print("Who is in relation <", synonim_relation, "> with <", synonim_concept2, ">?")
            elif random_question_type == 1:
                print("What is the relation between <", synonim_concept1, "> and <", synonim_concept2, ">?")
            elif random_question_type == 2:
                print("Who is <", synonim_concept1, "> in relation <", synonim_relation, "> with?")

        answer = input("Answer: ")
        answer_synsets = get_synset(answer.lower())

        correct = False
        if answer.lower() == expected_answer:
            print("It is correct!")
            correct = True
        if correct is False:
            for synset in answer_synsets:
                name = synset.name()
                name = name.split(".")[0]
                if name.lower() == expected_answer:
                    print("It is correct!")
                    correct = True
                    break
        if correct is False:
            print("It is not correct!")


if __name__ == '__main__':
    # exemple_nlth
    relations = get_relations()
    print_synset()
    ask_user(relations)
