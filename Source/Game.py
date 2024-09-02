import pygame
from Deck import Deck
from Hand import Hand

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
blue = (50, 50, 190)
red = (190, 50, 50)
grey = (100, 100, 100)

FPS = 10

class Game:
    def __init__(self, num_hands):
        pygame.display.set_caption('Household')
        self._clock = pygame.time.Clock()

        self._num_hands = num_hands
        self._dimensions = (1200, 800)
        self._display = pygame.display.set_mode(self._dimensions)
        self._display.fill(grey)
        self._deck = Deck()
        self._deck.load_cards(num_hands * 30)
        self._hands = []
        self.initialize_hands(num_hands)
        self._current_hand = 0

    def initialize_hands(self, num_hands):
        # create hands
        self._num_hands = num_hands
        for i in range(num_hands):
            hand = Hand(i, self._deck, self._display)
            self._hands.append(hand)

        # deal cards to hands
        for i, card in enumerate(self._deck._cards):
            hand = self._hands[i % self._num_hands]
            hand.deal_card(card)

    def start(self):
        self.run_hand(0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                self.handle_event(event)

            pygame.display.update()
            self._clock.tick(FPS)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                self.run_hand()

    def run_hand(self, id=-1):
        if id >= 0:
            self._current_hand = id
        else:
            self._current_hand = (self._current_hand + 1) % self._num_hands

        self._hands[self._current_hand].run()
