from django import forms
from .models import Flower, Garden


class GardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        exclude = {"user", }


class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        exclude = {"height", }
