
from django.conf.urls import url
from . import views

app_name = 'qshock'

urlpatterns = [
    # /qshock/
    url( r'^$', views.index, name = 'index' ),

    # /qshock/dashboard
    url( r'^dashboard/$', views.dashboard, name = 'dashboard' ),

    # /qshock/5 -> 5 becomes parameter of case_id and given to the detail method in views.py
    url(r'^(?P<case_id>[0-9]+)/$', views.detail, name='detail'),

    # /qshock/5/answer -> 5 becomes parameter of case_id and given to the answer method in views.py
    url(r'^(?P<case_id>[0-9]+)/answer/$', views.answer, name='answer'),
]

