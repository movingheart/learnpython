# -*- coding:utf-8 -*-

class ParserError(Exception):
    pass 
    
class Sentence(object):
    def __init__(self, subject, verb, object):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):
    """ 查看词的类型
    
    :param word_list: 
    :return: 词语的类型 或 None
    """
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    """ 匹配期望的词语类型
    
    :param word_list: 
    :param expecting: 
    :return: （匹配expecting类型的词语,词性）
    """
    if word_list:
        word = word_list.pop(0)
        
        if word[0] == expecting:
            return word
        else:
            return None
            
    else:
        return None


def skip(word_list, word_type):
    """ 跳过某类型的词
    
    :param word_list: 
    :param word_type: 
    :return: None
    """
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    """ 返回动词 """
    skip(word_list, 'stop')
    
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Excepted a verb next")


def parse_object(word_list):
    """ 返回宾语 """
    skip(word_list, 'stop')
    next = peek(word_list)
    
    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Excepted a noun or direction next.")


def parse_subject(word_list, subj):
    """ 解析主题：有主语之后，返回组成的句子 """
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    
    return Sentence(subj, verb, obj)


def parse_sentence(word_list):
    """ 解析句子：返回最后的句子 """
    skip(word_list, 'stop')
    
    start = peek(word_list)
    
    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject , object, or verb not: %s" % start)
