from django.urls import path
from myapp import views,views_api

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),   
    path('read/', views.readStudent, name='read-data-student'),   
    path('create/', views.createStudent, name='create-data-student'),   
    path('update/<str:id>', views.updateStudent, name='update-data-student'),   
    path('delete/<str:id>', views.deleteStudent, name='delete-data-student'),   #urls untuk Course   
    path('read/course', views.readCourse, name='read-data-course'),   
    path('create/course', views.createCourse, name='create-data-course'),   
    path('update/course/<str:id>', views.updateCourse, name='update-data-course'),   
    path('delete/course/<str:id>', views.deleteCourse, name='delete-data-course'),   
    path('api/course/', views_api.apiCourse, name='api-view-data-course'),]