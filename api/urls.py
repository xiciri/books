from django.urls import path
from .views import *

urlpatterns = [
    path('',BooksApiView.as_view(),name='book'),
    path('<int:pk>/',BooksDeteilView.as_view(),name='detail'),
    path('create/', BooksCreateView.as_view(),name='create'),
]