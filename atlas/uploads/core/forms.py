from django import forms

from atlas.uploads.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['description', 'titolo', 'added_by', 'feature_image']

    exclude= ['added_by']

    def __init__(self, added_by, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)