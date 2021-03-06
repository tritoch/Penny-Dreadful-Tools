from decksite.view import View

# pylint: disable=no-self-use
class Card(View):
    def __init__(self, card):
        self.card = card
        self.cards = [card]
        self.decks = card.decks

    def __getattr__(self, attr):
        return getattr(self.card, attr)

    def subtitle(self):
        return self.card.name
