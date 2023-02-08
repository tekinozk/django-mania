from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField



class BlogTag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = "title",unique = True,)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse(
            "blog:tag_view",
            kwargs={
                "tag_slug":self.slug,  
            }
        )    


class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = "title",unique = True,)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse(
            "blog:category_view",
            kwargs={
                "category_slug":self.slug
            }
        )

class Post(models.Model):
    slug = AutoSlugField(populate_from = "title",unique=True,)
    tag = models.ManyToManyField(BlogTag)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory,on_delete=models.SET_NULL,null=True)
    title = models.CharField( max_length=200 )
    content = HTMLField( blank=True,null=True )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='post',blank=True,null=True)
    view_count = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            kwargs={
                "category_slug":self.category.slug,
                "post_slug":self.slug,
                
            }
        )
   
