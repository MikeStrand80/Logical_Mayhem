"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project_apps.views import SignUp, Login, AdminHomepage, AddCourses, AddUsers, ViewCourses, ViewUsers, UserHomepage,\
                               Assignments, EditCourses, EditInfo
from project_apps import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view(), name='signup'),
    path('', Login.as_view(), name='login'),
    path('homepage/', AdminHomepage.as_view(), name='adminhomepage'),
    path('add_courses/', AddCourses.as_view(), name='addcourses'),
    path('add_users/', AddUsers.as_view(), name='addusers'),
    path('view_courses/', ViewCourses.as_view(), name='viewcourses'),
    path('view_course_details/<int:id>', views.detail_page, name='viewCourseDetails'),
    path('view_users/', ViewUsers.as_view(), name='viewusers'),
    path('view_user_details/<int:id>', views.user_detail_page, name='viewUserDetails'),
    path('user_homepage/', UserHomepage.as_view(), name='userhomepage'),
    path('assignments/', Assignments.as_view(), name='assignments'),
    path('edit_courses/', EditCourses.as_view(), name='editcourses'),
    path('edit_info/', EditInfo.as_view(), name='editinfo'),
]
