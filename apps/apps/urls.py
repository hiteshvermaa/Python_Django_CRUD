from django.urls import include, path
from django.contrib import admin

import theme.views

urlpatterns = [
    path('', theme.views.home),
    path('Attendence_Class_base_view/', include('Attendence_Class_base_view.urls')),
    path('Attendence_Function_base_view/', include('Attendence_Function_base_view.urls')),
    path('Attendence_Function_base_view_user/', include('Attendence_Function_base_view_user.urls')),

    # Enable built-in authentication views
    path('accounts/', include('django.contrib.auth.urls')),    
    # Enable built-in admin interface
    path('admin/', admin.site.urls),
]
