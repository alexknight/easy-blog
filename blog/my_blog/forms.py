from django import forms
from .models import BlogPost

class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost

    def _media(self):
	js = []
        return forms.Media(js=js)

    media = property(_media)
