from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'code', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            t = self.fields[field].widget.__class__.__name__
            if t != 'CheckboxInput':
                self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['type'] = t
        self.fields['text'].widget.attrs['rows'] = '24'
