# Family Recipes Jekyll Site - Context for Claude

## Project Overview

This is a family cookbook website built with Jekyll and hosted on GitHub Pages at <https://cookbook.joynt.co.uk>. The site allows multiple family members to contribute recipes with their own author profiles.

## Visual Design

- **Theme**: Minimal Mistakes (remote theme)
- **Skin**: "dirt" - warm, earthy tones
- **Color palette**: Sand/beige (#b8956a)
- **Header images**: Pen-and-ink sketch style with sepia tones (grayscale-first method)
- **Image format**: PNG (better for illustrations than JPG)

## Git Workflow

- **Commit prefix**: All commits must start with `CKBK-00001` (required by local git hook)
- **Branch**: Work on `main` branch
- **Auto-deploy**: GitHub Pages rebuilds automatically on push (~1-2 minutes)

## Project Structure

- `_posts/`: Recipe markdown files (format: `YYYY-MM-DD-recipe-name.md`)
- `_data/authors.yml`: Family member profiles
- `_data/navigation.yml`: Site navigation menu
- `assets/images/`: Header images and recipe photos
- `scripts/`: Utility scripts (keep root clean)
- `category-*.md`: Category archive pages

## Categories

Current categories (in navigation order):

1. Vegan
2. Meat
3. Puddings
4. Baking

Each category has:

- Category page (`category-{name}.md`)
- Header image (`assets/images/header-{name}.png`)
- AI prompt file (`assets/images/header-{name}.txt`)

## AI Image Generation

**Style prompt template**:
```
[Subject description], pen and ink sketch style, detailed line work,
warm sepia tones, artistic illustration, hand-drawn aesthetic,
traditional cookbook illustration style, no text
```

**Post-processing**: Run `uv run scripts/apply-sepia.py --inplace` to ensure consistent sepia treatment across all images.

## Scripts

### scripts/apply-sepia.py

- **Purpose**: Applies consistent grayscale-first sepia tone to header images
- **Method**: Converts to grayscale (luminosity), then applies sepia tint
- **Default intensity**: 0.8
- **Usage**: `uv run scripts/apply-sepia.py --inplace`

## Family Members (Authors)

- Charles: Chief food taster & site admin
- Susannah: Vegan specialist
- William: Master of the Grill
- Edward: Pudding and Dessert Connoisseur
- Henry: Fusspot extraordinaire
- Rosalie: Italian tastes

## Key Files

- `RECIPE-TEMPLATE.md`: Template for new recipes
- `CONTRIBUTING.md`: Instructions for family members
- `about.md`: About the chefs page
- `search.md`: Recipe search page
- `.vscode/settings.json`: Peacock sand theme configuration

## Future Considerations

- GitHub Actions could auto-apply sepia to new header images
- Additional categories may be added based on family usage
- Recipe photos should go in `assets/images/recipes/`
- All images should be PNG format
