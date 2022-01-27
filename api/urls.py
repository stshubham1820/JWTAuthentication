from . import views
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('api-auth/', include('rest_framework.urls')),
    path('data/',views.Stud.as_view()),
    path('data/<str:pk>/',views.Studpk.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]