from django.urls import path
from data import views

app_name='data'
urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.display,name='display'),
    path('adddev/' , views.developerData , name='devdata'),
    path('search' , views.search_view , name='search') ,
    path('<int:id>/' , views.edit , name='edit'),
    # path('adddev/' , views.DeveloperForm, name='adddev'),
]