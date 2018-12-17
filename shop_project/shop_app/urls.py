from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('products/<int:product_id>/', views.product, name='product'),
  path('clients/', views.clients, name='clients'),
  path('clients/<int:client_id>/', views.client, name='client'),

  path('comments/', views.comments, name='comments'),
  path('comments/<int:comment_id>/', views.comment, name='comment'),
  path('products/<int:product_id>/comment_form', views.comment_form, name='comment_form'),
  path('maillots/', views.maillots, name='maillots'),
  path('maillot/<int:maillot_id>/', views.maillot, name='maillot'),

]