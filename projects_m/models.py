from django.db import models
from django.utils import timezone

class User(models.Model):
    POSITION_CHOICES = [
        ('ceo', 'CEO'),
        ('cto', 'CTO'),
        ('designer', 'Designer'),
        ('programmer', 'Programmer'),
        ('product_owner', 'Product Owner'),
        ('project_owner', 'Project Owner'),
        ('project_manager', 'Project Manager'),
        ('qa', 'QA'),
    ]

    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=75, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    position = models.CharField(max_length=30, choices=POSITION_CHOICES, default='programmer')

    def __str__(self):
        return self.email

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='project_files/', blank=True, null=True)  # Поле для файлов

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('backlog', 'Backlog'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='backlog')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')  # Ссылка на Project
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['priority']),
            models.Index(fields=['created_at']),
        ]

class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)  # Ссылка на Project

    def __str__(self):
        return self.title
