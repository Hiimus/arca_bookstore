from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review, RATING_CHOICES


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    img_paths = forms.ImageField(
        label='Image', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'


class ReviewForm(forms.ModelForm):
    rating: forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Review
        fields = ('review', 'rating',)

        widgets = {
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 100%;'}),
        }
