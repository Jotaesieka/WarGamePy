colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
allCards=[]
for c in colors:
    for f in figures:
        aCard=f.copy()
        aCard['Color']=c
        allCards.append(aCard)
import random
random.shuffle(allCards)
##print(allCards)
player1=[]
player2=[]
player1=allCards[:12]
player2=allCards[12:]
print('Karty pierwszego-------------------')
print(len(player1))
print('Karty drugiego--------------------')
print(len(player2))
while len(player1)>0 and len(player2)>0:
    card1=player1.pop(0)
    card2=player2.pop(0)
    stock=[]
    if card1["Power"] == card2["Power"]:
        while card1['Power']==card2['Power']:
            print('NO TO MAMY WOJNĘ!',card1,' VS ',card2)
            stock.append(card1)
            stock.append(card2)
            if len(player1)<2:
                player2.extend(stock)
                player2.extend(player1)
                player1=[]
                break
            elif len(player2)<2:
                player1.extend(stock)
                player1.extend(player2)
                player2=[]
                break
            else:
                card1=player1.pop(0)
                card2=player2.pop(0)
                stock.append(card1)
                stock.append(card2)
                card1=player1.pop(0)
                card2=player2.pop(0)
        else:
            if card1['Power']>card2['Power']:
                player1.append(card1)
                player1.append(card2)
                player1.extend(stock)
            else:
                player2.append(card2)
                player2.append(card1)
                player2.extend(stock)
    
    elif card1['Power']>card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print('Gracz 1 ma:',card1,'\nGracz 2 ma: ',card2,'\n WYGRYWA GRACZ 1 i ma teraz',len(player1),'KART')
    else:
        player2.append(card2)
        player2.append(card1)
        print('Gracz 1 ma:',card1,'\nGracz 2 ma: ',card2,'\n WYGRYWA GRACZ 2 i ma teraz',len(player2),'KART')
if len(player1)<len(player2):
    print("!!!!!!!!!! WYGRAŁ GRACZ 2 !!!!!!!!!!!!!!!!!!")
else:
    print("!!!!!!!!!! WYGRAŁ GRACZ 1 !!!!!!!!!!!!!!!!!!")
