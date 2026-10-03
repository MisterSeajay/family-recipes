---
layout: posts
title: "Recipes by Chef"
permalink: /recipes-by-chef/
author_profile: true
---

<!-- markdownlint-disable MD033 -->
<!--
  This page is a Liquid template, so the markup below must be literal HTML.
  Markdown headings and lists are not rendered inside `{% for %}` loops, so
  they were deliberately converted to HTML tags (see commit 1c9de32).
-->

{% for author in site.data.authors %}
  {% assign author_id = author[0] %}
  {% assign author_details = author[1] %}
  
  <h2>{{ author_details.name }}</h2>
  <em>{{ author_details.bio }}</em>

  <ul>
    {% for post in site.posts %}
      {% if post.author == author_id %}
        <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date: "%B %Y" }})</li>
      {% endif %}
    {% endfor %}
  </ul>
  
  <hr>
{% endfor %}
