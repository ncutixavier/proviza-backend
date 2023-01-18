from django.contrib import admin
from . import models

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'category', 'is_active',
                    'created_at', 'updated_at')

admin.site.register(models.Question, QuestionAdmin)