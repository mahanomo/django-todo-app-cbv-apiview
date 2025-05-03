from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.views import View
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TodoForm
from .models import AddTodo
from django.urls import reverse_lazy
# Create your views here.

class TodoListView(LoginRequiredMixin,ListView):
    model = AddTodo
    template_name = "todo_app/index.html"
    context_object_name = 'object_list'
    def get_queryset(self):
        return AddTodo.objects.filter(user=self.request.user)

class TodoCreateView(LoginRequiredMixin,CreateView):
    model = AddTodo
    template_name = "todo_app/create_todo.html"
    form_class = TodoForm
    success_url = reverse_lazy('todo_app:base-todo')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model = AddTodo
    success_url = reverse_lazy('todo_app:base-todo')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)
    
class DoneTodoView(LoginRequiredMixin,View):
    def post(self, request, pk):
        todo = AddTodo.objects.get(pk=pk)
        todo.is_done = not todo.is_done
        todo.save()
        return JsonResponse({'success': True, 'is_done': todo.is_done})
    
class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = AddTodo
    form_class = TodoForm
    template_name = "todo_app/update_todo.html"
    success_url = reverse_lazy('todo_app:base-todo')