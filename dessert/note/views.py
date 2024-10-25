from django.shortcuts import render,redirect

# Create your views here.
from note.models import Note

def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Save the note to the database
        if title and content:
            Note.objects.create(title=title, content=content)
            return redirect('create_note')
    
    return render(request,'form.html')
