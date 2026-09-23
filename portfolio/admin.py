from django.contrib import admin
from .models import SiteSettings, Skill, Project, Education, Certification, LearningTopic, ContactMessage


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'location', 'is_active', 'updated_at']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'short_bio', 'about_full', 'location', 'profile_image', 'resume_file')
        }),
        ('Contact & Social Links', {
            'fields': ('email', 'github_url', 'linkedin_url')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

    def has_add_permission(self, request):
        # Prevent multiple active instances to maintain singleton simplicity
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']
    list_editable = ['order', 'proficiency']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'created_at']
    list_filter = ['category', 'featured', 'created_at']
    search_fields = ['title', 'technologies', 'short_description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['featured']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'is_current', 'order']
    list_editable = ['order']
    search_fields = ['degree', 'institution']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'issue_date', 'is_sample', 'order']
    list_filter = ['is_sample', 'organization']
    search_fields = ['name', 'organization']
    list_editable = ['order']


@admin.register(LearningTopic)
class LearningTopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Selected messages marked as read.")
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, "Selected messages marked as unread.")
    mark_as_unread.short_description = "Mark selected messages as unread"
