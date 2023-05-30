from django.urls import path

from .views import ProductView, ChatbotView, SetView, InfoView


urlpatterns = [
    path('product/', ProductView.as_view()),
    path('bot/', ChatbotView.as_view()),
    path('set/', SetView.as_view()),
    path('info/', InfoView.as_view()),
]
