from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from .tables import DocumentTable
from atlas.uploads.core.models import Document
from atlas.uploads.core.forms import DocumentForm
from django.views.generic import ListView, DeleteView


class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'core/document_delete.html'
    context_object_name= 'delete_document'
    success_url = reverse_lazy('model_form_upload')




class DocumentListView(ListView):
    model = Document
    template_name = 'core/document.html'


def home2(request):
    documents = Document.objects.all()
    return render(request, 'core/model_form_upload.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        added_by =request.user
        form = DocumentForm(added_by, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            documents = Document.objects.all().filter(added_by=request.user)
            table = DocumentTable(Document.objects.all().filter(added_by=request.user))
            return render(request, 'core/model_form_upload.html', {'form': form,'documents': documents, 'table' :table})
    else:
        added_by = request.user
        form = DocumentForm(added_by)
        documents = Document.objects.all().filter(added_by=request.user)
        return render(request, 'core/model_form_upload.html',{'form': form,'documents': documents})



def documentList(request):
    documents = Document.objects.all()
    return render(request, 'document/list.html', {'documents': documents})


def uploadDocuments(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document/upload.html', {'form': form})


def deleteDocument(request, pk):
    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('document_list')


