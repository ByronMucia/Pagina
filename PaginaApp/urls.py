from django.urls import path

from PaginaApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path("",views.home, name="Home"),
    path("service",views.service, name="Service"),
    path("contact",views.contact, name="Contacto"),
    path("about",views.about, name="About"),
    path("contacto",views.contact, name="Contacto"),
    path("page",views.about, name="Page"),
   # path("blog",views.blog, name="Blog"),
    path("detail",views.detail, name="Detail"),
    path("price",views.price, name="Price"),
    path("feature",views.feature, name="Feature"),
    path("team",views.team, name="Team"),
    path("testimonial",views.testimonial, name="Testimonial"),
   
    
    
]

#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)