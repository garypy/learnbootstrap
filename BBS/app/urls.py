from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
        url(r'^bbs/$', views.index, name='index'),
        url(r'^page/(\d+)/$', views.page, name='page'),
        #url(r'^add_category/$', views.add_category, name='add_category'),
		#url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
		)

