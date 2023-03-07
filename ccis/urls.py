from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('conta', views.conta, name='conta'),
    path('formLogin', views.formLogin, name='formLogin')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

