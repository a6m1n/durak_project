import random
def calc(num): #Калькулятор очков.
    result = 0
    if num[0] == 6 or num[0] == '6':
        result +=1
        if num[1]==Kozhurnaya_mast:
            result+=10
    elif num[0] == 7 or num[0] == '7':
        result +=2
        if num[1]==Kozhurnaya_mast:
            result+=10
    elif num[0] == 8 or num[0] == '8':
        result +=3
        if num[1]==Kozhurnaya_mast:
            result+=10
    elif num[0] == 9 or num[0] == '9':
        result +=4
        if num[1]==Kozhurnaya_mast:
            result+=10
    elif num[0] == 10 or num[0] == '10':
        result +=5
        if num[1]==Kozhurnaya_mast:
            result+=10
    elif num[0] == 'J':
        result +=6
        if num[1]==Kozhurnaya_mast:
            result+=10
    elif   num[0] == 'Q':
        result +=7
        if num[1]==Kozhurnaya_mast:
            result+=10
    elif  num[0] == 'K':
        result +=8
        if num[1]==Kozhurnaya_mast:
            result+=10
    elif  num[0] == 'A':
        result +=9
        if num[1]==Kozhurnaya_mast:
            result+=10

    return result


def give_deck_card(card, masti): # а эта просто даёт колоду карт
    deck = []
    for i in card:
        for j in masti:
            a=i+' '+j
            deck.append(a)
    return deck

def give_user_card(all_gamers,deck_main): #эта функция нужна чтоб не было повторок. их сюда выкидует
    last_card = []
    # global all_gamers,deck_main,last_card
    for i in range(all_gamers):
        while len(gamers[i])<6:
            a=random.choice(deck_main)
            if a in last_card:
                pass
            else:
                gamers[i].append(a)
            last_card.append(a)
    return last_card

def card_gamers(gamer): #функция демонстрирует карты всех игроков.
    counter = 0
    for h in range(len(gamers)):
        for i in range(len(gamers[h])):
            for j in range(i + 1, len(gamers[h])):
                if gamers[h][i] == gamers[h][j]:
                    counter += 1
    print ('______________________________kard_gamers________________________________________')
    for d in range(len(gamers)):
        print (', '.join(gamers[d]), '. Gamer nomer {}'.format(d+1))
    print ('______________________________kard_gamers________________________________________')


def gamer_strong_card(gamers): #функция считает очки всех игроков
    gamer_point = {}
    point = 0
    krug = 0
    for i in range(len(gamers)):
        point = 0
        krug +=1
        for j in gamers[i]:
            mas_card=j.split()
            point +=calc(mas_card)
        gamer_point['Gamer ' +str(i)]=point
    return gamer_point

def max_gamer_point(gamer_point): #функция вычисляет игрока у которого лучие карты по очкам.
    max = gamer_point['Gamer 0']
    name_max = 1
    for i in gamer_point:
        n=int(gamer_point[i])
        if n>max:
            max=n
            name_max=int(i.split()[1])
    print ('Best card have gamer num {} point this card {}'.format(name_max+1, max))




try:
    all_gamers = input('All gamer who play: ')
    if type(all_gamers) is float:
        print ('Input pls only type integer, not float. ')
        all_gamers=0
    try:
        all_gamers=int(all_gamers)
    except ValueError:
        all_gamers=0
        print ('Input pls only int')

    if all_gamers<=6 and all_gamers != 1 and all_gamers !=0 :

        gamers= [ [] for i in range(all_gamers)] #показует кол-во игроков в списке
        card = ["6", "7", "8", "9", "10", "J", "Q", "K", "A" ] #список карт
        masti = ['kresta', 'picka','byba','cehvy'] #масти
        Kozhurnaya_mast=random.choice(masti)
        print ('Kozhurnaya mast` = '+Kozhurnaya_mast)


        # if __name__=='__main__':
        deck_main=give_deck_card(card, masti) #deck_main = колода карт
        last_card= give_user_card(all_gamers,deck_main)
        card_gamers(gamers)
        gamer_point =gamer_strong_card(gamers)
        max_gamer_point(gamer_point)

    elif all_gamers ==1:
        print ('One gamers ne mozhet igrat. Error')
    elif all_gamers == 0:
        print ('Zero gamers ne mozhet igrat. Error')
    elif all_gamers >=7:
        print ('Range max. input num<6')

except TypeError:
    print ('Error.Report pls.')
