from django.urls import path,include
from . import views


#set name for app
app_name = "todo-app"

#write paths here
urlpatterns = [
    path('', views.TodoListView.as_view(), name='base-todo'),
    path('create/',views.TodoCreateView.as_view(),name='create-todo'),
    path('delete/<int:pk>',views.TodoDeleteView.as_view(),name='delete-todo'),
    path('done/<int:pk>/', views.DoneTodoView.as_view(), name='done-todo'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update-todo'),
    path('api/', include("todo_app.api.urls")),
]