#

import numpy as np
import urllib.request
from collections import defaultdict, Counter
import random

from text_analysis_class import MarkovModel

# Grimms' Fairy Tales by Jacob and Wilhelm Grimm
data_url = 'http://www.gutenberg.org/files/2591/2591-0.txt'
corpus = urllib.request.urlopen(data_url).read().decode("utf-8")

# remove the first chunk of characters, which contains some header stuff
corpus = corpus[2820:]

# print(corpus[:200])  # print out the first 200 characters

# код выше взят из твоего задания, дальше булет работа с типом данных str()
# тебе будет нужно самой поменять источник данных (это, вроде есть в задании)

# вводим количество символов, которое берется за основу
# n = int(input())
# пока не будем использовать вообще

# берем срез текста состоящий из 2000 символов
work_text = corpus[:2000].lower()

# дополнительные символы такие как "новая строка" ('\n') влияют на len()
# эта строка ниже проверяет есль ли неотображаемые символы в этом тексте
# print(work_text.isspace())

# вызываем методы из класса в соседнем файле
# вместо того чтобы вводить "n" с клавиатуры, передадим сразу число
first_mod = MarkovModel(work_text, 3)
first_mod.generate()
first_mod.fit()

# просто инпут требует нажатия любой клавиши чтобы продолжить выполнение
# программы т.к. у нас нет ничего дальше, программа завершается
# input()
