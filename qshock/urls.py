
from django.conf.urls import url
from . import views

app_name = 'qshock'

urlpatterns = [
    # /qshock/
    url( r'^$', views.index2, name = 'index' ),

    url(r'^test/$', views.test, name='test'),
    url(r'^test_create/$', views.test_create, name='test_create'),

    # /qshock/dashboard
    url( r'^dashboard/$', views.dashboard_neo, name = 'dashboard' ),

    # /qshock/5 -> 5 becomes parameter of case_id and given to the detail method in views.py
    url(r'^(?P<id>[0-9]+)/$', views.detail2, name='detail'),

    url(r'^(?P<id>[0-9]+)/othershock/$', views.othershock, name='othershock'),

    url(r'^(?P<id>[0-9]+)/secondfactor/$', views.second, name='second'),

    # /qshock/5/answer -> 5 becomes parameter of case_id and given to the answer method in views.py
    url(r'^(?P<id>[0-9]+)/answer/$', views.answer, name='answer'),

    url(r'^(?P<id>[0-9]+)/follow/$', views.follow, name='follow'),
]

