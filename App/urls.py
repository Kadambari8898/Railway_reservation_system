
from django.urls import path
from . import views
app_name='Tejas_App'

urlpatterns = [
    path('', views.func, name="home"),

    path('home/',views.func0,name="Home"),

    path('about/',views.func1, name="About"),

    path('contact/',views.func2, name="contact"),

    path('booking/',views.fun3, name="booking"),

    path('reservation/',views.func4, name="reservation"),
 
    path('signup/',views.func5, name="signup"),

   

]
