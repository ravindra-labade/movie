from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

        widgets = {
            "movie_name": forms.TextInput(attrs={'class': 'form-control'}),
            "director": forms.TextInput(attrs={'class': 'form-control'}),
            "lead_actor": forms.TextInput(attrs={'class': 'form-control'}),
            "lead_actress": forms.TextInput(attrs={'class': 'form-control'}),
            "ticket_fare": forms.NumberInput(attrs={'class': 'form-control'}),
            "payment_mode": forms.Select(attrs={'class': 'form-control'}),
        }
