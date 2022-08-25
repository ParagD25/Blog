from django.urls import path
from blogapp import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/new',views.CreatePost.as_view(),name='post_new'),
    path('post/<pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/update/<pk>',views.PostUpdateView.as_view(),name='post_update'),
    path('post/delete/<pk>',views.PostDeleteView.as_view(),name='post_delete'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/comment/<pk>',views.add_comment,name='add_comment'),
    path('comment/approve/<pk>',views.comment_approve,name='comment_approve'),
    path('comment/remove/<pk>',views.comment_remove,name='comment_remove'),
    path('post/publish/<pk>',views.publish_post,name='publish_post'),

]