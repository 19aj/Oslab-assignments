import os

WORDS=[]

def load_data():
    if os.path.exists("wordss_bank.txt"):
        with open ('words_bank.txt') as f:
            big_text=f.read()
            lines=big_text.split('\n')
            for i in range(0,len(lines),2):
                my_dict={'english':lines[i],'persian':lines[i+1]}
                WORDS.append(my_dict)  
    else :
        print('File Not Exists!')
        exit()
        

def eng2far():
    output_text=''
    user_text=input('Wrie Your Text In English : ')
    user_sentences=user_text.split('.')
    for sentence in user_sentences:
        user_words=sentence.split(' ')
        for user_word in user_words:
            for word in WORDS:
                if user_word==word['english']:
                    output_text+=word['persian']+' '
                    break
            else:
                output_text+=user_word+' '
        output_text+='.'
    
    print('Translated Text : \n',output_text)
    

def far2eng():
    output_text=''
    user_text=input('Wrie Your Text In Persian : ')
    user_sentences=user_text.split('.')
    for sentence in user_sentences:
        user_words=sentence.split(' ')
        for user_word in user_words:
            for word in WORDS:
                if user_word==word['persian']:
                    output_text+=word['english']+' '
                    break
            else:
                output_text+=user_word+' '
        output_text+='.'
    
    print('Translated Text : \n',output_text)


def add_word():
    print('--- Add New Word ---')
    e_word=input('Word In English : ')
    for word in WORDS:
        if e_word==word['english']:
            print('Word Already Exists!')
            break
    else:
        p_word=input('Word In English : ')
        WORDS.append({'english':e_word,'persian':p_word})
        with open ('words_bank.txt','a') as fa:
            fa.write('\n'+e_word+'\n'+p_word)
        print('Word Added.')




load_data()

while True:
    choice=int(input('1. Add New Word\n2. Translation English2Persian\n3. Translation Persian2English\n4. Exit\nCHOICE : '))
    if choice==1:
        add_word()
    elif choice==2:
        eng2far()
    elif choice==3:
        far2eng()
    elif choice==4:
        print('Good Luck!')
        break
    else :
        print('Choose Between 1 and 4')
        