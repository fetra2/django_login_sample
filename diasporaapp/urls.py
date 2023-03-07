from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns...
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name='contact'),
]

