# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added William's BBQ steak recipe with garlic butter and peppercorn sauce to Meat category (CKBK-00001)
- Enhanced Susannah's Spicy Vegan Chickpea Curry with complete recipe details (CKBK-00001)
- Added Rosalie's Marzipan recipe to Puddings category (CKBK-00001)
- Documented in AGENTS.md that the `header-*.txt` files alongside each header image are the intentional image
  generation prompts, not clutter, along with the two places a new header must be wired up
- Adopted the PyTools repository's Markdown standards: added `.markdownlint.json` (120-character wrap, matching
  PyTools). Every tracked `.md` file is now linted
- Added the site design tokens (theme, skin, overlay colour, image format), a map of the repository layout, and the
  header image style prompt template to AGENTS.md
- Documented in AGENTS.md and CONTRIBUTING.md that no GitHub Actions workflow exists and that the sepia step for
  header images must be run by hand

### Changed

- Moved the sepia tone script out to the PyTools repository as `format-image`, rewritten to the house Python standard
  (typer, rich, loguru to stderr, plus `--json`, `--verbose` and `--debug`). Verified to match the previous output to
  within 1/255 per channel on a real header image
- Replaced that script's per-pixel Python loop with Pillow's `convert`, `ImageOps.colorize` and `Image.blend`, which is
  equivalent in output but substantially faster
- Applied the 120-character Markdown standard across the documentation, fixing missing blank lines around headings,
  lists and code fences, asterisk list style, trailing whitespace and duplicate headings
- Lowered `#` to `##` for the intro heading in `about.md` and RECIPE-TEMPLATE.md, so those pages no longer render a
  second top-level heading beneath the front matter title

### Removed

- Removed `.claude/` and untracked `.claude/CLAUDE.md`. Its content was either duplicated in AGENTS.md or has been
  folded into it. Guidance for AI assistants now lives solely in AGENTS.md, and `.claude/` is gitignored so any
  local copy stays out of the repository
- Dropped the `CKBK-00001` commit prefix requirement, which referred to a local git hook that no longer applies.
  Commit messages are now free-form
- Removed `scripts/apply-sepia.py` and the now-empty `scripts/` directory, having moved the functionality to PyTools.
  The old name also broke the house naming convention: `apply` is not an approved PowerShell verb
- Dropped the unused `Course` category from the documented category list. It was never used by any recipe and appears
  to be a leftover from an earlier Starter/Main/Dessert scheme that `Puddings` superseded. Docs now steer contributors
  towards the four categories that actually exist rather than letting them create new ones

### Fixed

- Fixed chef headers on Recipes by Chef page rendering as literal "##" by replacing Markdown syntax with HTML tags
  inside Liquid for loop (CKBK-00001)
- Suppressed the inline-HTML lint rule locally in `authors-archive.md`, where the Liquid loop requires literal HTML tags
