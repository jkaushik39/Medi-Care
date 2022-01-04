from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name ="home"),
    path('about/', views.about , name = "about"),
    path('contact/', views.contact , name = "contact"),
    path('doc1/', views.doc1 , name="doc1"),
    path('doc2/', views.doc2 , name="doc2"),
    path('doc3/', views.doc3 , name="doc3"),
    path('doc4/', views.doc4 , name="doc4"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('payment/', views.payment, name="payment"),





] 