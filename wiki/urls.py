from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Admin
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/create/', views.page_create, name='page_create'),
    path('admin-dashboard/edit/<slug:slug>/', views.page_edit, name='page_edit'),
    path('admin-dashboard/delete/<slug:slug>/', views.page_delete, name='page_delete'),
    path('admin-dashboard/toggle/<slug:slug>/', views.page_toggle_status, name='page_toggle_status'),
]
