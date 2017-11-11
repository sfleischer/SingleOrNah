from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^$', views.BlogSearchListView, name = 'blog_search_list_view')
]
