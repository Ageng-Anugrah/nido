from django.urls import path

from app_auth import views
from app_auth.cas_views import (
    login, logout, callback
)


urlpatterns = [
    path('verify-login/', views.VerifyJWTAPIVIEW.as_view()),
    path('login/', login, name='cas_ng_login'),
    path('logout/', logout, name='cas_ng_logout'),
    path('callback/', callback, name='cas_ng_proxy_callback'),

]
