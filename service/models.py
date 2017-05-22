# ~*~ coding: utf-8 ~*~

from __future__ import unicode_literals

from django.db import models

from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    img = models.ImageField(upload_to='img/category/',null=True)
    date = models.DateTimeField(auto_now=True,null=True)
    shows = models.IntegerField(default=0)
    # как строки выводился вместо этого его title
    def __unicode__(self):
        return self.name;

class CategorySubcategory(models.Model):
    category = models.ForeignKey(Category, related_name='category')
    subcategory = models.ForeignKey(Category, related_name='subcategory')






class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','date','shows')

class CategorySubcategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id','subcategory_id')


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategorySubcategory, CategorySubcategoryAdmin)

