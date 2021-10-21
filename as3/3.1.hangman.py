from random import choice
words=['seriea','acmilan','juventus','intermilan','asroma','lazio','napoli','atalanta']
sel_word=choice(words)
user_true_char=[]
chance=7
while chance>0:
    print('Chances : ',chance)
    for i in range(0,len(sel_word)):
        if sel_word[i] in user_true_char:
            print(sel_word[i],end=' ')
        else:
            print('-',end=' ')
    user_char=input('\nEnte a Character : ')
    if user_char in sel_word:
        user_true_char.append(user_char)
        print('✅')
    else :
        chance-=1
        print('❌')
    if len(user_true_char)==len(sel_word):
        print('Congradulation You Win')
        break
if chance<=0:
    print('Sorry You Lose','\nAnswer is :',sel_word)
    
    