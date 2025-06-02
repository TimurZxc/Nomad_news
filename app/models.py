from django.db import models
from datetime import datetime
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field
from urllib.parse import urlparse, parse_qs
import os

def extract_youtube_id(url):
    """Extract the YouTube video ID from a URL."""
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if hostname in ['youtu.be']:
        # Short URL format: youtu.be/VIDEO_ID
        return parsed_url.path[1:]
    if hostname in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch':
            # URL format: youtube.com/watch?v=VIDEO_ID
            query_params = parse_qs(parsed_url.query)
            return query_params.get('v', [None])[0]
        elif parsed_url.path.startswith('/embed/'):
            # URL format: youtube.com/embed/VIDEO_ID
            return parsed_url.path.split('/')[2]
        elif parsed_url.path.startswith('/v/'):
            # URL format: youtube.com/v/VIDEO_ID
            return parsed_url.path.split('/')[2]
    return None

class News(models.Model):
    title = models.CharField(max_length=255)
    text = CKEditor5Field()
    image = models.ImageField(upload_to='news_images/', default='default_images/default_news.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_for_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title 

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class NewsFile(models.Model):
    news = models.ForeignKey(News, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='news_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.news.title} - File"

class Participant(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    work_place = models.CharField(max_length=255)
    description = CKEditor5Field()
    image = models.ImageField(upload_to='participants_images/', default='default_images/default_participant.png')
    pos_index = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.full_name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = CKEditor5Field(null=True, blank=True)
    tasks = CKEditor5Field(null=True, blank=True)
    participants = CKEditor5Field(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_preview =  models.ImageField(upload_to='event_images/', default='default_images/default_event.png', blank=True, null=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.event.name} Image"

class EventVideo(models.Model):
    event = models.ForeignKey(Event, related_name='videos', on_delete=models.CASCADE)
    preview =  models.ImageField(upload_to='video_previews/', default='default_images/default_event.png')
    video_url = models.URLField()
    video_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f"{self.event.name} Video"
    
    def save(self, *args, **kwargs):
        # Automatically extract and set video_id if video_url is provided
        if self.video_url:
            self.video_id = extract_youtube_id(self.video_url)
        super().save(*args, **kwargs)

class Result(models.Model):
    name = models.CharField(max_length=255)
    description = CKEditor5Field(null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return self.name
    
class ResultAttachment(models.Model):
    result = models.ForeignKey(
        Result,
        on_delete=models.CASCADE,
        related_name='attachments'
    )
    file = models.FileField(
        upload_to='results/result_attachments/%Y/%m/%d/',
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вложение результатов'
        verbose_name_plural = 'Вложения результатов'

    def __str__(self):
        return f"{self.file.name}"