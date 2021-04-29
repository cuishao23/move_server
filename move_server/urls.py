from django.conf.urls import url, include

urlpatterns = [
    url('^move/', include("user.urls")),  # to user
]
