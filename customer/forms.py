from django import forms
from .models import Feedback, UploadedFile


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comments']

    name = forms.CharField(max_length=100, label='Your Name', required=True)
    email = forms.EmailField(label='Your Email', required=True)
    rating = forms.IntegerField(
        label='Rate your experience (1-5)',
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'type': 'range'}),
        required=True
    )
    comments = forms.CharField(
        label='Additional Comments',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True
    )


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)