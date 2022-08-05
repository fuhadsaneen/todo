from django.urls import path
from . import views

app_name = 'todo_app'
urlpatterns = [

    path('',views.hello, name='hello'),
    path('delete/<int:taskid>',views.delete, name='delete'),
    path('update/<int:id>',views.update, name='update'),
    path('cvbhome/',views.Tasklistview.as_view(),name='cvbhome'),
    path('cvbdetail/<int:pk>',views.Taskdetailview.as_view(),name='cvbdetail'),
    path('cvbupdate/<int:pk>',views.TaskUpdateView.as_view(),name='cvbUpdate'),
]
