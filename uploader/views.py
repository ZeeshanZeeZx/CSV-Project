from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CSVUploadForm
from .models import CSVFile
from .tasks import process_csv

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            process_csv.delay(csv_file.id)
            return redirect('csv_list')
    else:
        form = CSVUploadForm()
    return render(request, 'uploader/upload.html', {'form': form})

def csv_list(request):
    csv_files = CSVFile.objects.all()
    return render(request, 'uploader/list.html', {'csv_files': csv_files})
