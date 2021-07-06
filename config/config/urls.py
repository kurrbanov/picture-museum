from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from museum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name="main"),
    path('pictures/', views.all_pictures_view, name="pictures"),
    path('authors/', views.all_authors_view, name="authors"),
    path('pictures/<int:pk>', views.show_picture, name="picture"),
    path('authors/<int:pk>', views.show_author, name="author")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
