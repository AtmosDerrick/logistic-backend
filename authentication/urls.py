from django.urls import path
from authentication.views import login, signup, test_token

urlpatterns = [
    path('login/', login ),
    path('signup/',signup),
    # path('adminsignup/', signup_by_admin),
    # path('profile/', create_profile ),
    # path('user/', profile ),
    # path('user/<id>/', oneProfile),

    # path('test_token',test_token),
    # path('logout/', user_logout),

  
]
