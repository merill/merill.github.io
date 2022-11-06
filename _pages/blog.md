---
title: "Merill's blog"
permalink: /blog/
author_profile: true
sidebar:
  nav: "projects"
classes: wide
---

{% for post in site.posts limit:5 %}
  <article>
    <h2>
        <a href="{{ post.url | relative_url }}" rel="permalink">{{ post.title }}</a>
    </h2>
    {% include page__meta.html type=include.type %}
    {{ post.content }}
    <section class="page__share" style="margin-bottom:80px">
      {% if site.data.ui-text[site.locale].share_on_label %}
        <h4 class="page__share-title">{{ site.data.ui-text[site.locale].share_on_label | default: "Share on" }}</h4>
      {% endif %}

      <a href="https://twitter.com/intent/tweet?{% if site.twitter.username %}via={{ site.twitter.username | url_encode }}&{% endif %}text={{ post.title | url_encode }}%20{{ post.url | absolute_url | url_encode }}" class="btn btn--twitter" onclick="window.open(this.href, 'window', 'left=20,top=20,width=500,height=500,toolbar=1,resizable=0'); return false;" title="{{ site.data.ui-text[site.locale].share_on_label | default: 'Share on' }} Twitter"><i class="fab fa-fw fa-twitter" aria-hidden="true"></i><span> Twitter</span></a>
    </section>
  </article>

{% endfor %}
