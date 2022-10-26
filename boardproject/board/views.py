from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.db.models import Count, Max
from .models import Thread, Response, Key
from .forms import ResponseCreateForm
import secrets, string

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
        context["response_form"] = ResponseCreateForm(initial={"delete_code":get_random_code(10)})

        return context

# レス確認
class ConfirmResponseView(FormView):
    form_class = ResponseCreateForm

    def form_valid(self, form):
        form.thread_pk = self.kwargs["pk"]

        return render(self.request, 'response_confirm.html', {'form': form})

# レス投稿
class CreateResponseView(CreateView):
    form_class = ResponseCreateForm

    def form_valid(self, form):
        thread_pk = self.kwargs.get('pk')
        thread = get_object_or_404(Thread, pk=thread_pk)
        response = form.save(commit=False)
        response.thread = thread
        response.number = thread.response_set.count() + 1
        ip = get_ip_address(self.request)
        key = Key.objects.order_by('created_at').last()
        response.random_id = xor_encrypt(ip, key.key)
        response.save()

        return redirect('thread_detail', pk=thread_pk)

def get_random_code(length):
    chars = string.ascii_letters + string.digits
    random_code = ''.join(secrets.choice(chars) for x in range(length))
    return random_code

def get_ip_address(request):
    ip_addresses = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_addresses:
        # 'HTTP_X_FORWARDED_FOR'ヘッダがある場合: 転送経路の先頭要素を取得する。
        ip_address = ip_addresses.split(',')[0]
    else:
        # 'HTTP_X_FORWARDED_FOR'ヘッダがない場合: 直接接続なので'REMOTE_ADDR'ヘッダを参照する。
        ip_address = request.META.get('REMOTE_ADDR')
    return ip_address

def xor_encrypt(word, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(word, key)])

def xor_decrypt(word, key):
        return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(word, key)])

