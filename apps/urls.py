from django.urls import path
from apps.views import UserListView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list_page'),
    path('user/delete/<int:pk>', UserDeleteView.as_view(), name='delete_user_page'),
]