from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import File
from django.views.generic.edit import FormView
#from django.contrib.auth.views import FileUploadView
#from django.http import HttpResponse

#CONTROLS FILE UPLOADS

def home(request):
    context = {
        'files': File.objects.all()
    }
    return render(request, 'classifile/home.html', context)


def image_files(request):
    context = {
        'files': File.objects.images()
    }
    return render(request, 'classifile/home.html', context)

class FileListView(ListView):
    model = File
    template_name = 'classifile/home.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'files'
    ordering = ['-date_uploaded']
    paginate_by = 5

class UserFileListView(ListView):
    model = File
    template_name = 'classifile/user_files.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'files'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return File.objects.filter(uploader=user).order_by('date_uploaded')



class FileDetailView(DetailView):
    model = File
    uploader = User

class FileCreateView(LoginRequiredMixin, CreateView):
    model = File
    fields = ['title', 'content', 'file']

class FileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = File
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        file = self.get_object()
        if self.request.user == file.uploader:
            return True
        return False


class FileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = File
    success_url = '/'

    def test_func(self):
        file = self.get_object()
        if self.request.user == file.uploader:
            return True
        return False

def about(request):
    return render(request, 'classifile/about.html', {'title': 'About'})


def filter(request):
    template = 'classifile/home.html'
    image_files = classifile.objects.filter(filetype="Image")
    text_files = classifile.objects.filter(filetype="Text")
    audio_files = classifile.objects.filter(filetype="Audio")
    visual_files = classifile.objects.filter(filetype="Video")
    context = {
    'image_files': Image,
    'text_files': Text,
    'audio_files': Audio,
    'visual_files': Video
    }
    return render(request, template, context)

#def file_upload(request):
#    if request.method == "POST":
#	    # if the post request has a file under the input name 'document', then save the file.
#	    request_file = request.FILES['document'] if 'document' in request.FILES else None
#	    if request_file:
#		    	# save attached file
#
#			    # create a new instance of FileSystemStorage
#			    fs = FileSystemStorage()
#			    file = fs.save(request_file.name, request_file)
#			    # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
#			    fileurl = fs.url(file)
#    return render(request, "fileupload.html")
