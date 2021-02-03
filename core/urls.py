from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views 

from . import views

urlpatterns = [
	path('',views.home, name='home'),
	path('signup/', views.signup, name='signup'),
	path('login/',views.user_login, name='user_login'),
	path('logout/', views.logout_view, name='logout'),
	path('api/data', views.DataView.as_view(), name='api_data'),
	path('api/token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'), 
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

]