from .import views
from django.urls import path

urlpatterns = [
    path('', views.index ,name='index'),
    path('register_user/',views.register_user,name='register_user'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('create_post/',views.create_post, name='create_post'),
    path('update_post/<int:id>/', views.update_post,name="update_post"),
    path('delete_post/<int:id>/', views.delete_post,name="delete_post"),

    
]
