from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from django.views.generic import ListView

# Create your views here.

# app_name = 'blog_app'

# def index(request):
#     get_all_posts = Post.objects.all()
#     get_all_posts_2018 = Post.objects.filter(publish__year=2018)
#     get_all_posts_2017 = Post.objects.filter(publish__year=2017)
#     published_by_year_and_author = Post.objects.filter(publish__year=2018, author__username='ned')
#     all_posts_excluded = Post.objects.exclude(title__startswith='Post')
#     post_ordered_by = Post.objects.order_by('title')


#     context = {
#         'all_posts': get_all_posts,
#         'all_posts_2018': get_all_posts_2018,
#         'all_posts_2017': get_all_posts_2017,
#         'published_by_author': published_by_year_and_author,
#         'posts_excluded': all_posts_excluded,
#         'ordered_posts': post_ordered_by,
#     }

#     return render(request, 'index.html', context)



# def post_list(request):
#     all_published_posts = Post.objects.all()
#     paginator = Paginator(all_published_posts, 2)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     this_year_posts = Post.objects.filter(publish__year=2018)
#     return render(request, 'blog/post/list.html', 
#             {
#                 'page': page,
#                 'posts': this_year_posts
#             })

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'



def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, status='published', slug=post,
            publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/details.html', {'post': post })