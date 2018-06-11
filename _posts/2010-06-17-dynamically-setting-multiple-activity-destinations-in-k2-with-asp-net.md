---
id: 690
title: Dynamically setting multiple activity destinations in K2 with ASP .NET
date: 2010-06-17T14:18:42+00:00
author: Merill Fernando
layout: post
guid: http://merill.net/?p=690
permalink: /2010/06/dynamically-setting-multiple-activity-destinations-in-k2-with-asp-net/
dsq_thread_id:
  - "108546559"
categories:
  - .NET
tags:
  - destinations
  - infopath
  - k2
  - workflow
---
When building a typical workflow you usually know which user or group needs to perform an activity at design time. Sometimes though the workflow needs to be more dynamic.

The issue I had to resolve recently involved having to build a workflow where the end-user gets to individually pick the users who will be performing the next step. Here's a view of  the workflow design.

<a href="http://merill.net/wp-content/uploads/2010/06/K2-Multiple-Destination-Workflow.png"><img class="alignnone size-full wp-image-691" title="K2 Multiple=" src="http://merill.net/wp-content/uploads/2010/06/K2-Multiple-Destination-Workflow.png" alt="" width="696" height="478" /></a>

The scenario involved an application being submitted for review. The application would go to an individual who is responsible for assigning a group of users (destination users) to review the application. The twist was that it was the individual picking users for each application, it wasn't a fixed group or role. The screen mockup shows how they do it.

When the person hits the 'Assign Reviewers' button the form then needs to turn up as a work list item for each of the reviewers (destination users) who get to review the application in parallel.

Implementing this process using K2/InfoPath is quite straightforward and is well documented in many places including this post titled '<a href="http://www.k2underground.com/blogs/fromthebench/archive/2008/05/22/activity-destination-users-based-upon-a-repeating-xml-element.aspx">Activity Destination Users based upon a Repeating XML element</a>' in a K2 underground blog.

It's not well documented though for ASP.NET. The post '<a href="http://www.k2underground.com/blogs/fromthebench/archive/2009/08/18/how-to-use-a-web-service-for-destinations-in-k2-blackpoint.aspx?CommentPosted=true#commentmessage">How To: Use a web service for destinations in K2 blackpoint</a>' is close to what we want but it's targeted at using a web service.

K2 let's you set multiple destination users in one of two ways

1. Using a SmartObject method in a role

2. Using Xml as a destination set

Going the SmartObject route was a lot of work for my simple requirement so I chose the Xml method. The idea here is to use the list of users in the Assign Reviewers form and store them in a Process xml field. The destination set will then be configured to read the xml field and create a slot for each user.

FYI: See page 4 of the <a href="http://help.k2.com/en/AdvancedDestinations_Whitepaper.aspx">Advanced Destinations whitepaper</a> for a description of the two roles. &lt;rant&gt;Why the K2 KB portal needs a login is beyond me.&lt;/rant&gt;

<strong>Step 1: Write the code to create the xml containing the list of users</strong>

The code block below accepts a ; delimited list of domain name\username (e.g. domain\johna) and creates an XML document containing the list of users. This is then assigned to the Process Instance XML field called Reviewers.
<div style="color: black; background: white; font-family: Consolas; font-size: 10pt;">
<pre style="margin: 0px;"><span style="color: blue;">private</span> <span style="color: blue;">static</span> <span style="color: blue;">void</span> AssignReviewers(<span style="color: #2b91af;">WorklistItem</span> item, <span style="color: blue;">string</span> listOfUsers)</pre>
<pre style="margin: 0px;">{</pre>
<pre style="margin: 0px;">    <span style="color: blue;">var</span> doc = <span style="color: blue;">new</span> <span style="color: #2b91af;">XmlDocument</span>();</pre>
<pre style="margin: 0px;">    <span style="color: blue;">var</span> root = doc.CreateElement(<span style="color: #a31515;">"UserList"</span>);</pre>
<pre style="margin: 0px;">    doc.AppendChild(root);</pre>
<pre style="margin: 0px;"></pre>
<pre style="margin: 0px;">    <span style="color: blue;">foreach</span> (<span style="color: blue;">string</span> user <span style="color: blue;">in</span> listOfUsers.Split(<span style="color: #a31515;">';'</span>))</pre>
<pre style="margin: 0px;">    {</pre>
<pre style="margin: 0px;">        <span style="color: blue;">var</span> userNode = doc.CreateElement(<span style="color: #a31515;">"Users"</span>);</pre>
<pre style="margin: 0px;">        userNode.InnerText = user;</pre>
<pre style="margin: 0px;">        root.AppendChild(userNode);</pre>
<pre style="margin: 0px;">    }</pre>
<pre style="margin: 0px;">    item.ProcessInstance.XmlFields[<span style="color: #a31515;">"Reviewers"</span>].Value = doc.OuterXml;</pre>
<pre style="margin: 0px;">}</pre>
</div>
<strong>Step 2: Create an xml schema based on the user list xml</strong>

This proved to be the trickiest part for me. Using the xsd.exe as documented in this <a href="http://www.k2underground.com/blogs/fromthebench/archive/2009/08/18/how-to-use-a-web-service-for-destinations-in-k2-blackpoint.aspx">article</a> didn't work.  After a lot of anguish I worked out that K2 was happy with the schema generated by InfoPath. So I opened an empty form in InfoPath and added a repeating text field (<a href="http://www.k2underground.com/blogs/fromthebench/archive/2008/05/22/activity-destination-users-based-upon-a-repeating-xml-element.aspx">screenshot</a>).

