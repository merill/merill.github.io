---
id: 591
title: WPF Checked ListBox
date: 2009-10-15T09:44:16+00:00
author: Merill Fernando
layout: post
guid: http://merill.net/2009/10/wpf-checked-listbox/
permalink: /2009/10/wpf-checked-listbox/
dsq_thread_id:
  - "77713059"
categories:
  - WPF
tags:
  - checked
  - listbox
  - WPF
---
<p>WPF currently does not have a checked list box out of the box so you’ll need to roll your own. Unfortunately most of the examples that come up on Google involve creating a usercontrol and writing some code.</p>  <p>Here’s one quick way that does not not involve writing any additional code.</p>  <p>Step 1: Start off by creating a class that will represent each checked list item in the list box. Obviously if you already have your data item all you need to ensure is that it has a boolean property to store the Checked/Unchecked flag.</p>  <pre class="csharpcode"><span class="kwrd">public</span> <span class="kwrd">class</span> CheckedListItem
{
    <span class="kwrd">public</span> <span class="kwrd">int</span> Id { get; set; }
    <span class="kwrd">public</span> <span class="kwrd">string</span> Name { get; set; }
    <span class="kwrd">public</span> <span class="kwrd">bool</span> IsChecked { get; set; }
}</pre>
<style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>

<p>&#160;</p>

<p>Step 2: Create the list item that will be bound to the list box. I called my list AvailablePresentationObjects.</p>

<div id="codeSnippetWrapper">
  <pre class="csharpcode"><span class="kwrd">public</span> List&lt;CheckedListItem&gt; AvailablePresentationObjects;</pre>
  <style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style></div>

<p>Step 3: The last step is to create the actual checked list box. I created a list box and used the HierarchicalDataTemplate to hold the CheckBox. The Name and the IsChecked property are then bound to the checkbox.</p>

<pre class="csharpcode"><span class="kwrd">&lt;</span><span class="html">ListBox</span> <span class="attr">ItemsSource</span><span class="kwrd">=&quot;{Binding AvailablePresentationObjects}&quot;</span> <span class="kwrd">&gt;</span>
    <span class="kwrd">&lt;</span><span class="html">ListBox.ItemTemplate</span><span class="kwrd">&gt;</span>
        <span class="kwrd">&lt;</span><span class="html">HierarchicalDataTemplate</span><span class="kwrd">&gt;</span>
            <span class="kwrd">&lt;</span><span class="html">CheckBox</span> <span class="attr">Content</span><span class="kwrd">=&quot;{Binding Name}&quot;</span> <span class="attr">IsChecked</span><span class="kwrd">=&quot;{Binding IsChecked}&quot;</span><span class="kwrd">/&gt;</span>
        <span class="kwrd">&lt;/</span><span class="html">HierarchicalDataTemplate</span><span class="kwrd">&gt;</span>
    <span class="kwrd">&lt;/</span><span class="html">ListBox.ItemTemplate</span><span class="kwrd">&gt;</span>
<span class="kwrd">&lt;/</span><span class="html">ListBox</span><span class="kwrd">&gt;</span></pre>
<style type="text/css">
.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }</style>

<p>And walla!</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="WPF-CheckedListBox" border="0" alt="WPF-CheckedListBox" src="http://merill.net/wp-content/uploads/2009/10/WPFCheckedListBox.png" width="330" height="159" /> </p>

<p>Now the IsChecked property will reflect the value in the UI and vice versa. If you need real-time notification when someone checks/unchecks then you simply need to raise the PropertyChanged event in the CheckedListItem class.</p>