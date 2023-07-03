from django import forms

class DateFilterForm(forms.Form):
    start_date = forms.DateField(
        label='Fecha de inicio', 
        widget=forms.DateInput(attrs={'type': 'date'}),
        error_messages={'required': 'Este campo es obligatorio'}
    )
    end_date = forms.DateField(
        label='Fecha de fin', 
        widget=forms.DateInput(attrs={'type': 'date'}),
        error_messages={'required': 'Este campo es obligatorio'}
    )

    def __init__(self, *args, **kwargs):
        super(DateFilterForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(DateFilterForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError('La fecha de inicio no debe ser mayor que la fecha de fin')
        return cleaned_data