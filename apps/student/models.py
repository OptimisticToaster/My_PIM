from django.db import models


class Assignment(models.Model):
    assignment_category = models.ForeignKey('Assignment_Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_assigned = models.DateField(null=True, blank=True)
    date_due = models.DateField(null=True, blank=True)
    date_submitted = models.DateField(null=True, blank=True)
    date_cleared = models.DateField(null=True, blank=True)
    total_points = models.FloatField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Assignment_Category(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    weighting = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    instructor = models.ForeignKey('Staff', on_delete=models.CASCADE)
    school_year = models.CharField(max_length=9, help_text = 'YYYY-YYYY')
    term = models.CharField(max_length=200, help_text = 'Q3, S2, B9')
    name = models.CharField(max_length=200)
    course_number = models.CharField(max_length=40, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


school_levels = (
    ('Preschool', 'Preeschool'),
    ('Elementary', 'Elementary School'),
    ('Middle', 'Middle School'),
    ('High', 'High School'),
    ('College', 'College')
)

class School(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(choices=school_levels, max_length=100)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=20, blank=True, help_text = 'Abbreviation')
    postal_code = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


roles = (
    ('Administrator', 'Administrator'),
    ('Counselor', 'Counselor'),
    ('Instructor', 'Instructor')
)

class Staff(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    roles = models.CharField(choices=roles, max_length=100)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
