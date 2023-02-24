from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # my patterns
    path('', include('itemapp.urls', namespace='itemapp')),
]
