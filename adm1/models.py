from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from tinymce.models import HTMLField

# from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # text = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # picture = models.ImageField(upload_to = 'Fisher/app/img', default = 'Fisher/app/img/template.jpg')    
    # link1 = HTMLField()
    # link2 = HTMLField()
    # link3 = HTMLField()
    # link4 = HTMLField()
    # link5 = HTMLField()
    # namelink1 = HTMLField()
    # namelink2 = HTMLField()
    # namelink3 = HTMLField()
    # namelink4 = HTMLField()
    content = HTMLField(default='', verbose_name='Контент')
    # namelink5 = RichTextUploadingField(config_name='awesome_ckeditor')
    # namelink25 = RichTextUploadingField(config_name='default')
    # namelink5 = RichTextUploadingField()
    # content11 = RichTextField(config_name='awesome_ckeditor')
    # content32 = RichTextField(config_name='default')
    # content42 = RichTextField(blank=True, verbose_name='Описание', default='')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class VideoPost(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', default = 'Fisher/app/img/template.jpg', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)


class Header(models.Model):
    # namelink55 = RichTextUploadingField()
    # content422 = RichTextField(default='')
    # widget = CKEditorWidget(config_name='awesome_ckeditor')
    daily_schedule = HTMLField()
    mail = HTMLField()
    phone = HTMLField()
    delivery = HTMLField()
    link_to_insta = HTMLField()
    link_to_facebook = HTMLField()
    link_to_vk = HTMLField()
    rent_rules = HTMLField()
    main_letter = HTMLField()
    logo34x46 = models.ImageField(upload_to = 'Fisher/app/img', default = 'Fisher/app/img/logo.jpg')
    


class Slider(models.Model):
    picture1 = models.ImageField(upload_to = 'Fisher/app/img', default = 'Fisher/app/img/template.jpg')
    picture2 = models.ImageField(upload_to = 'Fisher/app/img', default = 'Fisher/app/img/bgHome3.jpg')
    picture3 = models.ImageField(upload_to = 'Fisher/app/img', default = 'Fisher/app/img/bgHome2.jpg')
    headline1 = HTMLField()
    headline2 = HTMLField()
    headline3 = HTMLField()
    link1 = HTMLField()
    link2 = HTMLField()
    link3 = HTMLField()


class Thebigthree(models.Model):
    title = HTMLField()
    color = HTMLField()
    picture = models.ImageField(upload_to = 'Fisher/app/img/banners', default = 'Fisher/app/img/banners/banner3.png')


class Leaders(models.Model):
    button_name =  HTMLField()
    leaders_of_sale = HTMLField()
    picture_12x16 = models.ImageField(upload_to = 'Fisher/app/img/icons', default = 'Fisher/app/img/icons/logo.png')
    button_left_text = HTMLField()
    button_right_text = HTMLField()  


class LeadersStaff(models.Model):
    add_text_in_frame = HTMLField()
    color_of_frame = HTMLField()
    picture_600x434 = models.ImageField(upload_to = 'Fisher/app/img/items', default = 'Fisher/app/img/items/udilische_600x434.jpg')
    name = HTMLField()
    stars = HTMLField()
    new_price = HTMLField()
    old_price = HTMLField()


class SecondSlider(models.Model):
    title = HTMLField()
    stars = HTMLField()
    new_price = HTMLField()
    old_price = HTMLField()
    description = HTMLField()
    picture_600x600 = models.ImageField(upload_to = 'Fisher/app/img/items', default = 'Fisher/app/img/items/udilische_600x434.jpg')


class Hire(models.Model):
    title = HTMLField()
    picture_12x16 = models.ImageField(upload_to = 'Fisher/app/img/icons', default = 'Fisher/app/img/icons/logo.png')
    button_text = HTMLField()


class HireStaff(models.Model):
    add_text_in_frame = HTMLField()
    color_of_frame = HTMLField()
    picture_600x434 = models.ImageField(upload_to = 'Fisher/app/img/items', default = 'Fisher/app/img/items/udilische_600x434.jpg')
    name = HTMLField()
    stars = HTMLField()
    new_price = HTMLField()
    old_price = HTMLField()


class TheLastThree(models.Model):
    title = HTMLField()
    text = HTMLField()
    picture = models.ImageField(upload_to = 'Fisher/app/img/icons', default = 'Fisher/app/img/icons/freeShipping.png')
   

class Footer(models.Model):
    logo34x46 = models.ImageField(upload_to = 'Fisher/app/img', default = 'Fisher/app/img/logo.jpg')
    link_to_insta = HTMLField()
    link_to_facebook = HTMLField()
    link_to_vk = HTMLField()
    main_letter = HTMLField()
    description = HTMLField()
    copyrightt = HTMLField()


class Rent(models.Model):
    category = HTMLField()
    add_text_in_frame = HTMLField()
    color_of_frame = HTMLField()
    stars = HTMLField()
    rent_price = HTMLField()
    picture_600x600 = models.ImageField(upload_to = 'Fisher/app/img/items', default = 'Fisher/app/img/items/118ee07b6b6471b0a5e587d09985e6ad.jpg')


class Contacts(models.Model):
    location = HTMLField()
    number = HTMLField()
    email = HTMLField()
    address = HTMLField()
    

class ModelClass(models.Model):
    ## content = HTMLField()
    content = RichTextUploadingField()