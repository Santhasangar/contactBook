from django.urls import path,include
from book.views import *




urlpatterns = [
    
    path('search/', contactBookList.as_view(), name="contactBookList"),
    path('create-contact/', createContactAPIView.as_view(), name="createContact"),
    path('contact-detail/<int:id>/', contactBookDetailView.as_view(), name="contactBookDetail"),
]