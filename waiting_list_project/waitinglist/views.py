# import statements


from django.views import generic
from .forms import EntryForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Entry


# Create your views here.


class EntryListView(generic.ListView):
    model = Entry
    paginate_by = 10


class EntryDetailView(generic.DetailView):
    model = Entry


class EntryCreate(CreateView):
    model = Entry
    form_class = EntryForm


class EntryUpdate(UpdateView):
    model = Entry
    form_class = EntryForm


class EntryDelete(DeleteView):
    model = Entry
    success_url = reverse_lazy('entries')
