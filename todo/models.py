from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User


class TodoTag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = "title",unique = True,)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse(
    #         "tag_view",
    #         kwargs={
    #             "tag_slug":self.slug,  
    #         }
    #     )    


class TodoCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = "title",unique = True,)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse(
    #         "category_detail",
    #         kwargs={
    #             "category_slug":self.slug
    #         }
    #     )

class Todo(models.Model):
    tag = models.ManyToManyField(TodoTag)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(TodoCategory,on_delete=models.SET_NULL,null=True)
    title = models.CharField( max_length=200 )
    content = models.TextField( blank=True,null=True )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    # def get_absolute_url(self):
    #     return reverse(
    #         "todo_detail",
    #         kwargs={
    #             "category_slug":self.category.slug,
    #             "id":self.pk
    #         }
    #     )