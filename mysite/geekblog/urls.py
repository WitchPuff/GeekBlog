from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('blog/', views.blog, name='blog'),
    path('blog?page=<int:page_id>/', views.blog, name='blog'),
    
    # path('self', views.self, name='self'),
    # path('article/<int:article_id>/', views.article, name='article'),
    # path('edit', views.edit, name='edit'),
    # path('search', views.search, name='search')
]