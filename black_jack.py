import random


class Card:
    def __init__(self, rank: str, suite: str) -> None:
        self.rank = str(rank)
        self.suite = suite

    def index(self) -> str:
        return f'{self.rank}{self.suite}'

    def get_value(self, points: int) -> int:
        if self.rank in 'ВДК' or self.rank == '10':
            return 10

        if points < 11:
            if self.rank == 'А':
                return 11
            else:
                return '  23456789'.index(self.rank)
        else:
            return ' А23456789'.index(self.rank)


class CardDeck:
    def __init__(self) -> None:
        suite = ['Ч', 'Б', 'П', 'К']
        rank = ['А', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'В', 'Д', 'К']
        self.cards = [Card(r, s) for s in suite for r in rank]
        random.shuffle(self.cards)

    def get_card(self) -> Card:
        return self.cards.pop()


class Player:
    def __init__(self, name: str) -> None:
        self.points = 0
        self.cards = []
        self.name = name

    def one_more_card(self, deck) -> None:
        card = CardDeck.get_card(deck)
        self.points += card.get_value(self.points)
        self.cards.append(card.index())

    def turn_summary(self) -> str:
        return f'Карты {self.name}: {self.cards}, Очки: {self.points}'


class Dealer(Player):
    def myself(self, deck) -> None:
        while self.points < 18:
            self.one_more_card(deck)

    def table_result(self, player) -> None:
        print(self.turn_summary())
        print(player.turn_summary())


class Game:
    while True:
        deck = CardDeck()
        dealer = Dealer('Dealer')
        player = Player('Player')
        player.one_more_card(deck)
        player.one_more_card(deck)
        dealer.one_more_card(deck)
        dealer.one_more_card(deck)

        while player.points < 21:
            print(player.turn_summary())
            more_card = input('Еще карту? \n y/n:').lower()
            if more_card == 'y':
                player.one_more_card(deck)
            elif more_card == 'n':
                dealer.myself(deck)
                break
            else:
                print('Введите корректный ответ')
                continue

        if player.points > 21:
            dealer.table_result(player)
            print('Вы проиграли')
        elif dealer.points > 21:
            dealer.table_result(player)
            print('Вы победили')
        elif player.points == 21 and dealer.points < 21:
            dealer.table_result(player)
            print('Вы победили')
        elif player.points == 21 and dealer.points == 21:
            dealer.table_result(player)
            print('Ничья')
        elif player.points > dealer.points:
            dealer.table_result(player)
            print('Вы победили')
        else:
            dealer.table_result(player)
            print('Вы проиграли')

        next_game = input('Еще партию? \n \n \n \n y/n:')
        if next_game == 'y':
            continue
        elif next_game == 'n':
            break


def main():
    game = Game()


if __name__ == '__main__':
    main()

