from django import forms
from products.models import Product, Flower, PreRoll, Edible, Vape, Resin


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class NewFlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),

        }


class NewPreRollForm(forms.ModelForm):
    class Meta:
        model = PreRoll
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),

        }


class NewEdibleForm(forms.ModelForm):
    class Meta:
        model = Edible
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),

        }


class NewVapeForm(forms.ModelForm):
    class Meta:
        model = Vape
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),
        }


class NewResinForm(forms.ModelForm):
    class Meta:
        model = Resin
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),
        }
