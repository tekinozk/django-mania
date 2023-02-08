from django.urls import path
from blog.views import all_post_view,category_view,tag_view,post_detail
    
app_name="blog"
urlpatterns = [
path("",all_post_view,name="all_post_view"),
path("category/<slug:category_slug>/",category_view,name="category_view"),
path("category/<slug:category_slug>/<slug:post_slug>/",post_detail,name="post_detail"),
path("tag/<slug:tag_slug>/",tag_view,name="tag_view"),
]