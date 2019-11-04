---
id: 39
title: The Dangers of Static Events In User Controls
date: 2007-12-18T14:18:52+00:00


guid: /post/2007/12/The-Dangers-of-Static-Events-In-User-Controls.aspx
permalink: /2007/12/the-dangers-of-static-events-in-user-controls/
dsq_thread_id:
  - "78520841"
categories:
  - .NET
---
<p>Static events in user controls can lead to all sorts of weird behavior in your application. Especially when they are hosted in forms that are loaded and unloaded during the lifetime of your application.</p><pre class="code"><span style="color: blue">public partial class </span><span style="color: #2b91af">FlexiAddress </span>: <span style="color: #2b91af">UserControl
</span>{
    <span style="color: blue">public static event </span><span style="color: #2b91af">EventHandler</span>&lt;<span style="color: #2b91af">AddressChangedEventArgs</span>&gt; EventAddressChanged; 
</pre>
<p>The danger here is that unless you unhook from the static event before your form closes what happens is that although the form is not visible it still hangs around in memory until your application exits. </p>
<p>So if you are showing the form by creating a new instance, every form that is created is loaded into memory and will actually cause a memory leak.</p>
<p>If you want to prove this to yourself the easiest way is to include a Debug.WriteLine in the even handler and then after you've opened and closed the hosting form a couple of times try to do an action that causes the event to be fired. You'll notice that the Output window has one line for each instance of the form that is loaded in memory.</p>
<p>The solution, is to remove the hook to the event handler, the Form_Closing event is probably a good place to include this. </p><pre class="code"><span style="color: #2b91af">AddressControl</span>.EventAddressChanged -= AddressControl_EventAddressChanged;</pre>
<p>The better solution though is to avoid using static events.</p>