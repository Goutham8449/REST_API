from .views import BlogPostRudView , BlogPostAPIView
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

urlpatterns = [
	url(r'^(?P<pk>\d+)/$',BlogPostRudView.as_view(),name='post-rud'),
	url(r'^api/auth/login/$',obtain_jwt_token,name = 'api-login'),
	url(r'^$',BlogPostAPIView.as_view(),name='post-listcreate'),

]