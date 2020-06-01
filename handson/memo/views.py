from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from .models import Memo, Attachment
from .forms import MemoForm, AttachmentForm


def index(request):
    memo_list = Memo.objects.order_by('-modified_at')
    context = { 'memo_list': memo_list }
    return render(request, 'memo/index.html', context)


def create_Memo(request):
    if request.method == 'POST':
        memo_form = MemoForm(request.POST)
        if memo_form.is_valid():
            memo = memo_form.save()
            return redirect('memo:read_Memo', memo_id=memo.id)
    else:
        memo_form = MemoForm()
    return render(request, 'memo/create_update_memo.html', {'memo_form': memo_form})


def read_Memo(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    attachment_list = Attachment.objects.filter(memo_id=memo_id)
    return render(request, 'memo/read_memo.html', {'memo': memo, 'attachment_list': attachment_list})


def update_Memo(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    if request.method == 'POST':
        memo_form = MemoForm(request.POST, instance=memo)
        if memo_form.save():
            return redirect('memo:read_Memo', memo_id=memo_id)
    else:
        memo_form = MemoForm(instance=memo)
    return render(request, 'memo/create_update_memo.html', {'memo_form': memo_form})


def delete_Memo(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.delete()
    return redirect('memo:index')


def create_Attachment(request, memo_id):
    if request.method == 'POST':
        attachment_form = AttachmentForm(request.POST)
        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.memo_id = memo_id
            attachment.save()
            return redirect('memo:read_Memo', memo_id=memo_id)
    else:
        attachment_form = AttachmentForm()
    return render(request, 'memo/create_update_attachment.html', {'attachment_form': attachment_form})


def delete_Attachment(request, memo_id, attachment_id):
    attachment = get_object_or_404(Attachment, pk=attachment_id)
    attachment.delete()
    return redirect('memo:read_Memo', memo_id=memo_id)
