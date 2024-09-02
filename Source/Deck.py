import os
import random
import pygame
from Card import Card, CardWidth, CardHeight

image_file_list = [
    "001_seeding.png",
    "002_sapling.png",
    "003_flower.png",
    "004_bush.png",
    "005_tree.png",
    "006_compost.png",
    "007_broom.png",
    "008_vacuum.png",
    "009_leafblower.png",
    "010_bunny.png",
    "011_rabbit.png",
    "012_puppy.png",
    "013_dog.png",
    "014_kitten.png",
    "015_cat.png",
    "016_shower.png",
    "017_blackout.png",
    "018_drought.png",
    "019_plug.png",
    "020_window.png",
    "021_door.png",
    "022_cabinet.png",
    "023_spill.png",
    "024_safe.png",
    "025_pantry.png",
]

class Deck:
    def __init__(self):
        self._card_size = (CardWidth, CardHeight)
        self._card_images = {} # card image buffer
        self._raw_cards = [] # raw cards from the images
        self._cards = [] # cards for a deck

    def load_cards(self, num_cards):
        # back image
        image_file = os.path.join('resources', 'card_back.png')
        self._back_image = pygame.image.load(image_file)
        self._card_images["backside"] = pygame.transform.scale(
                self._back_image, self._card_size)

        # front images
        for file in image_file_list:
            image_file = os.path.join('resources', 'card_drafts', '{}'.format(file))
            image = pygame.image.load(image_file)
            self._card_images[image_file] = pygame.transform.scale(image, self._card_size)
            self._raw_cards.append(Card(image_file, self._card_size, "", "", 1))

        # create a deck from the raw cards
        for i in range(num_cards):
            index = random.randint(0, len(self._raw_cards) - 1)
            card = self._raw_cards[index]
            self._cards.append(card)

        # shuffle the deck
        random.shuffle(self._cards)
