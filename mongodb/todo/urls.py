from django.urls import path
from . import views


urlpatterns = [
    path('',views.todo ),
    path('delete/<int:todoid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),

]
