from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}  # Заполнение поля slug данными из поля title
    raw_id_fields = ['author']  # Создание виджета для отбора ассоциированных объектов для поля author
    date_hierarchy = 'publish'  # Навигационные ссылки
    ordering = ['status', 'publish']