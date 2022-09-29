from django.shortcuts import render, redirect

from djangoExample.playground.forms import PostForm
from djangoExample.playground.models import Post
from djangoExample.utils.link_manager import LinkManager

link_manager = LinkManager([
    LinkManager.Link(
        url='landing-page',
        template_name='playground/landing-page.html',
        label='Home'
    ),
    LinkManager.Link(
        url='posts',
        template_name='playground/posts.html',
        label='Posts'
    ),
    LinkManager.Link(
        url='add-posts',
        template_name='playground/add-post.html',
        label='Post anlegen'
    ),
])


def landing_page(request):

    template_name = 'playground/landing-page.html'
    page_links = link_manager.get_links_for(template_name)

    context = {'links': page_links}

    return render(
        request=request,
        template_name=template_name,
        context=context
    )


def posts(request):

    template_name = 'playground/posts.html'
    page_links = link_manager.get_links_for(template_name)

    last_10_posts = Post.objects.filter()[:10]

    context = {
        'posts': last_10_posts,
        'links': page_links
    }

    return render(
        request=request,
        template_name=template_name,
        context=context
    )


def add_post(request):

    template_name = 'playground/add-post.html'
    page_links = link_manager.get_links_for(template_name)

    form = PostForm

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('posts/')


    context = {
        'form': form,
        'links': page_links
    }

    return render(
        request=request,
        template_name=template_name,
        context=context
    )
