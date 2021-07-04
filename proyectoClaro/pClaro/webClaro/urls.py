from django.contrib import admin
from django.urls import path
from webClaro import views
from django.conf import settings

# Importar rutas estáticas.
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cliente/<id>/', views.verCliente, name='verCliente'),
    path('registroCliente/', views.registroCliente, name='registroCliente'),
    path('perfil/', views.perfil, name='perfil'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    path('modificarCliente/<id>/', views.modificarCliente, name='modificarCliente'),
    path('actualizarCliente/', views.actualizarCliente, name='actualizarCliente'),
]

# Incluir rutas estáticas.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)