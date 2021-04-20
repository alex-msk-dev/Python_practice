#  Импортируем функцию для генерации случайных целых чисел
from random import randint


#  Класс карта
class Card(object):
    #  Коды мастей
    SPADE = 1
    HEARTS = 2
    CLOVER = 3
    DIAMOND = 4

    #  Символы мастей (для красивого вывода)
    SUITS = ['♠', '♥', '♣', '♦']
    #  Значения карт
    VALUES = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    #  Конструктор: принимает два параметра - масть и значение карты
    def __init__(self, suit, value):
        #  Устанавливает полученные значения
        self.suit = suit
        self.value = value

    #  Представляет карту в виде строки
    def __str__(self):
        #  Соединяем масть и значение
        return self.VALUES[self.value - 6] + self.SUITS[self.suit - 1]

    #  Создаёт строку, по которой можно воспроизвести карту
    def __repr__(self):
        return f'Card({self.suit}, {self.value})'

    #  Проверяет меньше ли текущая карта переданной
    #  (сравниваются только значения)
    def __lt__(self, other):
        return self.value < other.value

    #  Проверяет равны ли две карты
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


#  Класс колода карт
class CardDeck(object):
    #  Конструктор: принимает либо список карт, либо ничего
    def __init__(self, cards = None):
        #  Если ничего не было передано, то генерируется новая колода из 36 карт
        if cards is None:
            self._cards = self._get_full_deck()
        #  Иначе колодой становится текущий список
        else:
            self._cards = cards

    #   Представление колоды в виде строки
    def __str__(self):
        #  Соединяем карты через пробел в одну строку
        return ' '.join(str(card) for card in self._cards)

    #  Перемешивает карты в колоде
    def shuffle(self):
        #  Идея следующая: будем генеривровать два случайных номера карт
        #  и менять их местами
        #  Проделываем данную операцию в кол-ве - кол-во карт в квадрате
        for _ in range(len(self._cards) ** 2):
            #  Генерируем два номера
            l = randint(0, len(self._cards) - 1)
            r = randint(0, len(self._cards) - 1)
            #  Меняем карты местами
            self._cards[l], self._cards[r] = self._cards[r], self._cards[l]

    #  Удаляет карту с конца списка карт (считаем это началом колоды)
    def pick_first(self):
        return self._cards.pop()
    
    #  Возвращает случайную карту из колоды
    def get_random_card(self):
        #  Если колода пуста
        if len(self._cards) == 0:
            return None
        #  Иначе возвращаем рандомную карту
        return self._cards[randint(0, len(self._cards) - 1)]

    #  Создаёт новую полную (из 36 карт) колоду карт
    def _get_full_deck(self):
        #  Создаём пустой список
        cards = []
        #  Для каждой масти
        for suit in range(1, 5):
            #  Для каждого значения
            for value in range(6, 15):
                #  Создаём и добавляем карту в список карт
                cards.append(Card(suit, value))
        #  Возвращаем полученный список
        return cards


#  Раздаёт 6 карт игроку: возвращает колоду из 6 карт
def get_player_deck(card_deck):
    #  Раздаём 6 карт: формируем из них список
    cards = [card_deck.pick_first() for _ in range(6)]
    #  Формируем из списка колоду карт
    return CardDeck(cards)


#  Выводит колоды карт игроков
def print_players(players):
    #  Для каждого игрока
    for i, player in enumerate(players, 1):
        #  Выводим его номер и колоду карт
        print(f'player {i}:', player)


#  Возвращает козырь
def get_trump(card_deck):
    #  Козырь получаем по случайной карте из колоды
    card = card_deck.get_random_card()
    #  Если карт в колоде не осталось, то козырь генерируется рандомно
    if card is None:
        return randint(1, 4)
    #  Иначе возвращаем масть случайной карты из колоды
    else:
        return card.suit


#  Выбирает игрока, который будет ходить первым
def get_first_player(players, trump):
    #  Мы ищем номер игрока, у которого козырь с минимальным значением
    min_value = 16
    res_num = 1
    #  Для каждого игрока
    for i, player in enumerate(players, 1):
        #  Мы перебираем его карты
        for card in player._cards:
            #  Если карта козырная и значение меньше минимального
            if card.suit == trump and card.value < min_value:
                #  то одновляем минимальное значение и запоминаем номер игрока
                min_value = card.value
                res_num = i
    #  Возвращаем номер игрока
    #  (Если не у кого не будет козыря, то первый игрок ходит первым)
    return res_num


#  Функция, с которой начинается игра
def main():
    #  Создаём колоду карт (полную)
    #  И перемешиваем колоду
    full_deck = CardDeck()
    full_deck.shuffle()

    #  Вводим количество игроков
    #  И создаём список игроков, каждый из которых получает по 6 карт
    num_players = int(input('Enter num players: '))
    print()
    players = [get_player_deck(full_deck) for i in range(num_players)]

    #  Выводим колоды карт игроков
    print_players(players)

    #  Получаем козырь и выводим его
    trump = get_trump(full_deck)
    print()
    print(f'Trump is {Card.SUITS[trump - 1]}')

    #  Получаем номер игрока, чеё ход первый и выводим его номер
    first_player = get_first_player(players, trump)
    print()
    print(f'Player with first move: {first_player}')


#  Начинаем игру
main()
