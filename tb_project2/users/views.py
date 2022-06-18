from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UploadFileForm, FileFieldForm#, ModelFormWithFileField
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
#from django.views.generic.edit import FormView

from users.models import Document
from users.forms import DocumentForm


def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs, force_insert=False, force_update=False, using=None)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)





def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('users.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


#class FileFieldFormView(FormView):
#    form_class = FileFieldForm
#    template_name = 'fileupload.html'  # Replace with your template.
#    success_url = '...'  # Replace with your URL or reverse().
#
#    def post(self, request, *args, **kwargs):
#        form_class = self.get_form_class()
#        form = self.get_form(form_class)
#        files = request.FILES.getlist('file_field')
#        if form.is_valid():
#            for f in files:
#                ...  # Do something with each file.
#            return self.form_valid(form)
#        else:
#            return self.form_invalid(form)


#def upload_file(request):
#    if request.method == 'POST':
#        form = ModelFormWithFileField(request.POST, request.FILES)
#        if form.is_valid():
#            # file is saved
#            form.save()
#            return HttpResponseRedirect('/success/url/')
#    else:
#        form = ModelFormWithFileField()
#    return render(request, 'upload.html', {'form': form})
