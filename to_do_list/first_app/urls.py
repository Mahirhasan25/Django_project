from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowInCompleteTask, name='showtask'),
    path('completetask', views.ShowCompleteTask, name='completetask'),
    path('addtask/', views.AddTaskForm, name='addtask'),
    path('completetask/<int:id>', views.CompleteTask, name='completetask'),
    path('editetask/<int:id>', views.EditTask, name='editetask'),
    path('detailtask/<int:id>', views.DetailTask, name='detailtask'),
    path('deletetask/<int:id>', views.DeleteTask, name='deletetask'),
]