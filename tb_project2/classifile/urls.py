from django.urls import path
from .views import FileListView, FileDetailView, FileCreateView, FileUpdateView, FileDeleteView, UserFileListView
from . import views
from django.conf.urls.static import static
from django.conf import settings
#from django.contrib.auth.views import FileUploadView

urlpatterns = [
    path('', FileListView.as_view(), name='classifile-home'),
    path('user<str:username>', UserFileListView.as_view(), name='user-files'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('file/new/', FileCreateView.as_view(), name='file-create'),
    path('file/<int:pk>/update/', FileUpdateView.as_view(), name='file-update'),
    path('file/<int:pk>/delete/', FileDeleteView.as_view(), name='file-delete'),
    path('about/', views.about, name='classifile-about'),
]


# only in development
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
