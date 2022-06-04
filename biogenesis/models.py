from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings

class Vid(models.Model):
    #Вид существа
    name = models.CharField("Вид", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique = True )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"


class Book(models.Model):
    #Книги
    name = models.CharField("Название книги", max_length=150)
    url = models.SlugField(max_length=160, unique = True )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Family(models.Model):
    #Семейство существа
    name = models.CharField("Семейство", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique = True )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Семейство"
        verbose_name_plural = "Семейство"

class Entity(models.Model):
    #Существа
    title = models.CharField("Название", max_length=150)
    description = RichTextField("Описание")
    text_preview = models.CharField("Краткое описание", max_length=150)
    poster = models.ImageField("Постер", upload_to="entitys/", null = True)
    vid = models.ForeignKey(Vid, verbose_name="Вид", on_delete = models.SET_NULL, null = True)
    family = models.ForeignKey(Family, verbose_name="Семейство", on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete = models.CASCADE, null=True,  blank=True)

    def get_absolute_url(self):
        return reverse("entity_detail", kwargs={"slug": self.url})


    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Существо"
        verbose_name_plural = "Существа"



class Reviews(models.Model):
    #Отзывы
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length= 5000)
    parent = models.ForeignKey('self',  verbose_name="Родитель", on_delete = models.SET_NULL, blank= True, null = True )
    entity = models.ForeignKey(Entity, verbose_name="Существо", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.entity}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

