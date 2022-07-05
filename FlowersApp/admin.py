from django.contrib import admin
from .models import Flower, FlowerCategory, Garden, Question, Answer, Reminder, Video


# Register your models here.

class FlowerAdmin(admin.ModelAdmin):
    list_display = ("name", "height", "category")
    list_filter = ("category",)


admin.site.register(Flower, FlowerAdmin)


class FlowerCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(FlowerCategory, FlowerCategoryAdmin)


class GardenAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.user:
            return True
        return False


admin.site.register(Garden, GardenAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Video, VideoAdmin)


class ReminderAdmin(admin.ModelAdmin):
    list_display = ("description",)


admin.site.register(Reminder, ReminderAdmin)


class QuestionAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.creator:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.creator:
            return True
        return False


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.creator:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.creator:
            return True
        return False


admin.site.register(Answer, AnswerAdmin)



