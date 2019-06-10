from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Entry

class HomeView(LoginRequiredMixin,ListView):
    model = Entry
    template_name = 'index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_data']
    paginate_by = 2



class EntryView(LoginRequiredMixin,DetailView):
    model = Entry
    template_name = "detail.html"
    context_object_name = "object"
    


class CreateEntryView(LoginRequiredMixin,CreateView):
    model = Entry
    template_name = "create_entry.html"
    fields =["entry_title","entry_text"]

    def form_valid(self,form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)