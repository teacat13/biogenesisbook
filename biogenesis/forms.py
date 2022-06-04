from django.conf import settings
from django import forms
from .models import Reviews, Entity
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ReviewForm(forms.ModelForm):
    #Форма отзывов
    captcha = ReCaptchaField()
    class Meta:
            model = Reviews
            fields = ("name", "email", "text", "captcha")
            widgets = {
                "name": forms.TextInput(attrs={"class": "form-control border"}),
                "email": forms.EmailInput(attrs={"class": "form-control border"}),
                "text": forms.Textarea(attrs={"class": "form-control border", "id": "contactcomment"})
            }

class AddStateForm(forms.ModelForm):
        #description = forms.CharField(label="", widget=CKEditorWidget())
        class Meta:
            model = Entity
            fields = '__all__'
            exclude = ('draft', 'user')

        # def save(self, request):
        #     obj = super(AddStateForm, self).save(commit=False)
        #     if self.request and self.request.user:
        #         obj.user = self.request.user()
        #         obj.save()
        #     return obj

        # def save(self, obj):
        #     if getattr(obj, 'user') is None:
        #         obj.user = request.user
        #         obj.save()







