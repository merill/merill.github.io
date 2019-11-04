---
id: 27
title: Migrated from dasBlog to BlogEngine.NET
date: 2008-02-12T22:48:00+00:00


guid: /post/2008/02/Migrated-from-dasBlog-to-BlogEngineNET.aspx
permalink: /2008/02/migrated-from-dasblog-to-blogenginenet/
dsq_thread_id:
  - "77712492"
categories:
  - BlogEngine.NET
---
<p>
After 5 years, starting from the humble <a href="http://www.simplegeek.com/CategoryView.aspx/BlogX">BlogX</a> that <a href="http://www.simplegeek.com">ChrisAn</a> wrote to <a href="http://staff.newtelligence.net/clemensv/">Clemens</a> and then <a href="http://www.hanselman.com/blog/">ScottH&#39;s</a> <a href="http://dasblog.info/">dasBlog</a>, I finally moved over to <a href="http://dotnetblogengine.net/">BlogEngine.NET</a> today. My main reasons for moving over included a brand new codebase, more features, better themes and frequent releases.
</p>
  
<p>
The other platforms that I had in mind were <a href="http://www.wordpress.org">WordPress</a> and <a href="http://graffiticms.com/">Grafitti CMS</a>, I gave up on WordPress due to my hoster being on Windows and didn&#39;t want to go through the trouble of figuring out how to get url rewrites for PHP working on IIS under my hoster&#39;s limitations.
</p>
  
<p>
Grafitti would have been my choice but it choked when I tried to import my blog posts. I opened a ticket with Telligent Systems and the really good guys mailed me today that the fix would be out in the next release this Friday. But in the end I thought it best to go with an open source platform and one that focused solely on blogging.
</p>
  
<p>
Okay now to the gory details of migrating my blog over. Which actually took a total of less than 10 minutes to setup on my machine and less than 30 minutes to upload everything to my hoster.
</p>
  
<p>
This is what I did to get my posts over to BlogEngine.NET
</p>
  
<p>
1. Setup BlogEngine locally on my machine. This just involved unzipping the file and pointing IIS to the folder.
</p>
  
<p>
2. Exported dasBlog to BlogML
</p>
  
<p>
The next version of dasBlog is scheduled to include this tool out of the box but right now you&#39;ll need to download the <a href="http://www.paulvanbrenk.com/blog/2006/12/27/BlogMLSupportForDasBlogBeta.aspx">zip</a> that <a href="http://www.paulvanbrenk.com/blog">Paul Van Brenk</a> has made available. You&#39;ll need to run the code from Visual Studio and it exports all your posts into the handy BlogML format (If anyone want&#39;s this in a nice UI let me know and I can upload it). Edit: I&#39;ve released this now, see <a href="/post/2008/03/DasBlog-to-BlogML-Converter.aspx">http://merill.net/post/2008/03/DasBlog-to-BlogML-Converter.aspx</a>&nbsp; 
</p>
  
<p>
3. Import BlogML into BlogEngine.NET
</p>
  
<p>
BlogEngine starts up a fancy ClickOnce app when you click the Import button, just feed it the BlogML file and presto all your posts and comments are migrated over.
</p>
  
<p>
I went with the Files and Images Moved Manually option which meant that I didn&#39;t have to mess around with moving any of the images or changing the paths.
</p>
  
<p>
4. Upload content
</p>
  
<p>
I simply deleted all the folders on my host server except for the ones that had the images and uploaded files which would usually be the content folder. Even here you could all the xml files that hold the posts.
</p>
  
<p>
Next I uploaded the whole BlogEngine folder that I had locally and remember to get your hosting provider to allow write permission on the App_Data folder.
</p>
  
<p>
That&#39;s all!
</p>
  
<p>
5. Configure settings
</p>
  
<p>
Obviously you&#39;ll want to play around in the control panel of the new blog and do things like put in your Google Analytics and other tracking script (which you had to edit by hand manually), redirect to the feedburner url so that your readers get your messages.
</p>
  
<p>
There are some disadvantages though like the incoming links being broken but since I don&#39;t have anything noteworthy that people link to this isn&#39;t going to be a problem for me.
</p>
