from django.shortcuts import render, get_object_or_404
from .models import Resource

def resource_list(request):
    resources = Resource.objects.all().order_by('-uploaded_at')
    return render(request, 'myapp/resource_list.html', {'resources': resources})

def resource_detail(request, pk):
    # Get the resource object or return 404 if not found
    resource = get_object_or_404(Resource, pk=pk)
    
    # For LaTeX or code files, read the content so we can render it in template
    if resource.resource_type in ['latex', 'code']:
        resource_content = resource.file.read().decode('utf-8')
    else:
        resource_content = ''
    
    # Pass both the resource and its content to the template
    return render(request, 'myapp/resource_detail.html', {
        'resource': resource,
        'content': resource_content
    })