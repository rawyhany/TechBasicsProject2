from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#FileUploadForm
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()
    file = forms.FileField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

#def form():
#    form = UploadFileForm(request.POST, request.FILES)
#    if form.is_valid():
#        upload_file = form.save(commit=False)
#        upload_file.uploader = request.user
#        upload_file.save()
#        return HttpResponseRedirect(
#            reverse_lazy('file-detail', kwargs={'pk': self.pk})
#        )
#    else:
#        return HttpResponse(form.errors)
