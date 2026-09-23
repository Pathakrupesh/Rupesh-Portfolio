from django.core.management.base import BaseCommand
from portfolio.models import SiteSettings, Skill, Project, Education, Certification, LearningTopic


class Command(BaseCommand):
    help = 'Seeds the database with initial portfolio data for Rupesh Pathak'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding portfolio data for Rupesh Pathak..."))

        # 1. Site Settings
        settings, created = SiteSettings.objects.get_or_create(id=1)
        settings.name = "Rupesh Pathak"
        settings.title = "Computer Science Student | Aspiring Software & AI Engineer"
        settings.short_bio = (
            "I'm a Computer Science student interested in software development, "
            "data science, and artificial intelligence. I enjoy turning ideas into "
            "practical software projects and continuously learning new technologies."
        )
        settings.about_full = (
            "I am an undergraduate Computer Science student at St. Xavier's College, Kathmandu. "
            "My primary passions lie at the intersection of modern software engineering, web architectures, "
            "and applied artificial intelligence. I focus on writing clean, maintainable code, building robust backend systems, "
            "and exploring machine learning workflows to solve real-world problems."
        )
        settings.email = "pathakrupesh666@gmail.com"
        settings.github_url = "https://github.com/[YOUR_GITHUB_USERNAME]"
        settings.linkedin_url = "https://linkedin.com/in/[YOUR_LINKEDIN_USERNAME]"
        settings.location = "Kathmandu, Nepal"
        settings.is_active = True
        settings.save()
        self.stdout.write(self.style.SUCCESS("✓ Site settings configured."))

        # 2. Education
        Education.objects.all().delete()
        Education.objects.create(
            degree="Bachelor's in Computer Science / Information Technology",
            institution="St. Xavier's College, Kathmandu",
            location="Kathmandu, Nepal",
            start_year="2022",
            end_year="Present",
            is_current=True,
            description=(
                "Pursuing an undergraduate degree with focus on Data Structures & Algorithms, "
                "Object-Oriented Programming, Database Management Systems (DBMS), Operating Systems, "
                "and Artificial Intelligence."
            ),
            order=1
        )
        self.stdout.write(self.style.SUCCESS("✓ Education data seeded."))

        # 3. Skills
        Skill.objects.all().delete()
        skills_data = [
            # Programming
            ("Python", "Programming", "Proficient", "bi-filetype-py", 1),
            ("C", "Programming", "Intermediate", "bi-code-slash", 2),
            ("C++", "Programming", "Intermediate", "bi-code-slash", 3),
            ("JavaScript", "Programming", "Proficient", "bi-filetype-js", 4),

            # Web Development
            ("HTML5", "Web Development", "Advanced", "bi-filetype-html", 1),
            ("CSS3", "Web Development", "Advanced", "bi-filetype-css", 2),
            ("Bootstrap 5", "Web Development", "Advanced", "bi-bootstrap", 3),
            ("Django", "Web Development", "Proficient", "bi-diagram-3", 4),
            ("REST APIs", "Web Development", "Proficient", "bi-hdd-network", 5),

            # Data & AI
            ("NumPy", "Data & AI", "Proficient", "bi-calculator", 1),
            ("Pandas", "Data & AI", "Proficient", "bi-table", 2),
            ("SQL", "Data & AI", "Proficient", "bi-database", 3),
            ("Data Analysis", "Data & AI", "Intermediate", "bi-graph-up-arrow", 4),
            ("Machine Learning", "Data & AI", "Intermediate", "bi-cpu", 5),

            # Tools
            ("Git", "Tools", "Proficient", "bi-git", 1),
            ("GitHub", "Tools", "Proficient", "bi-github", 2),
            ("VS Code", "Tools", "Advanced", "bi-laptop", 3),
            ("PostgreSQL", "Tools", "Intermediate", "bi-database-fill", 4),
            ("Docker", "Tools", "Beginner", "bi-box-seam", 5),
        ]
        for name, category, proficiency, icon, order in skills_data:
            Skill.objects.create(
                name=name,
                category=category,
                proficiency=proficiency,
                icon=icon,
                order=order
            )
        self.stdout.write(self.style.SUCCESS(f"✓ {len(skills_data)} skills seeded across 4 categories."))

        # 4. Projects
        Project.objects.all().delete()

        # Primary Project: AutoCare
        Project.objects.create(
            title="AutoCare — Vehicle Service & Maintenance Management System",
            slug="autocare",
            category="Web",
            short_description=(
                "A vehicle service and maintenance management system designed to manage customers, "
                "vehicles, bookings, service records, maintenance, invoices, and related operations."
            ),
            full_description=(
                "AutoCare is a comprehensive vehicle service and workshop management web application. "
                "Built using Django and PostgreSQL with a modern Bootstrap 5 UI, it streamlines automotive "
                "repair workflows, customer scheduling, and technician task assignments.\n\n"
                "The application provides granular role-based access control, allowing workshop managers, "
                "technicians, and car owners to collaborate smoothly. Key workflows include vehicle onboarding, "
                "automated service job cards, itemized parts and labor invoicing, and scheduled maintenance alerts."
            ),
            technologies="HTML5, CSS3, JavaScript, Bootstrap 5, Python, Django, PostgreSQL",
            features=(
                "Vehicle Management & Registry\n"
                "Online Service Appointment Booking\n"
                "Service History & Detailed Maintenance Logs\n"
                "Real-time Maintenance Status Tracking\n"
                "Automated Invoicing & Billing Generation\n"
                "Role-Based Access Control (Admin, Technician, Customer)\n"
                "Comprehensive Admin Dashboard"
            ),
            github_url="https://github.com/[YOUR_GITHUB_USERNAME]/autocare-vehicle-management",
            live_url="https://[YOUR-AUTOCARE-DEMO-URL]",
            featured=True
        )

        # Secondary Project: AI / ML
        Project.objects.create(
            title="Document Intelligence & Question-Answering Engine",
            slug="document-intelligence-qa",
            category="AI",
            short_description=(
                "An NLP-driven research tool that extracts key insights from technical documents and "
                "answers contextual queries with citation grounding."
            ),
            full_description=(
                "Developed as an experimental project to understand modern natural language processing and semantic embeddings. "
                "The engine reads technical PDFs or articles, partitions documents into semantic chunks, and allows users to ask "
                "natural language questions with prompt grounding."
            ),
            technologies="Python, NumPy, Pandas, Scikit-Learn, REST APIs",
            features=(
                "Semantic text chunking and vector indexing\n"
                "Contextual similarity matching\n"
                "Interactive web interface for queries\n"
                "Citations and source segment highlighting"
            ),
            github_url="https://github.com/[YOUR_GITHUB_USERNAME]/doc-intelligence-qa",
            live_url="",
            featured=True
        )

        # Secondary Project: Data Analysis
        Project.objects.create(
            title="Academic Performance & Learning Analytics Dashboard",
            slug="learning-analytics-dashboard",
            category="Data",
            short_description=(
                "An exploratory data analysis tool analyzing student engagement metrics, course progress, "
                "and predictive performance markers using statistical models."
            ),
            full_description=(
                "A data analysis and visualization dashboard built to explore student success variables. "
                "Uses Pandas and NumPy to clean and aggregate academic records, and presents trends via "
                "interactive charts to highlight areas needing intervention."
            ),
            technologies="Python, Pandas, NumPy, SQL, Data Analysis",
            features=(
                "Data cleaning and missing value imputation pipeline\n"
                "Exploratory statistical summaries & distributions\n"
                "Cohort progression tracking\n"
                "Exportable CSV reports"
            ),
            github_url="https://github.com/[YOUR_GITHUB_USERNAME]/student-learning-analytics",
            live_url="",
            featured=True
        )

        # Secondary Project: Python Tools
        Project.objects.create(
            title="Developer CLI Task & Workflow Automator",
            slug="developer-cli-automator",
            category="Python",
            short_description=(
                "A lightweight terminal command-line tool built with Python to automate repository setup, "
                "virtual environment initialization, and repetitive developer chores."
            ),
            full_description=(
                "Designed to boost day-to-day productivity for student developers. The CLI wraps Git routines, "
                "virtual environment provisioning, and automated testing runs in a clean, colored terminal interface."
            ),
            technologies="Python, Git, CLI, Automation",
            features=(
                "Automated Python virtualenv bootstrapping\n"
                "Git branch and commit template generator\n"
                "Color-coded terminal status outputs\n"
                "Cross-platform support (Linux, macOS, Windows)"
            ),
            github_url="https://github.com/[YOUR_GITHUB_USERNAME]/dev-cli-automator",
            live_url="",
            featured=False
        )
        self.stdout.write(self.style.SUCCESS("✓ Sample projects seeded (AutoCare & others)."))

        # 5. Currently Learning Topics
        LearningTopic.objects.all().delete()
        learning_items = [
            ("Data Science", "Deepening understanding of feature engineering, probability distributions, and statistical hypothesis testing with Pandas and SciPy.", "bi-graph-up"),
            ("Machine Learning", "Studying supervised and unsupervised learning algorithms, cost functions, gradient descent, and evaluation metrics.", "bi-cpu"),
            ("Django & REST APIs", "Building scalable RESTful web services with Django REST Framework, authentication tokens, and API documentation.", "bi-diagram-3"),
            ("Cloud & DevOps Fundamentals", "Exploring containerization with Docker, CI/CD pipelines with GitHub Actions, and deploying web applications to cloud platforms.", "bi-cloud-check"),
        ]
        for idx, (title, desc, icon) in enumerate(learning_items, start=1):
            LearningTopic.objects.create(title=title, description=desc, icon=icon, order=idx)
        self.stdout.write(self.style.SUCCESS("✓ Currently Learning topics seeded."))

        # 6. Certifications (Clearly labeled sample entries)
        Certification.objects.all().delete()
        Certification.objects.create(
            name="Python for Everybody Specialization",
            organization="Coursera / University of Michigan (Example Placeholder)",
            issue_date="2023",
            credential_url="https://[VERIFY_CREDENTIAL_URL]",
            credential_id="EXAMPLE-CERT-ID-123",
            is_sample=True,
            order=1
        )
        Certification.objects.create(
            name="Foundations of Data Science & Analysis",
            organization="Kaggle / Online Academy (Example Placeholder)",
            issue_date="2024",
            credential_url="https://[VERIFY_CREDENTIAL_URL]",
            credential_id="EXAMPLE-CERT-ID-456",
            is_sample=True,
            order=2
        )
        self.stdout.write(self.style.SUCCESS("✓ Sample certifications seeded (editable in Django admin)."))
        self.stdout.write(self.style.SUCCESS("\n🎉 All portfolio sample data successfully populated!"))
