from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from slugify import slugify

from .models import Page
from .forms import PageForm, LoginForm


# ─── Public Views ─────────────────────────────────────────────────────────────

def home(request):
    query = request.GET.get('q', '').strip()
    pages = Page.objects.filter(status=Page.STATUS_PUBLISHED)
    if query:
        pages = pages.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    all_pages = Page.objects.filter(status=Page.STATUS_PUBLISHED).order_by('title')
    return render(request, 'wiki/home.html', {
        'pages': pages,
        'all_pages': all_pages,
        'query': query,
    })


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, status=Page.STATUS_PUBLISHED)
    all_pages = Page.objects.filter(status=Page.STATUS_PUBLISHED).order_by('title')
    return render(request, 'wiki/page_detail.html', {
        'page': page,
        'all_pages': all_pages,
    })


# ─── Auth Views ────────────────────────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Invalid credentials or insufficient permissions.')

    return render(request, 'wiki/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


# ─── Admin Views ───────────────────────────────────────────────────────────────

@login_required
def admin_dashboard(request):
    pages = Page.objects.all().order_by('-updated_at')
    published_count = pages.filter(status=Page.STATUS_PUBLISHED).count()
    draft_count = pages.filter(status=Page.STATUS_DRAFT).count()
    return render(request, 'wiki/admin_dashboard.html', {
        'pages': pages,
        'published_count': published_count,
        'draft_count': draft_count,
    })


@login_required
def page_create(request):
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save()
            messages.success(request, f'Page "{page.title}" created successfully.')
            return redirect('admin_dashboard')

    return render(request, 'wiki/page_form.html', {
        'form': form,
        'action': 'Create',
        'page': None,
    })


@login_required
def page_edit(request, slug):
    page = get_object_or_404(Page, slug=slug)
    form = PageForm(instance=page)

    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            messages.success(request, f'Page "{page.title}" updated successfully.')
            return redirect('admin_dashboard')

    return render(request, 'wiki/page_form.html', {
        'form': form,
        'action': 'Edit',
        'page': page,
    })


@login_required
def page_delete(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if request.method == 'POST':
        title = page.title
        page.delete()
        messages.success(request, f'Page "{title}" deleted.')
        return redirect('admin_dashboard')
    return render(request, 'wiki/page_confirm_delete.html', {'page': page})


@login_required
def page_toggle_status(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if request.method == 'POST':
        if page.status == Page.STATUS_PUBLISHED:
            page.status = Page.STATUS_DRAFT
            messages.info(request, f'"{page.title}" moved to draft.')
        else:
            page.status = Page.STATUS_PUBLISHED
            messages.success(request, f'"{page.title}" published.')
        page.save()
    return redirect('admin_dashboard')
