from django.urls import path
from .views import PeriodListViews, CourseListViews, classRoomListViews, StudentListView, TeacherListViews

urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view'),
    path('Teacher/',TeacherListViews.as_view(),name = "teachers_list_view"),
    path('Courses/',CourseListViews.as_view(),name = "course_list_view"),
    path('ClassRoom/',classRoomListViews.as_view(),name = "class_room_list_view"),
    path('Period/',PeriodListViews.as_view(),name = "class_period_list_view"),

]