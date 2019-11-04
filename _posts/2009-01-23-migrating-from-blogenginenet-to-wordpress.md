---
id: 559
title: Migrating from BlogEngine.NET to WordPress
date: 2009-01-23T06:43:40+00:00
author: Merill Fernando

guid: http://merill.net/2009/01/migrating-from-blogenginenet-to-wordpress/
permalink: /2009/01/migrating-from-blogenginenet-to-wordpress/
dsq_thread_id:
  - "77715097"
categories:
  - Tips
tags:
  - BlogEngine.NET
  - blogml
  - migrate
  - wordpress
---
Yet another migration post, feels like just yesterday I <a href="http://merill.net/2008/02/migrated-from-dasblog-to-blogenginenet/">migrated from dasBlog to BlogEngine.NET</a>.

My justification was that I didn’t want to be manually updating my blog with each new release.

With <a href="http://www.aneef.net/">Aneef</a> graciously offering to host my site I’d be cutting down on my hosting bill as well! How sweet is that?

So here’s how I made the move.
<ul>
	<li>First I setup a new instance of WordPress on my host account. Now this is the absolutest fun part, with <a href="http://cpanel-host.com/fantastico/">Fantastico</a> it takes just two clicks and literally two seconds to install WP, plus upgrading to the latest version of WordPress is going to be a breeze as well!</li>
</ul>
<blockquote><a rel="lightbox" title="Fantastico" href="https://merill.net/wp-content/uploads/2009/01/fantasticowordpressinstall.jpg"><img style="border-top-width: 0px; display: inline; border-left-width: 0px; border-bottom-width: 0px; border-right-width: 0px" title="fantastico-wordpress-install" src="https://merill.net/wp-content/uploads/2009/01/fantasticowordpressinstall-thumb.jpg" border="0" alt="fantastico-wordpress-install" width="240" height="219" /></a></blockquote>
<ul>
	<li>Next we’ll export our posts to BlogML from the BlogEngine.NET admin site.</li>
	<li>You’ll need to tweak this file a bit before the import. Search for .axd files and you’ll realize the first problem. BlogEngine seems to pull down the images through an .axd file, a simple search and replace should fix this problem. You might want to move your images to the wp-content/uploads folder as well since it will become easier to backup your stuff.</li>
	<li>In the BlogML file, the categories seem to have a GUID, which I think I might have inherited from dasBlog, but if you do come across the problem you can either do a search and replace with the GUIDs or after importing into WordPress rename the category from the Admin site.</li>
	<li>Finally you’ll need to add the BlogML Import plugin to your WP install. Just grab the <a href="http://www.kavinda.net/content/other/BlogML-WordPress-Import.zip">zip file</a> from <a href="http://www.kavinda.net">Kavinda</a>, unzip and upload them to the wp-admin/imports folder check his <a href="http://www.kavinda.net/2008/10/23/migrating-from-dasblog-to-wordpress.html">post</a> and the related posts if you have trouble setting it up.</li>
	<li>From the WordPress admin menu click import, supply your file and your done!</li>
	<li>You’ll of course need to upload your images as well.</li>
	<li>If your using FeedBurner remember to change the source address of FeedBurner and also use the FeedBurner plugin from Google so that new user’s will get the FeedBurner url when they subscribe to your blog.</li>
</ul>
Enjoy! Let me know if you have any issues migrating.