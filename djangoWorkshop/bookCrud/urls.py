from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),  # Root URL -> index.html
    path('book/', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:id>/', views.book_update, name='book_update'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
]