from django.urls import path
from . import views

urlpatterns = [
    # API маршруты
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('documents/', views.DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', views.DocumentDetailView.as_view(), name='document-detail'),

    # Кастомные страницы
    path('login/', views.custom_login, name='login'),
    path('register/', views.custom_register, name='register'),

    # JWT аутентификация
    path('login/', views.login_view, name='login_view'),
]
