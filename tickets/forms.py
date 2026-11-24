from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "priority"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Мысалы: Компьютер қосылмайды"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Мәселені сипаттаңыз"}),
            "priority": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 5:
            raise forms.ValidationError("Тақырып кемінде 5 таңбадан тұруы керек.")
        return title
