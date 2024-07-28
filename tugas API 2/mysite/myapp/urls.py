from django.urls import path
from myapp import views_api
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('read/', views.readStudent, name='read-data-student'),
    path('create/', views.createStudent, name='create-data-student'),
    path('update/<str:id>', views.updateStudent, name='update-data-student'),
    path('delete/<str:id>', views.deleteStudent, name='delete-data-student'),

    # URLs for Course
    path('read/course', views.readCourse, name='read-data-course'),
    path('create/course', views.createCourse, name='create-data-course'),
    path('update/course/<str:id>', views.updateCourse, name='update-data-course'),
    path('delete/course/<str:id>', views.deleteCourse, name='delete-data-course'),

    # URLs for API Course
    path('api/course', views_api.apiCourse, name='api-view-data-course'),
    path('api/course/update/<str:id>', views_api.updateCourseApi, name='api-update-data-course'),
    path('api/course/delete/<str:id>', views_api.deleteCourseApi, name='api-delete-data-course'),

    # URLs for Consume API
    path('api/consume/course', views_api.consume_api_get, name='api-consume-get-data'),
    #BARU UNTUK POST DAN PUT
    path('api/create/user', views_api.create_user, name='api-create-user'),

    path('api/update/user/<uuid:id>', views_api.update_user, name='api-update-user'),
]

