import random
print("hello world")
# This is a comment
# var
x = 1
y = 2
z = x + y
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
    print ("this is",card)
for i in array:
    if i == 0:
        conter += 11
    elif i >= 9:
        conter += 10    
    else: conter += i + 1
    print("this is conter in for",conter)
ns = 0    
while conter <= 17:
    ns += 1
    print("this is conter in while",conter)
    rando = random.randint(0, 12)
    dealerDeck.append(carts[rando])
    if rando == 0:
        conter += 11
    elif rando >= 9:
        conter += 10    
    else: conter += rando + 1
print("this is ns",ns)    
print("this is conter",conter)    
print("dealerDeck", dealerDeck)    

