from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
path('', views.contacts_page, name='contacts_page'),
path('thanks-for-callback/', views.get_request_for_call_back, name='get_request_for_call_back'),
path('thanks-for-question/', views.get_a_question, name='get_a_question'),
path('thanks-for-order/', views.get_order, name='get_order'),
path('thanks-for-cooperation/', views.get_a_questionnaire, name='get_a_questionnaire'),
]
