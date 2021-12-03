import random
import datetime
from os import error
import telebot
import qrcode
from gtts import gTTS
from khayyam import JalaliDatetime

# @AjQ1_bot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def wellcome(message):
    bot.reply_to(message, "Wellcome " + message.from_user.first_name)

number=0
markup=''
@bot.message_handler(commands=['game'])
def game(message):
    global number
    number = random.randint(0, 10)
    user_input = bot.send_message(message.chat.id, 'Random number choosed between 0-10. Now you can guess number : ')
    bot.register_next_step_handler(user_input, gameplay)

def gameplay(user_input):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn = telebot.types.KeyboardButton('New Game')
    markup.add(itembtn)
    global number
    if user_input.text == 'New Game':
        number = random.randint(0, 10)
        user_input=bot.send_message(user_input.chat.id, 'New game started. Now you can guess number : ',reply_markup=markup)
        bot.register_next_step_handler(user_input, gameplay)

    elif int(user_input.text) == number:
        user_input = bot.send_message(user_input.chat.id, 'Congradulation! you guessed it right🏆',reply_markup=markup)
        
    elif int(user_input.text) > number:
        txt = bot.send_message(user_input.chat.id, 'Guess smaller number ⬇️',reply_markup=markup)
        bot.register_next_step_handler(user_input,gameplay)
        
    elif int(user_input.text) < number:
        user_input = bot.send_message(user_input.chat.id, 'Guess bigger number⬆️',reply_markup=markup)
        bot.register_next_step_handler(user_input,gameplay)
        
@bot.message_handler(commands=['age'])
def age(message):
    date = bot.send_message(message.chat.id, 'Enter your date of birth in shamsi like 1378/10/19')
    bot.register_next_step_handler(date,age_calculator)

def age_calculator(message):
    try:
        dob = message.text.split("/")
        subs=str(JalaliDatetime.now() - JalaliDatetime(dob[0],dob[1],dob[2]))
        subs=subs.split(' ')
        years=int(subs[0])//365
        days=int(subs[0])%365
        bot.send_message(message.chat.id,str(years)+' Years '+str(days)+'Days \n')
    except:
        age = bot.send_message(message.chat.id,'Enter your date of birth like sample.')
        bot.register_next_step_handler(dob,age_calculator)

@bot.message_handler(commands=['voice'])
def voice_generator(message):
    text=bot.send_message(message.chat.id,'Enter text in english like : welcome to my bot')
    bot.register_next_step_handler(text,text2voice)

def text2voice(message):
    try:
        language='en'
        vo=gTTS(text=message.text, lang=language, slow=False)
        vo.save("vo.mp3")
        voice=open('vo.mp3', 'rb')
        bot.send_voice(message.chat.id, voice)
    except:
        text = bot.send_message(message.chat.id,'Enter text like sample')
        bot.register_next_step_handler(text,text2voice)

@bot.message_handler(commands=['max'])
def max_number(message):
    array=bot.send_message(message.chat.id, 'Enter numbers like 1,2,4,8')
    bot.register_next_step_handler(array,find_max)

def find_max(message):
    try:
        array=list(map(int, message.text.split(',')))
        max_number=max(array)
        bot.send_message(message.chat.id, 'Max number : ' + str(max_number) )
    except:
        array = bot.send_message(message.chat.id,'Enter numbers like sample')
        bot.register_next_step_handler(array,max_number)     

@bot.message_handler(commands=['argmax'])
def argmax(message):
    array=bot.send_message(message.chat.id, 'Enter numbers like 1,2,4,8')
    bot.register_next_step_handler(array,find_argmax)

def find_argmax(message):
        try:
            array=list(map(int, message.text.split(',')))
            max_arg=array.index(max(array))
            bot.send_message(message.chat.id, 'Argument of maximum number is : ' + str(max_arg))
        except:
            array=bot.send_message(message.chat.id,'Enter numbers like sample')
            bot.register_next_step_handler(array,argmax)       

@bot.message_handler(commands=['qrcode'])
def qrCode(message):
    text=bot.send_message(message.chat.id, 'Enter your text')
    bot.register_next_step_handler(text,qrcode_generator)
def qrcode_generator(message):
    qr_pic=qrcode.make(message.text)
    qr_pic.save('QrCode.png')
    qr=open('QrCode.png','rb')
    bot.send_photo(message.chat.id,qr)
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"""
/start : 
Welcome to ArianBot 
/game :  
Number Prediction Game🎮
/age : 
Calculate age from day of birth(shamsi) 📅
/voice : 
Convert english text to voice🎵
/max : 
Find max number 
/argmax : 
Find argumet of max number
/qrcode : 
convert text to QR code  
/help : 
Show menu 
    """ )
              
bot.infinity_polling()
