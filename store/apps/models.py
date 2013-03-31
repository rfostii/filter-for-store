from django.db import models
from django.contrib import admin

class Item(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    mark = models.ForeignKey('Mark', verbose_name='Mark')
    cathegorie = models.ForeignKey('Cathegorie', verbose_name='Cathegorie')
    price = models.FloatField(verbose_name='Price')
    availability = models.BooleanField(verbose_name='Availability')
    description = models.TextField(verbose_name='Description')
    rating = models.IntegerField(verbose_name='Rating', max_length=1)
    accessorie = models.ManyToManyField('Accessories', verbose_name='Accessories', blank=True)
    feature = models.ForeignKey('Feature', verbose_name='Feature')
    picture = models.ManyToManyField('Picture', verbose_name='Picture')
    review = models.ForeignKey('Review', verbose_name='Review', blank=True)

    def __unicode__(self):
        return self.name

class Mark(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Cathegorie(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    body = models.TextField(verbose_name='Body')
    item = models.ForeignKey(Item, verbose_name='Item')

    def __unicode__(self):
        return self.name


class Picture(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    path = models.FileField(verbose_name='Path', upload_to='img')

    def __unicode__(self):
        return self.name


class Feature(models.Model):
    short_description = models.TextField()
    diagonal = models.FloatField()
    resolution = models.CharField(max_length=10)
    view = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    proccesor = models.CharField(max_length=100)
    hdd = models.IntegerField()
    cores = models.IntegerField()

    def __unicode__(self):
        return self.short_description


class Accessories(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    picture = models.ManyToManyField('Picture', verbose_name='Picture')
    items = models.ManyToManyField('Item', verbose_name='Item')

    def __unicode__(self):
        return self.name


class Review(models.Model):
    name = models.URLField(verbose_name='Name')

    def __unicode__(self):
        return self.name


class View_Item(admin.ModelAdmin):
    list_display = ('name',
                    'cathegorie',
                    'price',
                    'availability',
                    'description',
                    'rating'
    )

class View_Cathegorie(admin.ModelAdmin):
    list_display = ('name',)


class View_Comment(admin.ModelAdmin):
    list_display = ('name', 'body')


class View_Picture(admin.ModelAdmin):
    list_display = ('name',
                    'path'
    )


class View_Feature(admin.ModelAdmin):
    list_display = ('short_description',
                    'diagonal',
                    'resolution',
                    'view',
                    'os',
                    'proccesor',
                    'hdd',
                    'cores'
    )


class View_Accessories(admin.ModelAdmin):
    list_display = ('name',)


class View_Review(admin.ModelAdmin):
    list_display = ('name',)

class View_Mark(admin.ModelAdmin):
    list_display = ('name',)


try:
    admin.site.register(Item, View_Item)
    admin.site.register(Cathegorie, View_Cathegorie)
    admin.site.register(Comment, View_Comment)
    admin.site.register(Picture, View_Picture)
    admin.site.register(Feature, View_Feature)
    admin.site.register(Review, View_Review)
    admin.site.register(Accessories, View_Accessories)
    admin.site.register(Mark, View_Mark)
except Exception:
    pass