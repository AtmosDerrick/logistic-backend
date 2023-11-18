from django.urls import path
from authentication.views import login, signup, test_token, create_profile, profile,oneProfile


urlpatterns = [
    path('login/', login ),
    path('signup/',signup),
    path('profile/', create_profile ),
    path('user/', profile ),
    path('user/<id>/', oneProfile),

    path('test_token',test_token),
  
]
