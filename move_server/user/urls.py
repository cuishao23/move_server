from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^user/$', MoveUser.as_view()),
    url(r'^download/$', DownloadUser.as_view()),
    url(r'^mobile/$', MobileUser.as_view()),
    url(r'^mobiledownload/$', DownloadMobileUser.as_view()),
    url(r'^basic/$', BasicUser.as_view()),
    url(r'^basicdownload/$', DownloadBasicUser.as_view()),
    url(r'^totalpagenum/$', TotalPageNum.as_view()),
    # url(r'^login$', LoginView.as_view()),
    # url(r'^loginout$', LoginOutView.as_view())
]

