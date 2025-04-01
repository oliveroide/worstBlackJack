import random
import sys
#blackjack
carts = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
yourDeck = []
dealerDeck = []
conter = 0
#deler get 2 cards
array = []
for i in range(2):
    card = random.randint(0, 12)
    dealerDeck.append(carts[card])
    array.append(card)
for i in array:
    if i == 0:
        conter += 11
    elif i >= 9:
        conter += 10    
    else: conter += i + 1
while conter < 17:
    
    rando = random.randint(0, 12)
    dealerDeck.append(carts[rando])
    if rando == 0:
        conter += 11
    elif rando >= 9:
        conter += 10    
    else: conter += rando + 1   
    if conter > 21:
        for i in array:
            if i == 'A':
                conter -= 10
                break
print("dealerDeck", dealerDeck[0:1])
#prueba conter dealer
#print("this is dealer conter",conter) 
dealerconter = conter
array = []
conter = 0 
#player get 2 cards
for i in range(2):
    card = random.randint(0, 12)
    yourDeck.append(carts[card])
    array.append(card)   
for i in array:
    if i == 0:
        conter += 11
    elif i >= 9:
        conter += 10    
    else: conter += i + 1 
if conter == 21:
    print("blackjack you win")    
print("yourDeck", yourDeck)
print("this is conter in for you",conter)   
you = input("get a card Y, not get a card N ")
while you == 'Y':
    rando = random.randint(0, 12)
    yourDeck.append(carts[rando])
    if rando == 0:
        conter += 11
    elif rando >= 9:
        conter += 10    
    else: conter += rando + 1
    print("this is conter in new card",conter)
    print("yourDeck", yourDeck)    
    if conter > 21:
        break
    you = input("get a card Y, not get a card N ")    
print("this is dealerconter",dealerconter)     
##
if conter > 21:
    print("you lost")
elif conter == dealerconter:
    print("draw")
elif dealerconter > 21:
    print("dealerDeck", dealerDeck)
    print("this is dealer conter",conter)
    print("dealer lose")
    exit()    
if dealerconter > conter:
    print("dealer win")
elif dealerconter < conter:
    print("you win")        


