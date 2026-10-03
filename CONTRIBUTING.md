# 🛠️ Site Administration & Developer Guide

This document is for site administrators and anyone looking to customize the layout, theme, configuration, or run maintenance tasks on the family cookbook Jekyll site.

For details on how to add recipes (either manually or using the AI assistant), see the [README.md](file:///c:/Users/micro/Development/family-recipes/README.md).

---

## 1. Local Jekyll Development

To preview the cookbook website locally on your computer:

### Prerequisites
- **Ruby**: Install Ruby (3.0 or higher recommended) for your OS.
- **Bundler**: Install Bundler by running:
  ```bash
  gem install bundler
  ```

### Running the Site
1. Open your terminal in this directory and install the required dependencies:
   ```bash
   bundle install
   ```
2. Start the local Jekyll server:
   ```bash
   bundle exec jekyll serve --livereload
   ```
3. Open your browser and navigate to `http://localhost:4000`. The page will reload automatically as you make changes to files.

---

## 2. Configuration & Customization

### Global Settings (`_config.yml`)
The site uses the [Minimal Mistakes Theme](https://mmistakes.github.io/minimal-mistakes/). You can configure:
- **Site Skins**: Change the look and feel by changing `minimal_mistakes_skin` in `_config.yml` (e.g., `dirt`, `sunrise`, `dark`, `neon`, `contrast`).
- **Subdomain Settings**: Update `url` when deploying on custom subdomains or pages.

### Data Management (`_data/`)
- **Authors (`_data/authors.yml`)**: Add and edit biographical information for family members here. This controls the profiles displayed at the bottom of recipes and on author pages.
- **Navigation (`_data/navigation.yml`)**: Modify the site menu links (Home, Categories, Search, etc.).

---

## 3. Maintenance Scripts & Utilities

To maintain visual consistency across our recipe headers, we have utility scripts in the `scripts/` directory:

### Image Sepia Processing (`scripts/apply-sepia.py`)
This Python script processes header images matching `assets/images/header-*.png` and applies a vintage sepia tint. This ensures a consistent sketch/vintage illustration aesthetic across different pages.

#### Requirements
- Python 3.13+
- Pillow library

#### Commands
You can run the script using standard Python or via `uv` (recommended):

```bash
# Preview results (creates new files with a '-sepia' suffix without altering originals)
uv run scripts/apply-sepia.py

# Modify header images in-place (replaces the original files)
uv run scripts/apply-sepia.py --inplace

# Modify specific files with a custom intensity (0.0 to 1.0; default is 0.8)
uv run scripts/apply-sepia.py --intensity 0.6 --inplace assets/images/header-home.png
```
