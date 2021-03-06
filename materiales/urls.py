from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', views.materiales, name='materiales'),
    path('<slug:slug_material>/', views.detallematerial, name='detallematerial'),
]

materiales_urldash = ([
    path('list/', MaterialListView.as_view(), name='list'),
    path('create/',MaterialCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MaterialUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete')
], 'materiales_dash')
