from django import forms

from flags.conditions import get_conditions
from flags.models import FlagState
from flags.settings import get_flags


class FlagStateForm(forms.ModelForm):

    FLAGS_CHOICES = [(flag, flag) for flag in sorted(get_flags().keys())]

    name = forms.ChoiceField(choices=FLAGS_CHOICES,
                             label="Flag",
                             required=True)
    condition = forms.ChoiceField(label="Is enabled when",
                                  required=True)
    value = forms.CharField(label="Is", required=True)

    def __init__(self, *args, **kwargs):
        super(FlagStateForm, self).__init__(*args, **kwargs)

        self.fields['condition'].choices = [
            (c, c) for c in sorted(get_conditions())
        ]

    class Meta:
        model = FlagState
        fields = ('name', 'condition', 'value')
