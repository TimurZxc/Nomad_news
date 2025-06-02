from django.contrib import admin
from .models import Result, ResultAttachment, Event, News, Participant, EventImage, EventVideo, NewsFile

# Inline для вложений результата
class ResultAttachmentInline(admin.TabularInline):
    model = ResultAttachment
    extra = 1  # количество пустых форм

# Админ для Result с отображением вложений
class ResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    inlines = [ResultAttachmentInline]

    # Если нужно переопределить удаление
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

# Существующие админы для других моделей
@admin.action(description="Установить изображение по умолчанию")
def set_image(modeladmin, request, queryset):
    queryset.update(image="default_images/default_news.png")

@admin.action(description="Установить изображение по умолчанию")
def set_preview(modeladmin, request, queryset):
    queryset.update(preview="default_images/default_event.png")

class NewsFileInline(admin.TabularInline):
    model = NewsFile
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    actions = [set_image]
    list_display = ('title', 'created_at', 'updated_at')
    inlines = [NewsFileInline]

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1

class EventVideoInline(admin.TabularInline):
    model = EventVideo
    extra = 1

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    inlines = [EventImageInline, EventVideoInline]

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'pos_index')

# Регистрация всех админов
admin.site.register(Result, ResultAdmin)
admin.site.register(ResultAttachment)  # можно не регистрировать, если достаточно inline
admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(EventImage)
admin.site.register(EventVideo)
