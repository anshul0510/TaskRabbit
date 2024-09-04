from django import forms
from .models import UserImage , UserProfile


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:

            if image.size>5*1024*1024:
                raise forms.ValidationError("file size exceeds 5 mb")
            
            if not image.content_type.startwith('image/'):
                raise forms.ValidationError("file is not an image")
            
        return image
    

class UserProfileFOrm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['prodile_picture','bio']

    def clean_profile_picture(self):
        picture = self.cleaned_data.get('prodile_picture')
        if picture:

            if picture.size>5*1024*1024:
                raise forms.ValidationError("file size exceeds 5 mb")
            
            if not picture.content_type.startwith('image/'):
                raise forms.ValidationError("file is not an image")
            
        return picture
