from django import forms
from .models import Image
from django.core.exceptions import ValidationError

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

    # Add the 'form-control' class to the title field and 'form-control-file' for the image field
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False  # Make the title field not required
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )

