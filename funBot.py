import requests
import json


TOKEN = 'bot token :)'

URL = 'https://api.telegram.org/bot'+TOKEN+'/'

class BotHandler:
    def __init__(self, token):
        self.token = token 
        self.url = 'https://api.telegram.org/bot{}/'.format(token)
        self.num_of_message = 0

    


    def update(self, offset=None , timeout=1000):
        method = 'getupdates'
        params = {'timeout':timeout , 'offset':offset}
        req =  requests.get(self.url+method , params)
        result_list = req.json()['result']
        return result_list

    def lastUpdate(self):
        new_update = self.update()
        if len(new_update) == 0:
            last_update = []
        else:
            last_update = new_update[-1]

        return last_update

    def sendMessage(self, text, chat_id):
        method = 'sendmessage'
        new_url = self.url + method+'?chat_id={}&text={}'.format(chat_id, text)
        req = requests.get(new_url)
        res_json = req.json()
        print('\n\n\n')
        print(res_json)
        if res_json['ok']:
            return True
        else:
            return False

    def getChatId(self,obj):
        chat_id = obj['message']['chat']['id']
        return chat_id
    
    def getMessageId(self, obj):
        msg_id = obj['message']['message_id']
        return msg_id
       
    def replyMessage(self, text,chat_id, message_id):
        #method_send = 'sendmessage'
        #method_reply='reply_to_message_id'
        new_url = self.url +'sendmessage?chat_id={}&reply_to_message_id={}&text={}'.format(str(chat_id),str(message_id),text)
        print('\n\n\n'+new_url)
        req = requests.get(new_url)
        res_json = req.json()
        if res_json['ok']:
            return True
        else:
            return False

    
    #https://api.telegram.org/bot1551813377:AAGi3j56YM2t2rOYUeXT0VAbIbKd4eVQFb4/sendmessage?chat_id=-559007429&reply_to_message_id=11&text=hello

        

def isHello(obj):
    try:
        if 'سلام' in obj['message']['text']: 
            return True
        else:
            return False
    except:
        return False


myBot = BotHandler(TOKEN)



def main():
    msg_list = myBot.update(myBot.num_of_message-5)
    myBot.num_of_message = len(msg_list)
    while(True):
        last_obj = myBot.lastUpdate()
        msg_list = myBot.update()
        print(len(msg_list))
        print(myBot.num_of_message)
        if len(msg_list) > myBot.num_of_message:
            myBot.num_of_message = len(msg_list)
            print(last_obj)
        
            if isHello(last_obj): 
                txt_msg = '...سلام جووون دل سر کیفی عزیز ؟؟ سر کیفی بدم سر کیفی ... الکی ادا حال بدا رو در نیار:))'
                #myBot.sendMessage(txt_msg, myBot.getChatId(last_obj))
                myBot.replyMessage(txt_msg, myBot.getChatId(last_obj),myBot.getMessageId(last_obj))

            

            
            try:
                txt_msg = 'خوش اومدی جون دل...سر کیفی عزیز...خیلییییی خوووش اومدی عزیز'
                try:
                    txt_tag = '@'+ last_obj['message']['new_chat_member']['username']+' '
                except:
                    txt_tag = '@'+ last_obj['message']['new_chat_member']['first_name']+' '

                txt = txt_tag + txt_msg
                print('in the try')
                print(txt)
                myBot.replyMessage(txt, myBot.getChatId(last_obj),myBot.getMessageId(last_obj))
            
            except:
                print('in except :(')
            

main()





