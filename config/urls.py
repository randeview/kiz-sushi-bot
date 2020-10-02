from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include, path
api_url_patterns = [
    path("fastfood/", include("kiz_sushi_bot.main.urls", namespace="fastfood")),
    path("bot/", include("kiz_sushi_bot.bot.urls", namespace="bot")),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Bot API",
      default_version='v1',
      description="This is bot",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nurlantukenbayev@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include(api_url_patterns)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
