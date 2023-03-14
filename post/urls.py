from django.urls import path
from . import views

urlpatterns = {
    path('hello/', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('passion/', views.baby, name='passion'),
    path('details/', views.details, name='details')
}