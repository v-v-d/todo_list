from django.urls import path

import todo.views as todo_views


urlpatterns = [
    path('todo/', todo_views.TodoList.as_view()),
    path('todo/<int:pk>/', todo_views.TodoDetail.as_view()),
]
