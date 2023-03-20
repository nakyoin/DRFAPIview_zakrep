from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdApiView.as_view()),
    path('<int:pk>/', views.ProdApiView.as_view()),
    path('cart/', views.CartApi.as_view()),
]