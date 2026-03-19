from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']     # отображение полей модели
    list_filter = ['status', 'created', 'publish', 'author']    # Боковая панель фильтрации
    search_fields = ['title', 'body']   # Поиск по полям
    prepopulated_fields = {'slug': ('title',)} # Автозаполнение слага по заголовку
    raw_id_fields = ['author']  # Отображение поля автора поисковым виджетом при добавлении записи
    date_hierarchy = 'publish'  # Навигация по дате
    ordering = ['status', 'publish'] # Соритровка по умолчанию
