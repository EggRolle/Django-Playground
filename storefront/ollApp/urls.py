from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('oldHtml/', views.old_sample)
]