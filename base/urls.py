from django.urls import path
from .views import getUserDate

urlpatterns = [
    path('', getUserDate.as_view(), name='user_date')
]