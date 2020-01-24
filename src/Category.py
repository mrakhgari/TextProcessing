# auther: _MuhmdrezA <mra.akhgari@gmail.com>
# version: 1.0.0
# Category class, contains name of class (category's name) and unigram and bigram of senctences.

from math import log


class Category:
    def __init__(self, category_name):
        self.__name = category_name
        self.__number_of_words = 0
        self.__unigram = {}
        self.__bigram = {}
        self.__probability = 0

    def __str__(self):
        return str(self.__name) + ' ' + str(self.__probability)

    # check that two Category has same name or not?
    def __eq__(self, other):
        if isinstance(other, str):
            return self.__name == other
        if not isinstance(other, Category):
            return False
        return self.__name == other.__name

    def __hash__(self):
        return hash(self.__name)

    def get_name(self):
        return self.__name

    def get_unigrams(self):
        return self.__unigram

    def get_bigrams(self):
        return self.__bigram

    def add_unigram(self, word):
        if (self.__unigram.get(word) is None):
            self.__unigram[word] = 0
        self.__unigram[word] += 1
        self.__number_of_words += 1

    def add_bigram(self, words):
        w = words[0] + ' ' + words[1]
        if self.__bigram.get(w) is None:
            self.__bigram[w] = 0
        self.__bigram[w] += 1

    def add_sentence(self, sentence):
        words = sentence.split()
        for index in range(len(words)):
            self.add_unigram(words[index])
            if index != len(words) - 1:
                self.add_bigram((words[index], words[index+1]))
        self.__probability += 1

    def set_probability(self, count):
        self.__probability = log(self.__probability / count)
        # self.__probability = self.__probability / count

    def set_p(self, LAMBDA, word):
        ci_1 = 0 
        if self.__unigram.get(word[0]) is not None:
            ci_1 = self.__unigram[word[0]]
        ci = 0 
        if self.__unigram.get(word[1]) is not None:
            ci = self.__unigram[word[1]]
        
        pi = 0
        if ci != 0:
            pi = log(ci / self.__number_of_words)
        ci_1ci = 0
        pi_1pi = 0
        if self.__bigram.get(word[0] + ' ' + word[1]) is not None and ci_1 != 0:
            ci_1ci = self.__bigram.get(word[0] + ' ' + word[1])
            pi_1pi = log(ci_1ci / ci_1)
        return LAMBDA*pi + (1-LAMBDA) * pi_1pi

    def get_p(self):
        return self.__probability
