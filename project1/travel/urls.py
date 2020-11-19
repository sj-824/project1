from django.urls import path
from . import views 

urlpatterns = [
    path('list/', views.listview, name = 'list'),
    path('form/', views.Formview.as_view(), name = 'form'),
    path('delete/<int:pk>/',views.deleteview, name = 'delete'),
    path('edit/<int:pk>/',views.Editview.as_view(), name = 'edit'),
    path('group/',views.Groupview.as_view(), name = 'group'),
    path('group_list',views.group_list, name = 'group_list'),
    path('',views.Top.as_view(), name = 'top'),
    path('login/',views.Login.as_view(),name = 'login'),
    path('logput/',views.Logout.as_view(), name = 'logout'),
    path('user_create/',  views.UserCewateForm.as_view(), name = 'user_create'),
    path('user_create/done',views.UserCreateDone.as_view(),'user_create_done'),

]