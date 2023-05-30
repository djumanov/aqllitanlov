from django.urls import path

from .views import ProductView, RecommentView


urlpatterns = [
    path('product/', ProductView.as_view()),
    path('bot/', RecommentView.as_view()),
    path('set/', RecommentView.as_view()),
    path('info/', RecommentView.as_view()),
]
