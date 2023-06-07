from django.urls import path

from . import views
# app_name = 'geekblog'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('blog/', views.blog, name='blog'),
    path('blog/flush', views.flush, name='flush'),
    
    # path('self', views.self, name='self'),
    # path('article/<int:article_id>/', views.article, name='article'),
    # path('edit', views.edit, name='edit'),
    # path('search', views.search, name='search')
]