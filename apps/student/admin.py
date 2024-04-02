from django.contrib import admin

from apps.student.models import Assignment, Assignment_Category, Course, School, Staff

# from apps.student.models import School

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Assignment_Category)
class Assignment_CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Assignment)

# admin.site.register(Assignment_Category)

# admin.site.register(Course)

# admin.site.register(School)

# admin.site.register(Staff)
