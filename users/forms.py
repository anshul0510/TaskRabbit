from django import forms
from .models import UserImage , UserProfile, Task


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # Max size 5 MB
                raise forms.ValidationError("File size exceeds 5 MB.")
            
            # Corrected method name
            if not image.content_type.startswith('image/'):
                raise forms.ValidationError("File is not an image.")
            
        return image

    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']

    def clean_profile_picture(self):
        picture = self.cleaned_data.get('profile_picture')
        
        if picture:
            file = self.files.get('profile_picture')
            if file and not file.content_type.startswith('image/'):
                raise forms.ValidationError("File is not an image.")
            
            if picture.size > 5 * 1024 * 1024:  # Max size 5 MB
                raise forms.ValidationError("Profile picture size exceeds 5 MB.")
        
        return picture

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }