from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['nombre', 'descripcion', 'precio', 'consolas', 'stock', 'imagen', 'url_imagen']

    def clean(self):
        cleaned_data = super().clean()
        imagen = cleaned_data.get("imagen")
        url_imagen = cleaned_data.get("url_imagen")

        if not imagen and not url_imagen:
            raise forms.ValidationError('Debe proporcionar una imagen o una URL de la imagen.')

        return cleaned_data