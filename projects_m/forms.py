from django import forms
from .models import Document, Project

def validate_file_size(value):
    limit_mb = 5  # Лимит размера файла в мегабайтах
    limit = limit_mb * 1024 * 1024  # Преобразуем мегабайты в байты
    if value.size > limit:
        raise forms.ValidationError(f'File size exceeds {limit_mb} MB.')

class DocumentForm(forms.ModelForm):
    file = forms.FileField(validators=[validate_file_size])

    class Meta:
        model = Document
        fields = ['title', 'file']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'file']  # Поля формы

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'title']
