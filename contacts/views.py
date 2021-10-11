from django.shortcuts import render
from .models import *
from .sendtelegram import sendTelegram, sendQuestionnaireTelegram


# Create your views here.
location = 'contacts'

def contacts_page(request):
    return render(request, 'contacts/contacts_page.html', {'location':location})



def get_request_for_call_back(request):
    if request.POST:
        form_id = 'callback'
        name = request.POST['name']
        phone = request.POST['phone']
        time_to_call = request.POST['time_to_call']
        if phone:
            call_back_order = CallBackOrder(name = name, phone = phone, time_to_call = time_to_call)
            call_back_order.save()
            sendTelegram(name, phone, time_to_call, form_id, 'phone')
            return render(request, 'contacts/thanks_page.html', {'name':name,
                                                        'phone':phone,
                                                        'time_to_call':time_to_call,
                                                        'form_id':form_id,
                                                        'location':location
                                                        })
        else:
            return render(request, 'contacts/thanks_page.html', {'error':'error'
                                                                    })
    else:
        return render(request, 'contacts/thanks_page.html')



def get_a_question(request):
    if request.POST:
        form_id = 'question'
        name = request.POST['name']
        mail = request.POST['mail']
        phone = request.POST['phone']
        question = request.POST['question']
        contact = None
        if mail:
            contact = mail
            toggle = 'mail'
        if phone:
            contact = phone
            toggle = 'phone'
        if contact:
            customer_question = CustomerQuestion(name = name, phone = phone, mail = mail, question = question)
            customer_question.save()
            sendTelegram(name, contact, question, form_id, toggle)
            return render(request, 'contacts/thanks_page.html', {'name':name,
                                                                'contact':contact,
                                                                'question':question,
                                                                'form_id':form_id,
                                                                'location':location,
                                                                'toggle':toggle
                                                                })
        else:
            return render(request, 'contacts/thanks_page.html', {'error':'error'
                                                                    })
    else:
        return render(request, 'contacts/thanks_page.html')



def get_order(request):
    if request.POST:
        form_id = 'order'
        name = request.POST['name']
        phone = request.POST['phone']
        comment = request.POST['comment']
        if phone:
            customer_order = Order(name = name, phone = phone, comment = comment)
            customer_order.save()
            sendTelegram(name, phone, comment, form_id, 'phone')
            return render(request, 'contacts/thanks_page.html', {'name':name,
                                                            'phone':phone,
                                                            'comment':comment,
                                                            'form_id':form_id,
                                                            'location':location
                                                            })
        else:
            return render(request, 'contacts/thanks_page.html', {'error':'error'
                                                                    })

    else:
        return render(request, 'contacts/thanks_page.html')



def get_a_questionnaire(request):
    if request.POST:
        form_id = 'cooperation'
        name = request.POST['name']
        city = request.POST['city']
        mail = request.POST['mail']
        phone = request.POST['phone']
        site = request.POST['site']
        company = request.POST['company']
        if phone:
            cooperation = Cooperation(name = name, city = city, mail = mail, phone = phone, site = site, company = company)
            cooperation.save()
            sendQuestionnaireTelegram(name, city, mail, phone, site, company)
            return render(request, 'contacts/thanks_page.html', {'name':name,
                                                            'form_id':form_id,
                                                            'location':location
                                                            })
        else:
            return render(request, 'contacts/thanks_page.html', {'error':'error'
                                                                    })


    else:
        return render(request, 'contacts/thanks_page.html')
