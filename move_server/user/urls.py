from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^user/$', MoveUser.as_view()),
    url(r'^download/$', DownloadUser.as_view())
]

