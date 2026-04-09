from django import forms
from slugify import slugify
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'slug', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 rounded-lg border border-stone-200 bg-white text-stone-800 '
                         'placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-stone-400 '
                         'focus:border-transparent transition text-sm font-medium',
                'placeholder': 'Page title...',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 rounded-lg border border-stone-200 bg-white text-stone-800 '
                         'placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-stone-400 '
                         'focus:border-transparent transition text-sm font-mono',
                'placeholder': 'auto-generated-from-title',
            }),
            'status': forms.Select(attrs={
                'class': 'px-4 py-2.5 rounded-lg border border-stone-200 bg-white text-stone-800 '
                         'focus:outline-none focus:ring-2 focus:ring-stone-400 '
                         'focus:border-transparent transition text-sm',
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full',
                'id': 'markdown-editor',
                'rows': 20,
            }),
        }

    def clean_slug(self):
        slug = self.cleaned_data.get('slug', '')
        title = self.cleaned_data.get('title', '')
        if not slug:
            slug = slugify(title)
        else:
            slug = slugify(slug)
        return slug


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-stone-200 bg-white text-stone-800 '
                     'placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-stone-600 '
                     'focus:border-transparent transition text-sm',
            'placeholder': 'Username',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-stone-200 bg-white text-stone-800 '
                     'placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-stone-600 '
                     'focus:border-transparent transition text-sm',
            'placeholder': 'Password',
        })
    )
