from django.db import models
from django.utils import timezone


class TeacherCard(models.Model):
    """Карточка преподавателя на главную страницу"""
    name = models.CharField(verbose_name='Ф.И.О.', max_length=100,  blank=True, null=True)
    resume = models.TextField(verbose_name='Краткое резюме учителя для главной страницы', blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото на главную страницу', blank=True, null=True)


class ForParents(models.Model):
    """Полезная информация для родителей"""
    title = models.CharField(verbose_name='Тема информации', max_length=100, blank=True, null=True)
    text = models.TextField(verbose_name='Информация для родителей', blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото для родителей', blank=True, null=True)
    link = models.CharField(verbose_name='Ссыдка на источник', max_length=100, blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-pub_date"]


class ForStudents(models.Model):
    """Полезная информация для родителей"""
    title = models.CharField(verbose_name='Тема информации', max_length=100, blank=True, null=True)
    text = models.TextField(verbose_name='Информация для учеников', blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото для учеников', blank=True, null=True)
    link = models.CharField(verbose_name='Ссыдка на источник', max_length=100, blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-pub_date"]


class Methodically(models.Model):
    """Методические разработки учителя"""
    title = models.CharField(verbose_name='Тема информации', max_length=100, blank=True, null=True)
    text = models.TextField(verbose_name='Описание разработки', blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото', blank=True, null=True)
    link = models.CharField(verbose_name='Ссыдка на источник', max_length=100, blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-pub_date"]


class HelpfulInformation(models.Model):
    title = models.CharField(verbose_name='Описание источника', max_length=100, blank=True, null=True)
    link = models.CharField(verbose_name='Ссыдка на источник', max_length=100, blank=True, null=True)
