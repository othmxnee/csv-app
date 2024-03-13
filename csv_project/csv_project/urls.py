
from django.contrib import admin
from django.urls import path, include  # include is used to reference app-specific urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('csv_app.urls')),  # Include your app's URLs under the 'api/' path
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]