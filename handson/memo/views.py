from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return HttpResponse("All memos:")


def create_Memo(request):
    return HttpResponse("You are creating a memo.")


def read_Memo(request, memo_id):
    return HttpResponse("You are viewing memo %s." % memo_id)


def update_Memo(request, memo_id):
    return HttpResponse("You are updating memo %s." % memo_id)


def delete_Memo(request, memo_id):
    return HttpResponse("You are deleting memo %s." % memo_id)


def create_Attachment(request, memo_id):
    return HttpResponse("You are creating an attachment for memo %s." % memo_id)


def delete_Attachment(request, memo_id, attachment_id):
    return HttpResponse("You are deleting attachmend %s from memo %s." % (attachment_id, memo_id))
