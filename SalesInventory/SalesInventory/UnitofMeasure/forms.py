from  django import forms
from .models import UnitofMeasure,UnitofMeasureDetails
from parsley.decorators import parsleyfy
# from parsley.decorators import parsleyfy
from django.forms  import ModelForm

@parsleyfy
class UnitofMeasureForm(ModelForm):    
    class Meta:
        model = UnitofMeasure
        labels = {
            'unitbasisname': 'Unit Basis Name : ',
            'uom_name': 'UOM Name  : ',
            'uom_shortname': 'Uom Short Name : ',
            'IsActive':'Status : '
        }
        fields = ['unitbasisname','uom_name','uom_shortname','IsActive','CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate' ]        
        exclude = ('CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate')
        widgets = {
            'unitbasisname': forms.Select(),
            'uom_name': forms.TextInput(),
            'uom_shortname': forms.TextInput(),
            'IsActive': forms.CheckboxInput(),            
        }
        parsley_extras = {
            "unitbasisname": {
                "required-message": "Unit Basis Name Required",
            } ,
            "uom_name": {
                "required-message": "Uom Name Required",
            }  
             ,
            "uom_shortname": {
                "required-message": "Uom Short Name Required",
            }           
        }
    def __init__(self, *args, **kwargs):
        super(UnitofMeasureForm, self).__init__(*args, **kwargs)
        self.fields['unitbasisname'].widget.attrs['class'] = 'form-control select2 unitbasisname'
        self.fields['uom_name'].widget.attrs['class'] = 'form-control uom_name'
        self.fields['uom_shortname'].widget.attrs['class'] = 'form-control uom_shortname'
        self.fields['IsActive'].widget.attrs['class'] = 'iCheck IsActive'
            


@parsleyfy
class UnitofMeasureDetailsForm(ModelForm):
    
    class Meta:
        model = UnitofMeasureDetails
        labels = {
            'uomdetails_name': 'UOM Name',
            'uomdetails_shortname': 'UOM Short Name',
            # 'isbaseuom':'Base UOM',
            'convertionvalue':'Conversion Value',
        }
        fields = ['uomid','uomdetails_name','uomdetails_shortname','convertionvalue','isbaseuom','CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate' ]
        exclude = ('CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate')
        widgets = {
            'uomid': forms.HiddenInput(),
            'uomdetails_name': forms.TextInput(),
            'uomdetails_shortname': forms.TextInput(),
            #'isbaseuom': forms.RadioSelect(),       
            'convertionvalue': forms.TextInput(),     
        }
        parsley_extras = {
            "uomdetails_name": {
                "required-message": "UOM Details  Name Required",
            },
             "convertionvalue": {
                "required-message": "UOM Convertion Value Required",
            }  
        }
    def __init__(self, *args, **kwargs):
        super(UnitofMeasureDetailsForm, self).__init__(*args, **kwargs)
        self.fields['uomid'].widget.attrs['class'] = 'uomid'        
        self.fields['uomdetails_name'].widget.attrs['class'] = 'form-control uomdetails_name'
        self.fields['uomdetails_shortname'].widget.attrs['class'] = 'form-control uomdetails_shortname'
        self.fields['convertionvalue'].widget.attrs['class'] = 'form-control convertionvalue'
        self.fields['isbaseuom'].widget.attrs['class'] = 'iCheck isbaseuom'
        

    
    

