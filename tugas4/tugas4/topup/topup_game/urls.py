from django.urls import path
from . import views
from .views import top_up

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('<str:game_name>/', top_up, name='top_up'),

]
