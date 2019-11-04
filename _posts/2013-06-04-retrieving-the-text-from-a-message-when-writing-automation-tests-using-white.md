---
id: 858
title: Retrieving the text from a message when writing automation tests using White
date: 2013-06-04T23:03:58+00:00


guid: http://merill.net/?p=858
permalink: /2013/06/retrieving-the-text-from-a-message-when-writing-automation-tests-using-white/
dsq_thread_id:
  - "1359712877"
categories:
  - Tips
tags:
  - automation
  - testing
---
Quick tip on how to retrieve the value of a message box when writing automation tests using [White](https://github.com/TestStack/White) for Windows desktop apps.

	var dialog = window.MessageBox("ERROR");
	return dialog.Get<Label>(SearchCriteria.ByControlType(ControlType.Text)).Text;
