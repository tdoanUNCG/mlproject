from django.conf.urls import url
from movies import views

urlpatterns = [
    url(r'^$',views.movies,name="index"),
]