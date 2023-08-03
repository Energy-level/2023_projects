from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
    #for specifying placeholder for the position field
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"
        #for ingoring the validation of the particular field
        self.fields['emp_code'].required=False
