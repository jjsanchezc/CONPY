# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('upload-download/', views.upload, name='upload-download'),
    path('soporte/',views.read_input),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
