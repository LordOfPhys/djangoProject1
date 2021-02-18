from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'user')
    first_name = models.CharField(max_length=30, default='Имя')
    last_name = models.CharField(max_length=30, default='Фамилия')
    adress = models.CharField(max_length=100, default='Адрес')
    photo = models.ImageField(upload_to='people_photos/', default='user_icon.png')
    rating = models.FloatField(default='5.0')
    about = models.CharField(max_length=10000, default='О себе')
    tegs = models.CharField(max_length=1000, default='Стили')
    hello_word = models.CharField(max_length=2000, default='Приветственное слово')

    def get_user(self):
        return self.user

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, f_name):
        self.first_name = f_name
        self.save()

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, l_name):
        self.last_name = l_name
        self.save()

    def get_adress(self):
        return self.adress

    def set_adres(self, adress):
        self.adress = adress
        self.save()

    def get_photo(self):
        return self.photo

    def set_photo(self, photo):
        self.photo = photo
        self.save()

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating
        self.save()

    def get_about(self):
        return self.about

    def set_about(self, about):
        self.about = about
        self.save()

    def get_tegs(self):
        return self.tegs

    def set_tegs(self, tegs):
        self.tegs = tegs
        self.save()

class WorkPlace(models.Model):
    up = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    adress = models.CharField(max_length=200, default='адрес студии')
    description = models.CharField(max_length=1000, default='как добраться')

class WorkPlaceImage(models.Model):
    wp = models.ForeignKey(WorkPlace, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='WorkPlaceImage/')

class VideoUrl(models.Model):
    up = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)

class ResponseForMaster(models.Model):
    upmaster = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='master')
    upuser = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='commentator')
    text = models.CharField(max_length=1000, default='отзыв')
    image = models.ImageField(upload_to='response_for_master_image/', blank=True)
    score = models.FloatField(default='5.0')

class Sketch(models.Model):
    UserProfile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default='0')
    coments = models.ImageField(default='0')
    label = models.CharField(max_length=100, default='Название товара', unique=True)
    image = models.ImageField(upload_to='item_image/', default='')

    def __str__(self):
        return self.label

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label
        self.save()

    def get_user(self):
        return self.user

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image
        self.save()

    def get_likes(self):
        return self.likes

    def set_likes(self, likes):
        self.likes = likes
        self.save()

    def get_coments(self):
        return self.coments

    def set_coments(self, coments):
        self.coments = coments
        self.save()

class LikeScketch(models.Model):
    up = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    sketch = models.ForeignKey(Sketch, on_delete=models.CASCADE)

class CommentSketch(models.Model):
    up = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    sketch = models.ForeignKey(Sketch, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.CharField(max_length=1000, default='Комментарий')

class LikeCommentSketch(models.Model):
    up = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    commentSketch = models.ForeignKey(CommentSketch, on_delete=models.CASCADE)
