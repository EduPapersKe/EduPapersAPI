from rest_framework.routers import SimpleRouter
from django.urls import path

from .views import UserViewset, LoginView, LogoutView

router = SimpleRouter()
router.register(r'users', UserViewset)


urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/logout/', LogoutView.as_view(), name='log-out'),
]

urlpatterns += router.urls