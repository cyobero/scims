from django import forms
from products.models import Product, Flower, PreRoll, Edible, Vape, Resin


class NewProductForm(forms.ModelForm): 

    def __init__(self, *args, **kwargs):
        super(NewProductForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Product
        fields = fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class NewFlowerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewFlowerForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = Flower
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),

        }


class NewPreRollForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewPreRollForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = PreRoll
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),

        }


class NewEdibleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewEdibleForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = Edible
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),

        }


class NewVapeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewVapeForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = Vape
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),
        }


class NewResinForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewResinForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = Resin
        fields = fields = '__all__'
        widgets = {
            'final_test_date': DateInput(),
            'harvest_date': DateInput(),
            'package_date': DateInput(),
        }
