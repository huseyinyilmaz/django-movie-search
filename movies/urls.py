from django.conf.urls import url
from movies import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='movies-index'),
    url(r'^name/$', views.NameSearchView.as_view(), name='movies-name-search'),
    url(r'^id/$', views.IDSearchView.as_view(), name='movies-id-search'),
]
