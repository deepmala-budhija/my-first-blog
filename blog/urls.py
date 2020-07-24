from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'LineListings', views.LineListingViewSet)

urlpatterns = [

    #path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('linelist/', views.linelist_list, name = 'linelist_list'),
    path('linelist/<int:pk>/', views.linelist_detail, name='linelist_detail'),
    path('linelist/new/', views.linelist_new, name='linelist_new'),
    path('linelist/<int:pk>/edit/', views.linelist_edit, name='linelist_edit'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]