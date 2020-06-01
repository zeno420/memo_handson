from django import forms

from .models import Memo, Attachment

class MemoForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ('title', 'text')


class AttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ('url',)
