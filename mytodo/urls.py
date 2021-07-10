from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('task-create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>', views.TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>', views.TaskDeleteView.as_view(), name='task-delete'),
]