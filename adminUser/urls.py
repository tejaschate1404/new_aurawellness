
from django.urls import path 
from . import views
urlpatterns = [
    path('', views.indexAdmin, name='indexAdmin'),
    # path('base/', views.baseAdmin, name='baseAdmin'),
    
    # Counceiling
    path('add-counceling/', views.addCounseling, name='addCounseling'),
    path('add-category/', views.addCategory, name='addCategory'),
    path('view-counceling/', views.viewCounseling, name='viewCounseling'),
    path('delete/<int:record_id>/', views.delete_counseling, name='delete_counseling'),
    path('view-counseling/<int:record_id>/', views.view_counseling_details, name='view_counseling_details'),

    #Distance
    path('distance-healing/add/', views.addDistanceHealing, name='addDistanceHealing'),
    path('distance-healing/view/', views.viewDistanceHealing, name='viewDistanceHealing'),
    path('distance-healing/details/<int:record_id>/', views.view_distance_healing_details, name='viewDistanceHealingDetails'),
    path('distance-healing/delete/<int:record_id>/', views.delete_distance_healing, name='deleteDistanceHealing'),
    path('distance-healing/add-category/', views.addCategoryDistance, name='addCategoryDistance'),


    # Physical Healing
    path('physical-healing/add/', views.addPhysicalHealing, name='addPhysicalHealing'),
    path('physical-healing/view/', views.viewPhysicalHealing, name='viewPhysicalHealing'),
    path('physical-healing/details/<int:record_id>/', views.viewPhysicalHealingDetails, name='viewPhysicalHealingDetails'),
    path('physical-healing/delete/<int:record_id>/', views.deletePhysicalHealing, name='deletePhysicalHealing'),
    path('physical-healing/add-category/', views.addCategoryPhysical, name='addCategoryPhysical'),


    #Auth
    path('signup/',views.signup_view , name="signupAdmin"),
    path('login/',views.login_view , name="loginAdmin"),
    path('logout/',views.logout_view , name="logoutAdmin"),
    
    
]