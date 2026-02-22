# 🍳 How to Add a Recipe

Welcome to the family cookbook! To keep our site looking great and easy to search, please follow these steps when adding your delicious creations.

## 1. The Filename (Very Important!)
All recipes live in the `_posts/` folder. Your file **must** follow this exact naming format:
`YYYY-MM-DD-name-of-recipe.md`

*Example:* `2024-05-22-moms-vegan-lasagna.md`

## 2. The "Recipe Header" (Front Matter)
Every recipe needs a header at the very top. Copy and paste this block and fill in your details:

---
layout: single
title: "Name of Your Recipe"
author: "YourName"        # Must match your name in _data/authors.yml
categories:
  - Vegan                # Choose one: Vegan, Meat, Puddings, or Course
tags:
  - Quick
  - Spicy
  - Favorite
---

## 3. Writing the Recipe
Use standard Markdown below the header:

* **Bold** text for emphasis: `**Preheat oven to 200°C**`
* Use `###` for sub-headings (Ingredients, Method).
* Use `*` for bullet points (Ingredients).
* Use `1.` for numbered lists (Steps).

## 4. Adding Images
1. Save your photo in the `assets/images/` folder.
2. Use a simple name like `lasagna.jpg`.
3. Link it in your recipe like this:  
   `![Description of photo](/assets/images/lasagna.jpg)`

## 5. Sending it Live
1. **Pull** the latest changes: `git pull origin main`
2. **Create** your new file in the `_posts` folder.
3. **Commit** your changes: `git commit -m "Added [Recipe Name]"`
4. **Push** to GitHub: `git push origin main`

The website will update automatically in about a minute! 🚀
