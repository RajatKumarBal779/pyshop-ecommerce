from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
    path('cart/',include('cart.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='testapp/password_reset.html'), name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='testapp/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='testapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='testapp/password_reset_complete.html'), name='password_reset_complete'),
    path('payment/',include('payment.urls')),
]
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
