from django.shortcuts import render, get_object_or_404
from .models import Resource

def resource_list(request):
    resources = Resource.objects.all().order_by('-uploaded_at')
    return render(request, 'myapp/resource_list.html', {'resources': resources})

def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if resource.resource_type in ['latex', 'code']:
        with resource.file.open('rb') as f:
            resource_content = f.read().decode('utf-8')
    else:
        resource_content = ''

    return render(request, 'myapp/resource_detail.html', {
        'resource': resource,
        'content': resource_content
    })