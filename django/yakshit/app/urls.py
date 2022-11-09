from django.urls import path
from .import views
urlpatterns = [
    path('',views.home),
    path('sign',views.sign,name='sign'),
    path('log',views.log,name='log'),
    path('logout',views.logout,name='logout'),
    path('load_database',views.load_database,name='load_database'),
]