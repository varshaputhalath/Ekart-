from django import forms


class OrderUpdateForm(forms.Form):
    options=(
        ('dispatched','dispatched'),
        ('out_of_stock','out_of_stock'),
        ('delivered','delivered'),
    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":'form-control'}))
    exp_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))

   