from django.urls import path

from igwt_app.views import igwt_view

app_name='igwt'

urlpatterns = [
    path('', igwt_view, name='igwt'),
]
