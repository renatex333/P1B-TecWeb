from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer

def index(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        title_edit = request.POST.get('titulo-edit')
        content_edit = request.POST.get('detalhes-edit')

        if not id:
            new_note = Note(title=title, content=content)
            new_note.save()
        elif id and title_edit and content_edit:
            Note.objects.filter(id = id).update(title=title_edit, content=content_edit)
        elif id and not title_edit:
            Note.objects.filter(id = id).delete()
            
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

@api_view(['GET', 'POST'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)