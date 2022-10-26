from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.db.models import Count, Max
from django.urls import reverse_lazy
from .models import Thread, Response
from .forms import ResponseCreateForm

# Create your views here.
# ホーム
class IndexView(ListView):
    template_name = "index.html"
    context_object_name = 'threads'

    def get_queryset(self, **kwargs):
        #レス数、最新レス順に取得
        queryset = Thread.objects.all().annotate(response_count=Count("response"), update_date=Max("response__created_at")).order_by('-update_date')

        return queryset

# スレッド
class ThreadView(DetailView):
    template_name = "thread.html"
    model = Thread
    context_object_name = 'thread'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response_form'] = ResponseCreateForm

        return context

# レス確認
class ConfirmResponseView(FormView):
    form_class = ResponseCreateForm

    def form_valid(self, form):
        form.thread_pk = self.kwargs["pk"]
        return render(self.request, 'response_confirm.html', {'form': form})

    """     def form_invalid(self, form):
        return render(self.request, 'register/user_data_input.html', {'form': form}) """

# レス投稿
class CreateResponseView(CreateView):
    form_class = ResponseCreateForm

    def form_valid(self, form):
        thread_pk = self.kwargs.get('pk')
        thread = get_object_or_404(Thread, pk=thread_pk)
        response = form.save(commit=False)
        response.thread = thread
        response.number = thread.response_set.count() + 1
        response.save()

        return redirect('thread_detail', pk=thread_pk)





