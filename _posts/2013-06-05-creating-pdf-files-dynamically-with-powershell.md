---
id: 861
title: Creating PDF files dynamically with PowerShell
date: 2013-06-05T10:04:51+00:00


guid: https://merill.net/?p=861
permalink: /2013/06/creating-pdf-files-dynamically-with-powershell/
dsq_thread_id:
  - "1361822114"
categories:
  - Tips
tags:
  - pdf
  - powershell
---
So how does one go about creating PDF files dynamically? You need a pinch of the open source [PdfSharp](http://pdfsharp.net) library and 10 lines of PowerShell.
 
	Add-Type -Path .\PdfSharp.dll
	$doc = New-Object PdfSharp.Pdf.PdfDocument
	$doc.Info.Title = "Created dynamically"
	$page = $doc.AddPage()
	$gfx = [PdfSharp.Drawing.XGraphics]::FromPdfPage($page)
	$font = New-Object PdfSharp.Drawing.XFont("Verdana", 20, [PdfSharp.Drawing.XFontStyle]::BoldItalic)
	$msg = "Hello World"
	$rect = New-Object PdfSharp.Drawing.XRect(0,0,$page.Width, $page.Height)
	$gfx.DrawString($msg, $font, [PdfSharp.Drawing.XBrushes]::Black, $rect, [PdfSharp.Drawing.XStringFormats]::Center)
	$doc.Save("HelloWorld.pdf")