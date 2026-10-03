# 🛠️ Site Administration & Developer Guide

This document is for site administrators and anyone looking to customize the layout, theme, configuration, or run
maintenance tasks on the family cookbook Jekyll site.

For details on how to add recipes (either manually or using the AI assistant), see the
[README.md](file:///c:/Users/micro/Development/family-recipes/README.md).

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

3. Open your browser and navigate to `http://localhost:4000`.
   The page will reload automatically as you make changes to files.

---

## 2. Configuration & Customization

### Global Settings (`_config.yml`)

The site uses the [Minimal Mistakes Theme](https://mmistakes.github.io/minimal-mistakes/).
You can configure:

- **Site Skins**: Change the look and feel by changing `minimal_mistakes_skin` in `_config.yml`
  (e.g., `dirt`, `sunrise`, `dark`, `neon`, `contrast`).
- **Subdomain Settings**: Update `url` when deploying on custom subdomains or pages.

### Data Management (`_data/`)

- **Authors (`_data/authors.yml`)**: Add and edit biographical information for family members here.
  This controls the profiles displayed at the bottom of recipes and on author pages.
- **Navigation (`_data/navigation.yml`)**: Modify the site menu links (Home, Categories, Search, etc.).

---

## 3. Header Images

Every page banner in `assets/images/` is stored as a pair of files:

- `header-<page>.png` — the image the site displays.
- `header-<page>.txt` — the image generation prompt used to create it.

The `.txt` files are **deliberate records and must not be deleted**, even though they are never rendered by the site.

### Current banners

| Page | Files |
| --- | --- |
| Home | `header-home.png` / `.txt` |
| Meat | `header-meat.png` / `.txt` |
| Vegan | `header-vegan.png` / `.txt` |
| Puddings | `header-puddings.png` / `.txt` |
| Baking | `header-baking.png` / `.txt` |
| Recipe template fallback | `header-photo.png` / `.txt` |

### Adding a new banner

1. Write the generation prompt to `assets/images/header-<page>.txt`.
2. Generate the image from that prompt and save it as `assets/images/header-<page>.png`.
3. Apply the sepia tone (see below).
4. Reference the image from the page's front matter via `header.overlay_image`.
5. If it is a new section, add it to `_data/navigation.yml`.

### Sepia tone

All banners share a single vintage tone so that the set looks like a matched set.
The script that applies it, `format-image`, lives in the **PyTools** repository at
`C:/Users/micro/Development/PyTools`, not in this one.

```bash
# Preview one image, writing a new '-sepia' file and leaving the original alone
uv run --project C:/Users/micro/Development/PyTools --package pytools-image \
  format-image assets/images/header-home.png

# Rewrite the originals in place
uv run --project C:/Users/micro/Development/PyTools --package pytools-image \
  format-image assets/images/header-*.png --inplace

# Lighter tint, with JSON output for scripting
uv run --project C:/Users/micro/Development/PyTools --package pytools-image \
  format-image assets/images/header-home.png --intensity 0.6 --json
```

This step is **not automated**. There are no GitHub Actions workflows in this repository; the site is deployed by
GitHub Pages' own build, which never runs this script.
So a newly added banner will look out of place next to the existing ones until the tone has been applied by hand.

---

## 4. Documentation Standards

Markdown is linted with `markdownlint-cli2` using the rules in `.markdownlint.json`, mirroring the conventions of the
PyTools repository. Prose wraps at 120 characters.

```bash
markdownlint-cli2 "**/*.md"
```

Use `markdownlint-cli2 "**/*.md" --fix` to auto-correct the mechanical issues (missing blank lines, list style).

Notes:

- `.claude/**` is excluded through `.markdownlint-cli2.jsonc`, as it is local agent context rather than site content.
- There are no Jekyll theme files in this repository to exclude.
  Minimal Mistakes is a `remote_theme` fetched at build time, so every tracked `.md` file is our own content.
