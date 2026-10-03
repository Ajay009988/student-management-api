# from django.contrib import admin
# from .models import Student

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'roll_no', 'course', 'year', 'owner', 'email')
#     list_filter = ('course', 'year')
#     search_fields = ('name', 'roll_no')



from django.contrib import admin
from .models import Student
from django.utils.html import mark_safe

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'course', 'year', 'owner', 'email', 'photo_preview')
    list_filter = ('course', 'year')
    search_fields = ('name', 'roll_no')

    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" style="object-fit:cover; border-radius:50%" />')
        return "No Photo"
    photo_preview.short_description = "Photo"