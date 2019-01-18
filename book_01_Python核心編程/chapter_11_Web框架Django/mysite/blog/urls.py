#!/usr/bin/env python

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('blog/', views.archive),
    path('blog/create/', views.blog_create),
]