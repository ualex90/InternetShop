from django import forms
from django.forms import CheckboxInput

from catalog.models import Product, ProductVersion

FORBIDDEN_LIST = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'бесплатно',
            'полиция',
            'радар',
        ]


class StyleFrmMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFrmMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'price', 'image',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data.lower() in FORBIDDEN_LIST:
            raise forms.ValidationError(f'Наименование не должно содержать следующие слова: '
                                        f'{", ".join(FORBIDDEN_LIST)}')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if cleaned_data.lower() in FORBIDDEN_LIST:
            raise forms.ValidationError(f'Описание не должно содержать следующие слова: '
                                        f'{", ".join(FORBIDDEN_LIST)}')
        return cleaned_data


class ProductVersionForm(StyleFrmMixin, forms.ModelForm):

    class Meta:
        model = ProductVersion
        fields = '__all__'
