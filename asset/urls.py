from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views
from .views import AssetListCreateAPIView

#import index from this project


urlpatterns = [
    #point root path to Index view
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add-item/', AddItem.as_view(), name='add-item'),

    #id of the item here to know which item we're editing
    path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='asset/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='asset/logout.html'), name='logout'),
    path('api/', AssetListCreateAPIView.as_view(), name="inventoryitem-list-create"),

]
