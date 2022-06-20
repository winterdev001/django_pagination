from django.urls import path, include
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:author_id>', views.detail, name='detail'),
    path('edit/<int:author_id>', views.edit, name='edit'),
    path('delete/<int:author_id>',views.delete, name='delete'),
]