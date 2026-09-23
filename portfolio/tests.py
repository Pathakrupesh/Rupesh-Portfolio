from django.test import TestCase, Client
from django.urls import reverse
from .models import Project, ContactMessage, SiteSettings, Skill, Education


class PortfolioViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.settings = SiteSettings.objects.create(
            name="Rupesh Pathak",
            title="Computer Science Student | Aspiring Software & AI Engineer",
            email="pathakrupesh666@gmail.com"
        )
        self.project = Project.objects.create(
            title="AutoCare",
            slug="autocare",
            category="Web",
            short_description="Vehicle Service & Maintenance Management System",
            full_description="Full test description for AutoCare.",
            technologies="Python, Django, PostgreSQL, Bootstrap 5",
            features="Vehicle management\nService booking\nMaintenance tracking",
            featured=True
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rupesh Pathak")
        self.assertContains(response, "AutoCare")

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About")

    def test_skills_page_status_code(self):
        response = self.client.get(reverse('skills'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_status_code(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AutoCare")

    def test_project_detail_view(self):
        response = self.client.get(reverse('project_detail', args=[self.project.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AutoCare")
        self.assertContains(response, "Vehicle Service & Maintenance Management System")

    def test_resume_page_status_code(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)

    def test_contact_form_valid_submission(self):
        data = {
            'name': 'Recruiter Test',
            'email': 'recruiter@example.com',
            'subject': 'Software Engineering Internship Opportunity',
            'message': 'Hello Rupesh, we reviewed your portfolio and would like to invite you for an interview.'
        }
        response = self.client.post(reverse('contact'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.name, 'Recruiter Test')
        self.assertFalse(msg.is_read)

    def test_contact_form_invalid_submission(self):
        # Missing required message and invalid short name
        data = {
            'name': 'A',
            'email': 'not-an-email',
            'subject': '',
            'message': 'short'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_404_page(self):
        response = self.client.get('/this-url-does-not-exist/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "404", status_code=404)
