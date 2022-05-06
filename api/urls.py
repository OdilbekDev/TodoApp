from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/all/', AllTask),
    path('tasks/', Search_Task),
    path('tasks/new/', Create_Task),
    path('tasks/del/', Delete_Task),
    path('tasks/edit/status/', Edit_Task),
    path('tasks/filter/status/', Filter_Status_Task),
    path('tasks/filter/date/', Filter_Date_Task),
]
