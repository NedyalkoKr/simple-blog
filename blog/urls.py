from django.urls import path
from blog.views import post_details, PostListView

app_name='blog_app'

urlpatterns = [
    # path('', index, name='index'),
    # path('', post_list, name='all_posts'),
    path('', PostListView.as_view(), name='all_posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_details, name='post_details')
]