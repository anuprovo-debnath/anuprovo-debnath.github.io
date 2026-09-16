# My Academic Website & Portfolio

This repository contains the source code for my personal academic website and research portfolio, hosted via GitHub Pages at **[anuprovo-debnath.github.io](https://anuprovo-debnath.github.io/)**.

I built this website using [Jekyll](https://jekyllrb.com/) and customized it on top of the open-source [al-folio](https://github.com/alshedivat/al-folio) academic theme.

---

## 🚀 Quick Start (Local Development)

How I run and preview my website locally:

### Option 1: Native Installation (Ruby & Bundler)

1. **Install Ruby and Bundler** (Ruby >= 3.1 recommended).
2. **Install dependencies**:
   ```bash
   bundle install
   ```
3. **Run the local development server**:
   ```bash
   bundle exec jekyll serve --livereload --port 4000
   ```
4. Open [http://localhost:4000](http://localhost:4000) in your browser.

---

### Option 2: Docker / Docker Compose

To run in a containerized environment:

```bash
# Start container and local dev server
docker compose up

# Stop container
docker compose down
```

The site will be accessible at [http://localhost:8080](http://localhost:8080) (or the port mapped in `docker-compose.yml`).

---

## 📂 Repository Structure

```text
.
├── _bibliography/         # BibTeX citation files for my publications (papers.bib)
├── _data/                 # Structured YAML data
│   └── cv.yml             # My CV content rendered dynamically on /cv/
├── _includes/             # Liquid partials (header, footer, cv modules, etc.)
├── _layouts/              # Page layouts (about, cv, page, post, default)
├── _news/                 # Short announcements displayed on my home / news page
├── _pages/                # Primary website pages (about.md, cv.md, projects.md, etc.)
├── _posts/                # Markdown files for my blog posts & notes
├── _projects/             # My research project pages & reports
├── assets/
│   ├── img/               # Images and profile pictures
│   ├── pdf/               # My PDF reports, CV, and academic documents
│   └── css/ / js/         # Custom styling and script assets
├── _config.yml            # Global Jekyll site configuration
└── Gemfile                # Ruby dependencies
```

---

## 🛠️ How I Manage & Update Content

### 1. Adding a New Project or Internship Report
1. Place the PDF report inside `assets/pdf/` (e.g., `assets/pdf/My_Report.pdf`).
2. (Optional) Place a preview image in `assets/img/` (e.g., `assets/img/report_thumbnail.png`).
3. Create a new markdown file inside `_projects/` (e.g., `_projects/my_project.md`):
   ```yaml
   ---
   layout: page
   title: Project Title
   description: Brief description
   img: assets/img/report_thumbnail.png
   importance: 1
   category: work
   ---

   ## Project Overview
   Summary of project scope, supervisor, and institution.

   ---

   ## 📄 Project Report
   <div class="embed-responsive embed-responsive-16by9">  
     <iframe src="/assets/pdf/My_Report.pdf"
             class="embed-responsive-item" 
             loading="lazy"
             style="min-height: 900px; width: 100%;"></iframe>  
   </div>
   ```

### 2. Updating My Curriculum Vitae (CV)
- **Interactive CV Page (`/cv/`)**: Update `_data/cv.yml` under the respective sections (`Education`, `Experience`, `Volunteer`, `Awards`, `Skills`, `Projects`).
- **Downloadable PDF CV**: Place my compiled PDF at `assets/pdf/cv_debnath_anuprovo.pdf` (linked in `_pages/cv.md`).

### 3. Adding Publications
Add BibTeX entries to `_bibliography/papers.bib`. The theme automatically parses, formats, and renders my citations under `/publications/`.

### 4. Adding News & Blog Posts
- **Announcements**: Add markdown files to `_news/` with front matter containing `date:` and `inline: true`.
- **Blog Posts**: Add markdown files to `_posts/` with the filename format `YYYY-MM-DD-title.md`.

---

## 🚢 Deployment & CI/CD

I use GitHub Actions (`.github/workflows/deploy.yml`) to automatically build and deploy my website to **GitHub Pages** whenever I push changes to the `main` or `master` branch.

---

## 📜 License & Credits

- Website theme: Built upon [al-folio](https://github.com/alshedivat/al-folio) by Maruan Al-Shedivat under the [MIT License](LICENSE).
- All personal research reports, writings, and content &copy; Anuprovo Debnath.
