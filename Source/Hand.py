import pygame
from Deck import Deck
from Card import Card, CardWidth, CardHeight

class Hand:
    def __init__(self, id, deck, display):
        self._id = id
        self._active = False
        self._pile = []
        self._dead_pile = []
        self._cards = []
        self._deck = deck
        self._display = display
        self._pile_offset = [0, id * CardHeight]
        self._card_offset = [CardWidth, id * CardHeight]

    def deal_card(self, card):
        self._pile.append(card)

    def update_display(self):
        # display pile
        if len(self._pile) > 0:
            img = self._deck._card_images["backside"]
            self._display.blit(img, self._pile_offset)

        # display cards
        for i, card in enumerate(self._cards):
            img = self._deck._card_images[card.image]
            card._position[0] = self._card_offset[0] + i * 100
            card._position[1] = self._card_offset[1]
            # print("card {}".format(card._position))
            self._display.blit(img, [card.x, card.y])

    def run(self):
        """ Run a hand.
        """
        print("run_hand {}".format(self._id))

        cards_in_hand = 5

        # play a card and put back to pile
        while (len(self._cards) >= cards_in_hand):
            card = self._cards[0]
            del(self._cards[0])
            self._pile.insert(0, card)

        # deal cards in hand
        while len(self._cards) < cards_in_hand:
            # deal a card from pile
            if len(self._pile) > 0:
                card = self._pile[-1]
                del(self._pile[-1])
                card._face_up = True
                self._cards.append(card)
            else:
                break

        print("cards = {}, {}".format(len(self._pile), len(self._cards)))
        self.update_display()
