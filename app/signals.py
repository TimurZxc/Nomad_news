import os
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import *

@receiver(post_delete, sender=News)
def auto_delete_files_on_delete_news(sender, instance, **kwargs):
    # Delete image file only if it's not the default image
    default_image = 'default_images/default_news.png'
    if instance.image and instance.image.name != default_image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)

@receiver(post_delete, sender=NewsFile)
def auto_delete_file_on_delete_newsfile(sender, instance, **kwargs):
    # Delete the file for NewsFile when its instance is deleted
    if instance.file:
        file_path = instance.file.path
        if os.path.isfile(file_path):
            os.remove(file_path)

@receiver(post_delete, sender=Participant)
def auto_delete_files_on_delete_participant(sender, instance, **kwargs):
    # Delete image file only if it's not the default image
    default_image = 'default_images/default_participant.png'
    if instance.image and instance.image.name != default_image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)

@receiver(post_delete, sender=Event)
def auto_delete_files_on_delete_event(sender, instance, **kwargs):
    # Delete image file only if it's not the default image
    default_image = 'default_images/default_event.png'
    if instance.image_preview and instance.image_preview.name != default_image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)

@receiver(post_delete, sender=EventImage)
def auto_delete_files_on_delete_event_image(sender, instance, **kwargs):
    # Delete the event image file when the EventImage instance is deleted
    default_image = 'default_images/default_event.png'
    if instance.image and instance.image.name != default_image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)

@receiver(post_delete, sender=EventVideo)
def auto_delete_files_on_delete_event_video(sender, instance, **kwargs):
    # Delete the event video file when the EventVideo instance is deleted
    default_image = 'default_images/default_event.png'
    if instance.preview and instance.preview.name != default_image:
        video_path = instance.preview.path
        if os.path.isfile(video_path):
            os.remove(video_path)