Next I exported the form to get to the .xsd (in InfoPath 2010 it is File -&gt; Publish -&gt; Export Source Files). Cleaning out the my: namespace and a bit of tweaking should give you the following schema definition. This definition should work fine with the xml produced by the above code block.
<div style="color: black; background: white; font-family: Consolas; font-size: 10pt;">
<pre style="margin: 0px;"><span style="color: blue;">&lt;?</span><span style="color: #a31515;">xml</span><span style="color: blue;"> </span><span style="color: red;">version</span><span style="color: blue;">=</span>"<span style="color: blue;">1.0</span>"<span style="color: blue;"> </span><span style="color: red;">encoding</span><span style="color: blue;">=</span>"<span style="color: blue;">UTF-8</span>"<span style="color: blue;"> </span><span style="color: red;">standalone</span><span style="color: blue;">=</span>"<span style="color: blue;">no</span>"<span style="color: blue;">?&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">&lt;</span><span style="color: #a31515;">xsd:schema</span><span style="color: blue;"> </span><span style="color: red;">xmlns:xsd</span><span style="color: blue;">=</span>"<span style="color: blue;">http://www.w3.org/2001/XMLSchema</span>"<span style="color: blue;">&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">  &lt;</span><span style="color: #a31515;">xsd:element</span><span style="color: blue;"> </span><span style="color: red;">name</span><span style="color: blue;">=</span>"<span style="color: blue;">UserList</span>"<span style="color: blue;">&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">    &lt;</span><span style="color: #a31515;">xsd:complexType</span><span style="color: blue;">&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">      &lt;</span><span style="color: #a31515;">xsd:sequence</span><span style="color: blue;">&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">        &lt;</span><span style="color: #a31515;">xsd:element</span><span style="color: blue;"> </span><span style="color: red;">name</span><span style="color: blue;">=</span>"<span style="color: blue;">Users</span>"<span style="color: blue;"> </span><span style="color: red;">minOccurs</span><span style="color: blue;">=</span>"<span style="color: blue;">0</span>"<span style="color: blue;"> </span><span style="color: red;">maxOccurs</span><span style="color: blue;">=</span>"<span style="color: blue;">unbounded</span>"<span style="color: blue;">/&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">      &lt;/</span><span style="color: #a31515;">xsd:sequence</span><span style="color: blue;">&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">    &lt;/</span><span style="color: #a31515;">xsd:complexType</span><span style="color: blue;">&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">  &lt;/</span><span style="color: #a31515;">xsd:element</span><span style="color: blue;">&gt;</span></pre>
<pre style="margin: 0px;"><span style="color: blue;">&lt;/</span><span style="color: #a31515;">xsd:schema</span><span style="color: blue;">&gt;</span></pre>
</div>
<strong>Step 3: Create an xml field for the process</strong>

Armed with the xml schema, we're now ready to configure the workflow.

Fire up the K2 process designer and add the process xml field name <em>Reviewers</em> which we referred to in our code in step 1.

To do this open the Process General Properties window, expand the right panel. From the list select the Process/Activity Data node, expand it to select the name of your process and right-click on it to click Add.. and get to the Add XML Field.

<img class="alignnone size-full wp-image-696" title="K2 Add Process Xml Field" src="http://merill.net/wp-content/uploads/2010/06/K2-Add-Process-Xml-Field.png" alt="" width="306" height="192" />

Name the field 'Reviewers'.

<img class="alignnone size-full wp-image-697" title="K2 Add Xml Field Dialog" src="http://merill.net/wp-content/uploads/2010/06/K2-Add-Xml-Field-Dialog.png" alt="" width="462" height="205" />

Switch to the XML Schema tab and browse to pick the xsd file created in Step 2.

When you hit OK you should now be able to drill down and see the Users node.

<img class="alignnone size-full wp-image-698" title="K2 Xml Field Step" src="http://merill.net/wp-content/uploads/2010/06/K2-Xml-Field-Step.png" alt="" width="188" height="183" />

The key is to make sure that the node's icon has a green overlay which flags it as a repeating node. If it's there you should be fine. If not you need to repeat the steps above until you get the green overlay icon. Without it, the worklist item is not going to be assigned to multiple users.

<strong>Step 4: Setup the destination to read from the xml field</strong>

Select the activity which needs to be executed in parallel and click on the Destination Users node. Switch to the Advanced Mode if you are not already in there (select the checkbox on the first page). In the Destination Rule Options select Plan per destination -&gt;All at once. We do this to tell K2 that when it goes to multiple users they will be able to open and work on the item in parallel.

<img class="alignnone size-full wp-image-703" title="K2 Setup Destination 1" src="http://merill.net/wp-content/uploads/2010/06/K2-Setup-Destination-1.png" alt="" width="560" height="281" />

Select 'Create a slot for each destination', this way each destination user get's their own slot.

<img class="alignnone size-full wp-image-704" title="K2 Setup Destination 2" src="http://merill.net/wp-content/uploads/2010/06/K2-Setup-Destination-2.png" alt="" width="543" height="328" />

Click on the Edit button to configure the Destination sets.

<img class="alignnone size-full wp-image-705" title="K2 Setup Destination 3" src="http://merill.net/wp-content/uploads/2010/06/K2-Setup-Destination-3.png" alt="" width="532" height="198" />

Click on the ellipsis to open the Context Browser, drill down to the Process Xml field that we setup earlier and drag the Users repeating node (the one with the green icon) onto Name column.

<img class="alignnone size-full wp-image-706" title="K2 Setup Destination 4" src="http://merill.net/wp-content/uploads/2010/06/K2-Setup-Destination-4.png" alt="" width="734" height="323" />

You should now be all set to test out your dynamic multiple destination users! Running through the workflow you will now see that the worklist item gets assigned to each of the reviewers in parallel.