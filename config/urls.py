"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

admin.site.site_header = "Django Tutor"
admin.site.site_title = "Django Tutor"
admin.site.index_title = "Django Tutor"

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
]

from .settings import DEBUG
if DEBUG:
    import mimetypes
    import debug_toolbar
    from django.urls import include, re_path

    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
