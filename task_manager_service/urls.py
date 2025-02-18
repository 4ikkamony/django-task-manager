from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from task_manager.views import login_view, RegisterView

urlpatterns = [
    path("", include("task_manager.urls", namespace="task_manager")),
    path("login/", login_view, name="login"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
