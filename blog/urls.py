from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path(
            'rest_framework/api-auth/',
            include('rest_framework.urls', namespace='rest_framework')
        )
    ] + urlpatterns
