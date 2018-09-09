from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^home$', views.home),
    url(r'^user/(?P<id>\d+$)$', views.user),
    url(r'^edit/(?P<id>\d+$)$', views.edit),
    url(r'^delete/(?P<id>\d+$)$', views.delete),
    url(r'^editUser/(?P<id>\d+$)$', views.editUser),
    url(r'^process$', views.process),
    url(r'^addQuote$', views.addQuote),
    url(r'^like/(?P<id>\d+$)$', views.like),
    # url(r'^process$', views.process),
    # url(r'^books$', views.welcome),
    # url(r'^books/add$', views.add),
    # url(r'^newbook$', views.newBook),
    # url(r'^books/(?P<id>\d+$)', views.bookId),
    # url(r'^addreview$', views.bookReview),
    # url(r'^books/id$', views.bookId),
    # url(r'^user/(?P<id>\d+$)$', views.user),
    url(r'^logout$', views.logout)
]