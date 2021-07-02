from django.urls import path
from profile.views import forms_page_token_views, profile_post_views

app_name = 'profile'

urlpatterns = [
    path('fill', forms_page_token_views, name='fill-profile-token'),
    path('post', profile_post_views, name='post-profile'),
]
