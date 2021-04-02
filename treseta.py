from random import shuffle,randint
import random

class Card:
    
    colors = {"Kupe": 0, "Špade": 1, "Bastoni": 2, "Dinari": 3}
    numbers = [
    "cetvorka",
    "petica",
    "sestica",
    "sedmica",
    "fanat",
    "kaval",
    "kralj",
    "As",
    "duja",
    "trica"]
    
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


    def __str__(self):
        return "{} of {} ".format(str(self.number), self.suit)
   
class Cards:
    
    def __init__(self, cards):
        self._cards = cards
    
    def __str__(self):
        return '{' + ', '.join(str(c) for c in self._cards) + '}'

    def add(self, card):
        self._cards.append(card)

    def count(self):
        return len(self._cards)

    def remove(self, card):
        for c in self._cards:
            if str(c) == str(card):
                self._cards.remove(c)
                return

class Deck(Cards):
    
    def __init__(self):
        cards = [ Card(n, s) for n in Card.numbers for s in Card.colors ]
        super().__init__(cards)

    def shuffle(self):
        random.shuffle(self._cards)


    def deal(self,N):
        hand, self._cards = self._cards[:N], self._cards[N:]
        return Cards(hand)

class Treseta():
    igracPts=0
    kompPts=0

    def __init__(self):
        self.deck=Deck()

    def game(self):
        igracKarta=0
        kompKarta=0
        self.deck.shuffle()
        self.igracPotez=self.deck.deal(4)
        self.kompPotez=self.deck.deal(4)
        name1 = input("Dobrodosli, unesite svoje ime: ")
        while(self.deck.count()!=0):
            print("{} karte: " .format(name1) + str(self.igracPotez))
            print("Komp karte: " + str(self.kompPotez))
            print("\nunesite koju kartu zelite odigrati:")
            br = 0
            for i in self.igracPotez._cards:
                print("{} {}" .format(br,i))
                br += 1

            odabirKarte=int(input(":"))
            igracKarta = self.igracPotez._cards[odabirKarte]
            print("odabrali ste: ", igracKarta)
            cardColor=Cards([card for card in self.kompPotez._cards if card.suit == igracKarta.suit ])
            
            if len(cardColor._cards) > 0:
                kompKarta = cardColor._cards[randint(0, len(cardColor._cards) - 1)]
                print("komp bira: ", kompKarta)
                if igracKarta.suit==kompKarta.suit:
                    if(igracKarta.number > kompKarta.number):
                        self.igracPts += 1
                    else:
                        self.kompPts += 1

            else:
                kompKarta = self.kompPotez._cards[randint(0, len(self.kompPotez._cards) - 1)]
                print("komp bira: ", kompKarta) 
                self.igracPts += 1


            self.igracPotez._cards.remove(igracKarta)
            self.kompPotez._cards.remove(kompKarta)

            self.igracPotez=Cards(self.igracPotez._cards + self.deck.deal(1)._cards)

            self.kompPotez=Cards(self.kompPotez._cards + self.deck.deal(1)._cards)

            if self.igracPts > self.kompPts:
                print("stanje: {} : {} \n" .format(self.igracPts,self.kompPts))
            else: 
                print("stanje: {} : {} \n" .format(self.igracPts,self.kompPts))
        


treseta=Treseta()
treseta.game()



