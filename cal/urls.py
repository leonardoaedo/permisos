from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import *
from edt.views import PermisoListView,BitHorasPDF,BitHorasExcel,EstadisticaPermisosExcel,EstadisticaPermisosPDF,AnuladosPDF,AnuladosExcel
urlpatterns = [

    # Examples:
    # url(r'^$', 'cal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/','edt.views.login' ),
    url(r'^$','edt.views.index' ),
    url(r"^verpermiso/(?P<pk>\d+)/$","edt.views.verpermiso"),
    url(r"^verpermiso2/(?P<pk>\d+)/$","edt.views.verpermiso2"),
    url(r'^logout/','edt.views.logout' ),
    url(r'^upload/(?P<pk>\d+?)/$',"edt.views.upload" ),
    url(r'^devueltas/(?P<pk>\d+?)/$',"edt.views.devueltas" ),
    url(r'^main/(\d+)/$', "edt.views.main"),
    url(r"^comprobante/(?P<pk>\d+)/$","edt.views.comprobante" ),
    url(r'^urlcalendario/$', "edt.views.urlcalendario"),
    url(r'^wsCalendari/', "edt.views.wsCalendario"),
    url(r'^wsPermiso_Jefatura/', "edt.views.wsPermiso_Jefatura"),
    url(r'^main/', "edt.views.main"),
    url(r'^permiso/','edt.views.ingresapermiso' ),
    url(r'^permisolst/','edt.views.permisolst' ),
    url(r'^resolucion/','edt.views.aprobarRechazar' ),
    url(r"^respuesta/(?P<pk>\d+)/$","edt.views.mostrar_respuesta" ),
    url(r'^genero/','edt.views.wsGenero' ),
    url(r'^jefaturas/','edt.views.wsJefaturas' ),
    url(r'^permiso_jefatura/','edt.views.permiso_jefatura' ),
    url(r'^edades/','edt.views.wsEdades' ),
    url(r'^bitacora/', PermisoListView.as_view()),
    # url(r'^modpermiso/', PermisoUpdateView.as_view()),
    url(r'^anularlst/','edt.views.anularlst' ),
    url(r"^anulapermiso/(?P<pk>\d+)/$","edt.views.anulapermiso"),
    url(r'^anula/','edt.views.anula'),
    url(r"^anulado/(?P<pk>\d+)/$","edt.views.mostrar_anulado" ),    
    url(r'^horas/', "edt.views.horas"),
    url(r"^devolver/","edt.views.devuelvehoras"),
    url(r"^descontar/","edt.views.descontar"),
    url(r'^bgeneral/', "edt.views.bitgeneral"),
    url(r'^anulaciones/', "edt.views.anulaciones"),
    url(r'^bfuncionario/',"edt.views.bitfuncionario"),       
    url(r'^permisosusuario/(?P<pk>\d+)/$',"edt.views.permisosusuario"),
    url(r'^bhorasEXCEL/$',BitHorasExcel.as_view(), name="BitHorasExcel"),
    url(r'^bhorasPDF/',BitHorasPDF.as_view()),    
    url(r'^bhoras/',"edt.views.bithoras"),
    url(r'^anuladosEXCEL/$',AnuladosExcel.as_view(), name="AnuladosExcel"),
    url(r'^anuladosPDF/',AnuladosPDF.as_view()),
    url(r'^anulados/','edt.views.anulados' ),
    url(r'^estadisticapermisosPDF/',EstadisticaPermisosPDF.as_view()),
    url(r'^estadisticapermisosEXCEL/$',EstadisticaPermisosExcel.as_view(), name="EstadisticaPermisosExcel"),
    url(r'^estadisticapermisos/',"edt.views.EstadisticaPermisos"),



    # url(r'^(?P<slug>[-\w]+)/$', PermisoDetailView.as_view(), name='permiso-detail'),

]
