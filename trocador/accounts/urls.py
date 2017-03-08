from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
		url(r'^$', views.dashboard, name='dashboard'),
		url(r'^entrar/$', auth_views.login, 
			{'template_name': 'accounts/login.html'}, name='login'),
		url(r'^sair/$', auth_views.logout, 
			{'next_page': 'core:home'}, name='logout'),
		url(r'^cadastre-se/$', views.register, name='register'),
		url(r'^nova_senha/$', views.password_reset, name='password_reset'),
		url(r'^confirmar_nova_senha/(?P<key>\w+)$', views.password_reset_confirm, name='password_reset_confirm'),
		url(r'^editar/$', views.edit, name='edit'),
		url(r'^editar_senha/$', views.edit_password, name='edit_password'),
]