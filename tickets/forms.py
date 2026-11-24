
from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Өтінім тақырыбын енгізіңіз'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Мәселені сипаттаңыз',
                'rows': 4
            }),

            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'title': 'Тақырып',
            'description': 'Сипаттама',
            'priority': 'Басымдық',
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title.strip()) < 5:
            raise forms.ValidationError(
                'Тақырып кемінде 5 таңбадан тұруы керек!'
            )

        return title
