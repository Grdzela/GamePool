from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.game, name="game"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('<int:id>/', views.detail_page, name='detail'),
    # path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
