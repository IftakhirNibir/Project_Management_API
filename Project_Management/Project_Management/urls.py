from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API Documentation",
        default_version='v1',
        description="The Project Management API facilitates team collaboration on projects by providing a comprehensive set of endpoints to manage users, projects, tasks, and comments. Designed for integration with both front-end web and mobile applications, this API serves as the backbone for a robust project management tool.",
        contact=openapi.Contact(email="iftakhirnibir@gmail.com"),
        license=openapi.License(name="Iftakhir Mozumder Nibir"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
