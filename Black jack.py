from random import *
while True:
    spam1= randint(1, 11)
    spam2= randint(1, 11)
    spam3= randint(1, 11)

    if (spam1+spam2 == 21):
        print (spam1, spam2, ' Black Jack')

    elif (spam1+spam2 > 21):
        print (spam1, spam2, ' Bust')

    elif (spam1+ spam2 <=20):
        print (spam1, spam2, ' (h)it/ (s)tand')
        user= input()
        if (user== 'h'):
            if (spam1+spam2+spam3 > 21):
                print (spam1, spam2, spam3, ' Bust')

            elif (spam1+spam2+spam3 == 21):
                print (spam1, spam2, spam3, ' Black Jack')

            elif (spam1+ spam2+ spam3 <= 20):
                print (spam1, spam2, spam3)

        elif (user== 's'):
            print(spam1, spam2)

#DEALER
    deal1= randint(1, 11)
    deal2= randint(1, 11)
    deal3= randint(1, 11)
    print ('DEALER\'s HAND', end=' ')
    if (deal1+deal2 == 21):
        print (deal1, deal2, ' Black Jack')
        print ('YOU WIN')

    elif (deal1+deal2 > 21):
        print (deal1, deal2, ' Bust')
        print ('YOU WIN')

    elif (deal1+ deal2 <=20):
        if (deal1+ deal2+ deal3 <= spam1+ spam2 + spam3):
            print (deal1, deal2, deal3, 'YOU WIN')
        else:
            print (deal1, deal2, deal3, 'YOU LOSE')

    print ('')

