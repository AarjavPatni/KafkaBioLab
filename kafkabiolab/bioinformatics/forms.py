from django import forms
from .models import Sequence


class SequenceForm(forms.ModelForm):
    class Meta:
        model = Sequence
        fields = ["input_sequence", "operation"]
        labels = {
            "input_sequence": "Input Sequence",
            "operation": "Operation",
        }
