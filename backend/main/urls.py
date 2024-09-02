"""
URL configuration for berry_information_engine main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from django.http import JsonResponse


from django.conf import settings
from django.urls import re_path
from django.views.static import serve


# Catch-all pattern to serve the index.html for any path
def serve_index(request, path):
    # TODO: need to fix document root which is path to dist folder
    return serve(request, path, document_root=settings.STATICFILES_DIRS[0])


def health_check():
    return JsonResponse({"status": "ok"})


urlpatterns = []

# Enable DEBUG to serve static files from Django Server
if settings.DEBUG:
    from django.conf.urls.static import static

    # Return a URL pattern for serving static files from Django server.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('health_check', health_check, name='health_check'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    path('auth/google/callback/', views.google_callback, name='google_callback'),
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    # catch all
    re_path(r'^(?:.*)/?$', serve_index, {'path': '/index.html'}),
]
