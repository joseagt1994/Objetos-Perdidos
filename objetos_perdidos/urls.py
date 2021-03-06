"""objetos_perdidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from objetos_lose import settings
from objetos.views import publicar,agregarImagenes,verPublicacion,enviarMensaje,publicarEncontrado,publicacion_detallada,vistaLogin
from objetos.views import perfil,conversacion,logout,registro

urlpatterns = [
    url(r'^$', vistaLogin, name="login"),
    url(r'^ver/(?P<cod_publicacion>\d+)$',publicacion_detallada),
    url(r'^agregarImagenes/(?P<cod_publicacion>\d+)$', agregarImagenes, name="agregarImagenes"),
    url(r'^admin/', admin.site.urls),
    url(r'^visualizar$',verPublicacion),
    url(r'^reclamar/(?P<cod_publicacion>\d+)$',enviarMensaje),
    url(r'^encontrado$',publicarEncontrado),
    url(r'^perfil/(?P<cod_user>\d+)$',perfil),
    url(r'^conversacion/(?P<cod_mensaje>\d+)$',conversacion),
    url(r'^logout$',logout),
    url(r'^registrarse$',registro),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
