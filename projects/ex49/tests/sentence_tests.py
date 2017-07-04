from nose.tools import *
from ex49 import lexicon
from ex49 import sentence


def test_peek():
    word_list = lexicon.scan("I love you")
    assert_equal(sentence.peek(word_list), "noun")

def test_match():
    word_list = lexicon.scan("eat the bear")
    assert_equal(sentence.match(word_list, "verb"), ("verb", "eat"))


def test_skip():
    word_list = lexicon.scan("eat the bear")
    assert_equal(sentence.skip(word_list, 'verb'), None)

def test_parse_verb():
    word_list = lexicon.scan("eat the bear")
    assert_equal(sentence.parse_verb(word_list), ("verb", "eat"))


def test_parse_object():
    word_list = lexicon.scan("I love you")
    assert_equal(sentence.parse_object(word_list), ("noun", "I"))


def test_parse_subject():
    word_list = lexicon.scan("love you")
    sobj = sentence.parse_subject(word_list, ("noun", "I"))
    print sobj
    assert_equal(sobj.object, "you")
    assert_equal(sobj.subject, "I")
    assert_equal(sobj.verb, "love")

