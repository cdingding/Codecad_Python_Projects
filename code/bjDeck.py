import random

class Card(object):
    value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                  'K': 13, 'A': 14}

    def __init__(self, number, suit):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return "%s%s" % (self.number, self.suit)

    def __cmp__(self, other): # count and compare, return bust or not, and sum
        return cmp(self.value_dict[self.number], self.value_dict[other.number])

class Deck(object):
    def __init__(self):
        self.cards = []
        for num in Card.value_dict.keys():
            for suit in 'cdhs':
                self.cards.append(Card(num, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self): #2cards first
        if not self.isempty():
            return self.cards.pop()

    def hands(self, deal_cards, player_cards):
        pass


    def add_cards(self, cards): #add ???
        self.cards.extend(cards)

    #def __len__(self):
        #return len(self.cards)

    #def isempty(self):
        #return self.cards == []


class War(object):
    def __init__(self, human=True):
        self.human = human
        self.player1 = self.create_player("Player 1")
        self.dealer = self.create_player("Dealer")
        self.winner = None
        self.loser = None
        self.pot = []
        self.deal()

    def create_player(self, title):
        if self.human:
            name = raw_input("Enter %s's name: " % title)
        else:
            name = title
        return Player(name)

    def deal(self): #two only first
        deck = Deck()
        deck.shuffle()
        while not deck.isempty():
            self.player1.receive_card(deck.draw_card())
            self.player2.receive_card(deck.draw_card())

    def play_game(self):
        while self.winner is None:
            self.play_round()
        self.display_winner()

    def draw_card(self, player, other_player): #???
        card = player.play_card()
        if not card:
            self.winner = other_player.name
            self.loser = player.name
            return
        self.pot.append(card)
        return card

    def draw_cards(self, player, other_player, n): #??? maybe fore count
        cards = []
        n = min(n, len(player.hand), len(other_player.hand))
        for i in xrange(n):
            card = self.draw_card(player, other_player)
            if not card:
                return
            cards.append(card)
        return cards

    def war(self): #define deal more cards, hit or give one more, check player bust condition
        cards1 = self.draw_cards(self.player1, self.player2, 3)
        cards2 = self.draw_cards(self.player2, self.player1, 3)
        self.display_war(cards1, cards2)

    def play_round(self): #black jack main body, call funciton or instances.
        self.pause()
        card1 = self.draw_card(self.player1, self.player2)
        card2 = self.draw_card(self.player2, self.player1)
        self.display_play(card1, card2)
        if not card1 or not card2:
            return
        if card1 == card2:
            self.war()
            self.play_round()
        elif card1 > card2:
            self.give_cards(self.player1)
        else:
            self.give_cards(self.player2)

    def give_cards(self, player): # with this may not need add cards
        player.receive_cards(self.pot)
        self.display_receive(player)
        self.pot = []

    def pause(self):
        if self.human:
            raw_input("")

    def cards_to_str(self, cards): #need it
        return " ".join(str(card) for card in cards)

    def display_play(self, card1, card2): #display for monitoring
        if self.human:
            print "%s plays %s" % (self.player1.name, str(card1))
            print "%s plays %s" % (self.player2.name, str(card2))

    def display_receive(self, player):
        if self.human:
            self.pot.sort(reverse=True)
            pot_str = self.cards_to_str(self.pot)
            print "%s receives the cards: %s" % (player.name, pot_str)

    def display_war(self, cards1, cards2):
        if self.human:
            print "WAR!"
            print "%s plays %s" % (self.player1.name, self.cards_to_str(cards1))
            print "%s plays %s" % (self.player2.name, self.cards_to_str(cards2))

    def display_cards(self): # added additionally
        print "%s has %s cards and %s has %s cards." \
              %(self.player1.name, self.cards_to_str(cards1), self.player2.name, self.cards_to_str(cards2))

    def display_winner(self):
        if self.human:
            print "The winner is %s!!!" % self.winner


if __name__ == '__main__':
    game = War()
    game.play_game()
    game.display_cards()


import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        #self.discard = []

    #def receive_card(self, card):
        #self.discard.append(card)

    #def receive_cards(self, cards):
        #self.discard.extend(cards)

    '''def play_card(self):
        if not self.hand:
            random.shuffle(self.discard)
            self.hand = self.discard
            self.discard = []
        if not self.hand:
            return None
        card = self.hand.pop()
        return card'''

    def __repr__(self):
        return self.name

    def __len__(self): #//take sum of the cards
        return len(self.hand) + len(self.discard)