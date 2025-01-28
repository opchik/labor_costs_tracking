from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('projects/', ProjectList.as_view(), name='project_list'),
    path('projects/add/', AddProject.as_view(), name='add_project'),
    path('worklogs/', WorkLogList.as_view(), name='worklog_list'),
    path('worklogs/add/', AddWorkLog.as_view(), name='add_worklog'),
]
