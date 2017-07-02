from django.conf.urls import url
from basic_app import views

# TEMPLATE URLS!
app_name = 'basic_app'

urlspatterns=[
    urls(r'^register/$', views.register, name='register')
    
]
