from django.conf.urls import url
from .import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from accounts.views import password_reset_confirm_view
from tutorial import settings



urlpatterns = [

    url(r'^login/$', login, {'template_name':'accounts/login.html'},name = 'login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^register/$', views.register,name = 'register'),
    url(r'^profile/$', views.view_profile,name = 'view_profile'),

    url(r'^profile/(?P<pk>\d+)/$', views.view_profile,name = 'view_profile_with_pk'),

    url(r'^profile/(?P<pk>\d+)/entries/$', views.view_profile_entries,name = 'view_profile_with_pk_entries'),

    url(r'^profile/edit/$', views.edit_profile,name = 'edit_profile'),
    url(r'^change-password/$', views.change_password,name = 'change_password'),

    url(r'^reset-password/$', password_reset, {'template_name':'accounts/reset_password.html',
    'post_reset_redirect':'accounts:password_reset_done', 'email_template_name':'accounts/reset_password_email.html'}, name = 'reset_password'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name = 'password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm_view, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),


    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),
    
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username')
]


