from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

class Page(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = "title",unique = True,)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='cover')
    content = HTMLField( blank=True,null=True )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse(
            "page:page_view",
            kwargs={
                "page_slug":self.slug
            }
        )
