from django.conf.urls import url, include

urlpatterns = [
    url('^move/user/', include("user.urls")),  # to user
]
