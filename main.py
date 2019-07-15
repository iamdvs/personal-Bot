import telebot
import re


TOKEN = '875389738:AAEhNaYI3NVZ-Q1pFVFa8VrkunUdtjZK71w'
bot=telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,'''you can speak with me here  
     about /aboutme''')

f=open('about.txt','r')
about_file=f.read()

with open('about.txt','r') as fileaboute:
    about_file=fileaboute.read()
    @bot.message_handler(commands=['aboutme'])
    def send_about_data(message):
        bot.reply_to(message,about_file)
        
    fileaboute.close()



#ith open('new.jpg','rb') as image:
 #  rimage=image.read()
    
  # @bot.message_handler(commands=['img'])
   #def image_reader(message):
    #   cid=message.chat.id
     #  bot.send_photo(cid,rimage)    
   #image.close()
    
    

@bot.message_handler(regexp=r"@.........\s*")
def admin_to_user(message):
    cid=message.chat.id
    try:
        msg=message.text
        to_cid=re.findall(r".(.........)",msg)
        to_msg=re.findall(r"@.........\s(.*)",msg)
        cid_to=to_cid[0]
        msg_to=to_msg[0]
        bot.send_message(cid_to,msg_to)
        
        if(to_cid):
            print("mached")
    except:
        bot.send_message(cid,"user Not found please Enter valid chat id ❌")

    

bot.polling()
