from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Memo, Attachment


def index(request):
    memo_list = Memo.objects.order_by('-modified_at')
    context = { 'memo_list': memo_list }
    return render(request, 'memo/index.html', context)


def create_Memo(request):
    return HttpResponse("You are creating a memo.")


def read_Memo(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    attachment_list = Attachment.objects.filter(memo_id=memo_id)
    return render(request, 'memo/read_memo.html', {'memo': memo, 'attachment_list': attachment_list})


def update_Memo(request, memo_id):
    return HttpResponse("You are updating memo %s." % memo_id)


def delete_Memo(request, memo_id):
    return HttpResponse("You are deleting memo %s." % memo_id)


def create_Attachment(request, memo_id):
    return HttpResponse("You are creating an attachment for memo %s." % memo_id)


def delete_Attachment(request, memo_id, attachment_id):
    return HttpResponse("You are deleting attachmend %s from memo %s." % (attachment_id, memo_id))
