from django.db import models
from django.utils.text import slugify


class SiteSettings(models.Model):
    """
    Singleton-style settings model to store editable portfolio information.
    Ensures that Rupesh can update profile details without touching HTML code.
    """
    name = models.CharField(max_length=100, default='Rupesh Pathak')
    title = models.CharField(
        max_length=150,
        default='Computer Science Student | Aspiring Software & AI Engineer'
    )
    short_bio = models.TextField(
        default="I'm a Computer Science student interested in software development, "
                "data science, and artificial intelligence. I enjoy turning ideas into "
                "practical software projects and continuously learning new technologies."
    )
    about_full = models.TextField(
        blank=True,
        default="I am an undergraduate Computer Science student at St. Xavier's College, Kathmandu. "
                "My primary passions lie at the intersection of modern software engineering, web architectures, "
                "and applied artificial intelligence. I focus on writing clean, maintainable code, building robust backend systems, "
                "and exploring machine learning workflows to solve real-world problems."
    )
    email = models.EmailField(default='[YOUR EMAIL]')
    github_url = models.URLField(default='https://github.com/[YOUR_GITHUB_USERNAME]', blank=True)
    linkedin_url = models.URLField(default='https://linkedin.com/in/[YOUR_LINKEDIN_USERNAME]', blank=True)
    location = models.CharField(max_length=100, default='Kathmandu, Nepal')
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return f"{self.name} Portfolio Settings"

    @classmethod
    def get_settings(cls):
        settings = cls.objects.filter(is_active=True).first()
        if not settings:
            settings, _ = cls.objects.get_or_create(id=1)
        return settings


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Web Development', 'Web Development'),
        ('Data & AI', 'Data & AI'),
        ('Tools', 'Tools'),
    ]

    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Proficient', 'Proficient'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Programming')
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='Proficient')
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Bootstrap icon name (e.g. bi-filetype-py, bi-code-slash, bi-database)"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Web', 'Web Development'),
        ('Python', 'Python Application'),
        ('Data', 'Data Science & Analysis'),
        ('AI', 'Artificial Intelligence & ML'),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Web')
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    technologies = models.CharField(
        max_length=255,
        help_text="Comma-separated list of technologies (e.g. Python, Django, PostgreSQL, Bootstrap 5)"
    )
    features = models.TextField(
        blank=True,
        help_text="Key features separated by new lines"
    )
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(
        default='https://github.com/[YOUR_GITHUB_USERNAME]/[PROJECT_REPO]',
        blank=True,
        help_text="Editable GitHub repository link"
    )
    live_url = models.URLField(
        blank=True,
        help_text="Editable live demo link (leave empty if not deployed)"
    )
    featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def feature_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=150, default="Bachelor's in Computer Science / Information Technology")
    institution = models.CharField(max_length=150, default="St. Xavier's College, Kathmandu")
    location = models.CharField(max_length=100, default="Kathmandu, Nepal")
    start_year = models.CharField(max_length=10, default="2022")
    end_year = models.CharField(max_length=20, default="Present")
    is_current = models.BooleanField(default=True)
    description = models.TextField(
        blank=True,
        default="Focusing on core computer science foundations, algorithms, object-oriented software engineering, database management systems, and applied machine learning."
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Education'
        ordering = ['order', '-start_year']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):
    name = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    issue_date = models.CharField(max_length=50, blank=True, default="[Date / Year]")
    credential_url = models.URLField(blank=True, default="https://[VERIFY_CREDENTIAL_URL]")
    credential_id = models.CharField(max_length=100, blank=True)
    certificate_file = models.FileField(upload_to='certifications/', blank=True, null=True)
    is_sample = models.BooleanField(default=False, help_text="Checked if this is an editable placeholder")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.name} - {self.organization}"


class LearningTopic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='bi-lightbulb')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
