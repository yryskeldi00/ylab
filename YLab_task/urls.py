from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="TAPP API",
      default_version='v1',
      description="TAPP API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="abdymazhinov.timur@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(settings.API_PERMISSION,),
)

v1_api = ([
    path('account/', include('main.urls')),
], 'v1')

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^docs(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    re_path(r'^redocs/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

    re_path(r'api/v1/', include(v1_api, namespace='v1')),
]
