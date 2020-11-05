from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('account/register/', RegistrationCreateAPIView.as_view(), name='registration'),
    path('account/login/', obtain_auth_token, name="login"),
    path('account/user/', AccountRetrieveAPIView.as_view(), name="account"),
    path('account/readinglist/<readinglist>/', ReadingListAPIView.as_view(), name="readinglist"),
    path('account/serie/<pk>/', SerieRetrieveDestroyAPIView.as_view(), name="serie"),
    path('account/addserie/', SerieCreateAPIView.as_view(), name="addserie"),
    path('account/add/', ReadingListCreateAPIView.as_view(), name="add"),
]
