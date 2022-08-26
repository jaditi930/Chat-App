from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('index/',views.index),
    path('index/checkRoom/',views.checkRoom),
    path('<str:room>/',views.room),
    path('<str:room>/send/',views.send),
    path('getMessages/<str:room>/',views.getMessages),
]
