# Rupesh Portfolio — Django Personal Portfolio Website

A clean, modern, and professional personal developer portfolio built with **Python 3**, **Django**, and **Bootstrap 5**. Designed specifically for **Rupesh Pathak** (Computer Science Student | Aspiring Software & AI Engineer) to showcase projects, technical skills, academic background, certifications, resume, and contact management.

---

## 🌟 Key Features

- **Modern Dark Interface:** Sleek dark-mode aesthetic with clean typography, soft card borders, and subtle animations (includes instant Dark/Light mode toggle).
- **Dynamic Content via Django Models:** Update your bio, social links, location, and resume through the Django Admin panel without editing HTML code.
- **Projects Showcase & Filtering:** Instant client-side and server-side filtering (All, Web, Python, Data, AI). Includes the featured **AutoCare Vehicle Service & Maintenance Management System**.
- **Categorized Technical Skills:** Organized into Programming, Web Development, Data & AI, and Developer Tools.
- **Interactive Resume & Education Timeline:** Dedicated resume page with St. Xavier's College academic details and graceful fallback if a PDF is not yet uploaded.
- **Contact Inquiries with Admin Management:** Working contact form protected with CSRF and Django messages. Inquiries are stored in the database with read/unread statuses in Django Admin.
- **Zero-Config SQLite by Default:** Runs locally straight out of the box. Ready for PostgreSQL deployment via `DATABASE_URL`.
- **Sample Data Included:** One-command seed tool (`python manage.py seed_data`) to populate the portfolio immediately.

---

## 🚀 Beginner-Friendly Setup Guide (Visual Studio Code on Windows)

Follow these exact steps to run this project on your Windows machine:

### Step 1 — Extract the ZIP Archive
1. Right-click `Rupesh-Portfolio.zip` and select **Extract All...**
2. Choose a destination folder (for example, `C:\Users\<YourUsername>\Projects\Rupesh-Portfolio`).

---

### Step 2 — Open the Project in VS Code
1. Launch **Visual Studio Code**.
2. Click **File** in the top menu and select **Open Folder...**
3. Select the extracted `Rupesh-Portfolio` directory (make sure you see `manage.py` inside the root folder).

---

### Step 3 — Open the Integrated Terminal
1. In VS Code, open the terminal by pressing `` Ctrl + ` `` (backtick) or go to the top menu: **Terminal → New Terminal**.

---

### Step 4 — Create a Python Virtual Environment
Run the following command in the terminal to create an isolated Python environment:
```powershell
python -m venv venv
```
*(Wait 5-10 seconds for the `venv` folder to appear).*

---

### Step 5 — Activate the Virtual Environment

#### On Windows PowerShell:
```powershell
venv\Scripts\Activate.ps1
```

> ⚠️ **PowerShell Execution Policy Error?**  
> If Windows gives an error saying *“running scripts is disabled on this system”*, simply run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```
> Then run `venv\Scripts\Activate.ps1` again.  
> Alternatively, switch to the Command Prompt (CMD) in VS Code terminal and run:
> ```cmd
> venv\Scripts\activate.bat
> ```

Once activated, your terminal prompt will show `(venv)` at the beginning of the line.

---

### Step 6 — Install Required Packages
With `(venv)` active, install all dependencies:
```powershell
pip install -r requirements.txt
```

---

### Step 7 — Run Database Migrations
Create the local SQLite database tables:
```powershell
python manage.py migrate
```

---

### Step 8 — Populate Sample Portfolio Data
Run the built-in seeding command to populate your skills, education, AutoCare project, and site settings:
```powershell
python manage.py seed_data
```

---

### Step 9 — Create an Admin Superuser (For Admin Login)
Create an account to manage your portfolio content:
```powershell
python manage.py createsuperuser
```
You will be prompted for:
1. **Username**: (e.g., `admin` or `rupesh`)
2. **Email address**: (e.g., `pathakrupesh666@gmail.com`)
3. **Password**: (type a secure password; characters will be hidden for security)
4. **Password (again)**: (re-type to confirm)

---

### Step 10 — Start the Development Server
```powershell
python manage.py runserver
```

---

### Step 11 — Open Your Website in the Browser
- **Portfolio Website:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Django Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Log in to the Admin Panel using the superuser credentials created in Step 9 to customize your name, bio, social links, add new projects, or view submitted contact messages.

---

## 📁 Project Structure

```
Rupesh-Portfolio/
├── manage.py                   # Django CLI management utility
├── requirements.txt            # Python dependencies (Django, dotenv, etc.)
├── README.md                   # This setup and documentation file
├── .gitignore                  # Git exclusions for secrets, venv, and bytecode
├── .env.example                # Example environment configuration
├── .env                        # Local development settings
│
├── config/                     # Core Django project configuration
│   ├── __init__.py
│   ├── asgi.py                 # ASGI entry point
│   ├── wsgi.py                 # WSGI entry point
│   ├── settings.py             # Project settings (SQLite, static, media, apps)
│   └── urls.py                 # Top-level URL routing & 404 handler
│
├── portfolio/                  # Main portfolio application
│   ├── __init__.py
│   ├── admin.py                # Admin registrations & customized list views
│   ├── apps.py                 # App configuration
│   ├── models.py               # Models: SiteSettings, Project, Skill, Education, etc.
│   ├── views.py                # View functions (home, about, projects, contact, etc.)
│   ├── urls.py                 # Portfolio URL routes
│   ├── forms.py                # ContactForm with validation
│   ├── tests.py                # Automated unit tests
│   ├── context_processors.py   # Injects site settings and current year globally
│   ├── management/             # Custom management commands
│   │   └── commands/
│   │       └── seed_data.py    # `python manage.py seed_data` command
│   └── migrations/
│       └── 0001_initial.py     # Initial database migration
│
├── templates/                  # Reusable HTML5 templates
│   ├── base.html               # Master layout (Navbar, Footer, CSS/JS includes)
│   ├── home.html               # Hero, Interests, Featured Projects, Highlights
│   ├── about.html              # Bio, Education, Career Interests
│   ├── skills.html             # Categorized skills matrix
│   ├── projects.html           # Project catalog with instant JS category filters
│   ├── project_detail.html     # Deep dive into individual project specs
│   ├── resume.html             # Qualifications, coursework, and PDF download
│   ├── contact.html            # Contact form with database persistence & messages
│   └── 404.html                # Friendly custom 404 error page
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css           # Custom Modern Dark styles + Light mode overrides
│   └── js/
│       └── main.js             # Theme toggle & category filter scripts
│
└── media/                      # User uploads and media
    ├── projects/               # Project screenshots & AutoCare SVG illustration
    ├── resume/                 # Folder for rupesh_resume.pdf
    └── profile/                # Folder for profile picture uploads
```

---

## 🧪 Running Automated Tests

Verify that all views and forms are functioning correctly:
```powershell
python manage.py test
```

---

## 🛠️ Customizing Your Portfolio

1. **Profile Info & Socials:** Log into `/admin/` and click on **Site Settings**. Update your GitHub URL, LinkedIn URL, bio, and upload your profile picture.
2. **Resume:** Place your resume PDF in `media/resume/` or upload it through **Site Settings > Resume file** in Django Admin.
3. **Projects:** Add your latest software applications in **Projects**; toggle the `Featured` checkbox to showcase them on the homepage.
4. **PostgreSQL in Production:** To deploy to Heroku, Render, or Railway, provide a `DATABASE_URL` in your environment variables. Django will automatically connect to PostgreSQL!

---

## 📄 License
This portfolio template is open-source and customizable for personal developer portfolios.
