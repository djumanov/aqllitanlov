from django.urls import path

from .views import ProductView, ChatbotView


urlpatterns = [
    path('product/', ProductView.as_view()),
    path('bot/', ChatbotView.as_view()),
]
