from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Album


class indexview(generic.ListView):
    template_name='music/index.html'
    context_oblect_name='all_albums'

    def get_queryset(self):
        return Album.objects.all()



class detailview(generic.DetailView):
    model=Album
    template_name = 'music/detail.html'


class albumcreate(CreateView):
    model=Album
    fields=['artist','artist_title','genre','album_logo']
