from  django import forms
from .models import ItemCategory,ItemGroup
from parsley.decorators import parsleyfy
from django.forms  import ModelForm

@parsleyfy
class ItemCategoryForm(ModelForm):    
    class Meta:
        model = ItemCategory
        
        labels = {
            'itemcategory_title': 'Title : ',
            'itemcategory_title_bangla': 'Title (Bangla) : ',
            'itemcategory_code': 'Code : ',
            'IsActive':'Status : ',
            'ItemGroup': 'Group Name : '           
        }
        fields = ['ItemGroup','itemcategory_title','itemcategory_title_bangla','itemcategory_code','IsActive','CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate' ]
        exclude = ('CreatedBy','CreatedDate','UpdatedBy','UpdatedDate','DeletedBy','DeletedDate')
        widgets = {
            'itemcategory_title': forms.TextInput(),
            'itemcategory_title_bangla': forms.TextInput(),
            'itemcategory_code': forms.TextInput(),
            'IsActive': forms.CheckboxInput(),
            'ItemGroup':forms.Select()            
        }
        parsley_extras = {
            "itemcategory_title": {
                "required-message": "Item Category Title Required",
            },
            "ItemGroup":{
                "required-message":"Group Name Required"
            }
        }
    def __init__(self, *args, **kwargs):
        super(ItemCategoryForm, self).__init__(*args, **kwargs)
        self.fields['ItemGroup'].widget.attrs['class'] = 'form-control select2'
        self.fields["ItemGroup"].queryset = ItemGroup.objects.filter(IsActive = True,DeletedBy=None)
        self.fields['itemcategory_title'].widget.attrs['class'] = 'form-control'
        self.fields['itemcategory_title_bangla'].widget.attrs['class'] = 'form-control'
        self.fields['itemcategory_code'].widget.attrs['class'] = 'form-control'
        self.fields['IsActive'].widget.attrs['class'] = 'iCheck'