from django import forms
from .models import Event, Category, Participant

class MixinForm:
   

    input_class = (
        "block w-full rounded-lg border-gray-300 bg-white text-gray-900 shadow-sm "
        "focus:border-gray-900 focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50 transition"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            old_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{old_classes} {self.input_class}".strip()
            # Use field label as placeholder if not set
            if 'placeholder' not in field.widget.attrs:
                field.widget.attrs['placeholder'] = field.label

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']

        widgets = {
            'date' : DateInput(),
            'time' : TimeInput()
        }

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ["name","description"]

class ParticipantForm(forms.ModelForm):
    
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']

        widgets = {
            
            'events' : forms.CheckboxSelectMultiple(attrs={
                "class":"grid grid-cols-1 gap-2 md:grid-cols-2"
            })
        }

class EventFilterForm(forms.Form):
    query = forms.CharField(required=False, label="Search your event with name or location")
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False, empty_label="All categories"
    )
    start = forms.DateField(required=False, widget=DateInput(), label="Start Date")
    end = forms.DateField(required=False, widget=DateInput(), label="End Date")
    
