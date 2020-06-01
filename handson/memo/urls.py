from django.urls import path

from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_Memo, name='create_Memo'),
    path('<int:memo_id>/', views.read_Memo, name='read_Memo'),
    path('<int:memo_id>/update', views.update_Memo, name='update_Memo'),
    path('<int:memo_id>/delete', views.delete_Memo, name='delete_Memo'),
    path('<int:memo_id>/create_attachment', views.create_Attachment, name='create_Attachment'),
    path('<int:memo_id>/delete_attachment/<int:attachment_id>', views.delete_Attachment, name='delete_Attachment'),
]
