from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import SiteSettings, Skill, Project, Education, Certification, LearningTopic, ContactMessage
from .forms import ContactForm


def home(request):
    """
    Homepage view featuring Hero, About summary, Interests, Featured Projects,
    Top Skills, and Quick Contact.
    """
    settings = SiteSettings.get_settings()
    featured_projects = Project.objects.filter(featured=True)[:3]
    if not featured_projects.exists():
        featured_projects = Project.objects.all()[:3]

    skills_programming = Skill.objects.filter(category='Programming')[:5]
    skills_web = Skill.objects.filter(category='Web Development')[:5]
    skills_data = Skill.objects.filter(category='Data & AI')[:5]
    learning_topics = LearningTopic.objects.all()[:4]
    education_items = Education.objects.all()[:2]

    context = {
        'page_title': 'Home',
        'site_settings': settings,
        'featured_projects': featured_projects,
        'skills_programming': skills_programming,
        'skills_web': skills_web,
        'skills_data': skills_data,
        'learning_topics': learning_topics,
        'education_items': education_items,
    }
    return render(request, 'home.html', context)


def about(request):
    """
    About page with comprehensive bio, education history, areas of interest,
    and current learning tracks.
    """
    settings = SiteSettings.get_settings()
    education_list = Education.objects.all()
    learning_topics = LearningTopic.objects.all()
    context = {
        'page_title': 'About Me',
        'site_settings': settings,
        'education_list': education_list,
        'learning_topics': learning_topics,
    }
    return render(request, 'about.html', context)


def skills(request):
    """
    Technical skills categorized into Programming, Web Development, Data & AI, and Tools.
    """
    categories = ['Programming', 'Web Development', 'Data & AI', 'Tools']
    grouped_skills = {}
    for cat in categories:
        grouped_skills[cat] = Skill.objects.filter(category=cat)

    context = {
        'page_title': 'Technical Skills',
        'grouped_skills': grouped_skills,
    }
    return render(request, 'skills.html', context)


def projects(request):
    """
    All projects with client-side & server-side category filter capability.
    """
    category_filter = request.GET.get('category', 'all').strip()
    if category_filter and category_filter.lower() != 'all':
        project_list = Project.objects.filter(category__iexact=category_filter)
    else:
        project_list = Project.objects.all()

    context = {
        'page_title': 'Projects',
        'projects': project_list,
        'current_category': category_filter.lower(),
    }
    return render(request, 'projects.html', context)


def project_detail(request, slug):
    """
    Detailed project page displaying overview, feature list, tech badges, and links.
    """
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.exclude(id=project.id).filter(category=project.category)[:2]
    context = {
        'page_title': project.title,
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'project_detail.html', context)


def resume_view(request):
    """
    Interactive resume page with education timeline, technical summary,
    certifications, and download PDF button with missing file fallback.
    """
    settings = SiteSettings.get_settings()
    education_list = Education.objects.all()
    certifications = Certification.objects.all()
    categories = ['Programming', 'Web Development', 'Data & AI', 'Tools']
    grouped_skills = {cat: Skill.objects.filter(category=cat) for cat in categories}

    has_resume = bool(settings and settings.resume_file)
    resume_url = settings.resume_file.url if has_resume else '#'

    context = {
        'page_title': 'Resume',
        'site_settings': settings,
        'education_list': education_list,
        'certifications': certifications,
        'grouped_skills': grouped_skills,
        'has_resume': has_resume,
        'resume_url': resume_url,
    }
    return render(request, 'resume.html', context)


def contact(request):
    """
    Contact form view. Validates input, saves to database, and uses Django messages.
    """
    settings = SiteSettings.get_settings()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for reaching out! Your message has been received successfully. I will get back to you soon."
            )
            return redirect('contact')
        else:
            messages.error(
                request,
                "Please correct the errors in the form below before submitting."
            )
    else:
        form = ContactForm()

    context = {
        'page_title': 'Contact',
        'form': form,
        'site_settings': settings,
    }
    return render(request, 'contact.html', context)


def custom_404(request, exception=None):
    """
    Custom 404 handler that gracefully blends with the website design.
    """
    return render(request, '404.html', {'page_title': 'Page Not Found'}, status=404)
