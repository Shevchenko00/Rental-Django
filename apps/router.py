from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.users.urls')),
    path('house/', include('apps.housing.urls'))
]