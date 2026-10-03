# 🍳 Family Recipes Cookbook

Welcome to our family cookbook! This repository holds a collection of our favourite family recipes, which are built into a website hosted at [cookbook.joynt.co.uk](https://cookbook.joynt.co.uk).

If you are a family member looking to add your recipes, you can either:
1. **Ask the AI Assistant for help** (Easiest!) - details below.
2. **Add it manually** by following the instructions below.

---

## 🤖 Option 1: Let the AI Assistant Do It!

If you are using this client (like Antigravity or Claude) to view this folder, you don't need to know Git, Markdown, or Jekyll structure. 

Simply tell the AI assistant:
> *"I want to add a new recipe for [Recipe Name]."*

The assistant will ask you simple questions (like who is the author, what are the ingredients, and how do you cook it) and automatically format, save, and publish the recipe to the website for you!

---

## 📝 Option 2: Add it Manually

If you prefer to write the recipe yourself, follow these steps to keep our cookbook neat and tidy:

### 1. File Name and Location
All recipes must go into the `_posts/` folder. The file **must** be named in this exact format:
`YYYY-MM-DD-recipe-name.md`

*Example:* `2026-05-30-susannahs-chickpea-curry.md`

### 2. Recipe Header (Front Matter)
Copy and paste this header block at the very top of your recipe file, then fill in your details:

```yaml
---
layout: single
title: "Name of Your Recipe"
author: "YourName"        # Must match your name in _data/authors.yml
categories:
  - Vegan                # Choose one: Vegan, Meat, Puddings, or Baking
tags:
  - Quick
  - Spicy
  - Favorite
---
```

You can copy a clean starting point from [RECIPE-TEMPLATE.md](file:///c:/Users/micro/Development/family-recipes/RECIPE-TEMPLATE.md).

### 3. Writing the Recipe Body
Use standard Markdown formatting:
- Use `##` or `###` for section headings (e.g., `## 🛒 Ingredients`, `## 🍳 Method`).
- Use `*` or `-` for bullet points (e.g., ingredients).
- Use `1.`, `2.`, etc., for numbered instructions.
- Use `**` to make text **bold**.

### 4. Adding Photos
1. Put your photo in the `assets/images/recipes/` folder.
2. Use a simple, lowercase file name (e.g., `lasagna.jpg`).
3. Link the image in your recipe using this format:
   `![Description of photo](/assets/images/recipes/lasagna.jpg)`

### 5. Publishing Your Recipe
To send your new recipe live:
1. **Pull the latest version** of the cookbook so you have everyone's latest changes:
   ```bash
   git pull origin main
   ```
2. **Create and save** your new file in the `_posts` folder.
3. **Commit your changes**:
   ```bash
   git commit -am "Added [Recipe Name] recipe"
   ```
4. **Push your changes to GitHub**:
   ```bash
   git push origin main
   ```

Within a minute, the website will automatically rebuild and show your new recipe! 🚀

---

## 🛠️ Site Administration & Local Development
If you want to run the website locally on your computer or manage theme customization, see the guidelines in [CONTRIBUTING.md](file:///c:/Users/micro/Development/family-recipes/CONTRIBUTING.md).
