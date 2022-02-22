from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('cordless/', views.CordlessModelList.as_view(), name='cordless'),
    path('robot/', views.RobotModelList.as_view(), name='robot'),
    path('cordless/<int:pk>', views.CordlessDetailView.as_view(), name='cordless-detail'),
    path('robot/<int:pk>', views.RobotDetailView.as_view(), name='robot-detail'),

]