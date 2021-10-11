from dotenv import load_dotenv
import os
import requests


load_dotenv(override=True)
token = os.getenv('TG_TOKEN')
chat_id = os.getenv('TG_CHAT_ID')
api = 'https://api.telegram.org/bot'
method = api + token + '/sendMessage'



def sendTelegram(name, contact, text, form_id, toggle):


    if form_id == 'callback' and toggle == 'phone':
        message = 'Заявка на обратный звонок\nИмя: ' + name + '\nТелефон: ' + contact + '\nУдобное время для звонка: ' + text

    elif form_id == 'question' and toggle == 'mail':
        message = 'Вопрос с формы обратной связи\nИмя: ' + name + '\nЭмейл: ' + contact + '\nВопрос: ' + text

    elif form_id == 'question' and toggle == 'phone':
        message = 'Вопрос с формы обратной связи\nИмя: ' + name + '\nТелефон: ' + contact + '\nВопрос: ' + text


    elif form_id == 'order' and toggle == 'phone':
        message = 'Заявка на изготовление мебели под заказ\nИмя: ' + name + '\nТелефон: ' + contact + '\nКомментарий: ' + text

    else:
        message = ''


    try:
        req = requests.post(method, data={
            'chat_id':chat_id,
            'text':message,
            })
    except:
        pass

    finally:
        if req.status_code != 200:
            print('Ошибка отправки!')
        elif req.status_code == 500:
            print('Ошибка 500!')
        else:
            print('Все ок сообщение отправлено!')



def sendQuestionnaireTelegram(name, city, mail, phone, site, company):

    message = 'Заявка на сотрудничество\nИмя: ' + name + '\nГород: ' + city + '\nЭмейл: ' + mail + '\nТелефон: ' + phone + '\nСайт: ' + site + '\nКомпания: ' + company

    try:
        req = requests.post(method, data={
            'chat_id':chat_id,
            'text':message,
            })
    except:
        pass

    finally:
        if req.status_code != 200:
            print('Ошибка отправки!')
        elif req.status_code == 500:
            print('Ошибка 500!')
        else:
            print('Все ок сообщение отправлено!')
