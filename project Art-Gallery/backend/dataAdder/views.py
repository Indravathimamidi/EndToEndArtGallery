from django.shortcuts import render, get_object_or_404

# Create your views here.
# myapp/views.py

from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'imagelist.html', {'images': images})

def home(request):
    return render(request, 'index.html');

def explore(request):
    return render(request,  'explore.html');

def arts(request):
    # Filter images by category 'arts'
    arts_images = Image.objects.filter(category='art')
    return render(request, 'products.html', {'items': arts_images})


def crafts(request):
    # Filter images by category 'crafts'
    crafts_images = Image.objects.filter(category='craft')
    return render(request, 'products.html', {'items': crafts_images})

def productView(request, id):
    product = get_object_or_404(Image, id=id)
    return render(request, 'productView.html', {'product': product})
