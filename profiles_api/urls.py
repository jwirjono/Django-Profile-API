from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


# APIView Doesn't need Router
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
# if model view set doesn't need base_name because queryset, name will be configured as the name of the model assigned to it
router.register('profile', views.UserProfileViewSet)


urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
