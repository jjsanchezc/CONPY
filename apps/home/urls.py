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
    path('soporte-add/',views.read_new_input),
    path('a/',views.a),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
