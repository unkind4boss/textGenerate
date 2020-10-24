
import numpy as np
import urllib.request
from collections import defaultdict, Counter
import random


class MarkovModel:

    def __init__(self, work_text, n):
        self.work_text = work_text
        self.n = n
        self.dict_of_dict = {}
        self.main_dict = {}
        self.p = ''
        self.generated_text = ''


    def generate(self):
        """
        с помощью np.random.choice()
        выбираем первые символы или один символ,
        которые будут искаться в тексте
    """
        # тут рандомно выбираются несколько символов из текста,
        # количесво символов определяет n (self.n)
        # self.p = np.random.choice(self.work_text, self.n)
        # self.p = ''.join(self.p)

        # тут рандомно выбирается срез из текста,
        # количесво символов определяет n (self.n)
        num = np.random.choice(len(self.work_text) - self.n - 1)
        self.p = self.work_text[num : num + self.n]
        self.p = ''.join(self.p)


    def subfit(self):
        """
        ищем индекс нужного символа с помощью медода find
        затем проверяем есть ли этот символ в нашем словаре, если нет то
        добавляем его в словарь.
        символ -- key,
        количесво таких символов -- value.
    """

        index_start_find = 0
        self.dict_of_dict = {}
        quantity_sing = self.work_text.count(self.p)
        if quantity_sing == 1:
            quantity_sing = 2

        # сдвиг, который определяет какой символ нужно взять
        sh = self.n
        # количество символов в нашем тексте s -- size
        s = len(self.work_text)

        while quantity_sing > 1:
            index_of_sind = self.work_text.find(self.p,
                                            index_start_find,
                                            len(self.work_text)
                                        )

            # % (s + 1) -- означает зацикленность индекса
            # если используемый символ окажется последним и после него нет
            # символов, то программа выдаст ошибку, в нашем же случае
            # будет взят первый символ
            if self.work_text[(index_of_sind+sh) % (s)] not in self.dict_of_dict:
                self.dict_of_dict[self.work_text[(index_of_sind+sh) % (s)]] \
                    = self.work_text.count(self.work_text[
                                            ((index_of_sind) % (s))\
                                            :((index_of_sind+sh+1) % (s+1))
                                        ])

            index_start_find = index_of_sind + sh + 1
            quantity_sing -= 1


    def choice_next_letter(self):
        """
        этот метод вызывается после метода subfit(). работаем со словорём и
        с помощью random.choices выбираем символ учитывая его частоту
        встречаемость в тексте. добовляем этот символ в общий текст
    """
        keys_list = self.dict_of_dict.keys()
        values_list = self.dict_of_dict.values()

        # тут небольшая проверка т.к.тогда и только тогада,
        # когда self.n = 1 и символ "а"
        # находится в конце словаря, этому символу присваивается
        # несоизмеримо большое число встречаемости. это не вызывает ошибку.
        # рекомендуется посмотреть каким образом строится сгенерированный текст
        # как работоет эта проверка и посмотреть на этот недостаток (ошибку).
        # if 'a' in list(keys_list):
            # print(list(keys_list), list(values_list))

        b = random.choices(list(keys_list),
                            weights=list(values_list)
                        )

        self.generated_text += b[0]
        self.p = self.generated_text[-self.n:]


    def fit(self):
        """
        в range() задается количество символов которое мы будем генерировать
        и каждую итерацию вызываются методы, которые
        1 создает словарь
        2 выбирает символ из этого словоря
        не забывая при этом создать словарь словарей.
    """
        self.generated_text = self.p
        for _ in range(1000):
            MarkovModel.subfit(self)
            self.main_dict[self.p] = self.dict_of_dict
            MarkovModel.choice_next_letter(self)

        # печатаем весь сгенерированный текст
        print(self.generated_text)
        # печатаем словарь словарей
        print(self.main_dict)
