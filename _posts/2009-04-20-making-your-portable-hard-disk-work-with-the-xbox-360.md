---
id: 576
title: Making your portable hard disk work with the XBox 360
date: 2009-04-20T10:12:12+00:00


guid: http://merill.net/2009/04/making-your-portable-hard-disk-work-with-the-xbox-360/
permalink: /2009/04/making-your-portable-hard-disk-work-with-the-xbox-360/
dsq_thread_id:
  - "77730650"
categories:
  - Tips
tags:
  - format
  - hard disc
  - portable
  - xbox 360
---
<p>I like using my XBox as a media center. But when I plugged in a portable HDD to the 360 but it didn’t show up as a disc. Didn’t work on the Samsung home theatre as well. A quick google and I figured out the disc was formatted as NTFS (right-click Properties on your drive to check) on which is not supported by the 360. </p>  <p>Okay so backed up the data and when I try to format as FAT32 there is no such option on the Explorer ‘Format’ dialog. It’s either NTFS or exFAT, couldn’t figure out if the 360 supported exFAT (should have tried) so went about trying to format from the command line. Which does have a switch for FAT32.</p>  <p>Unfortunately format.exe complains that the partition is too big. What I should not have done was to try a quick format. </p>  <p>Instead I went about deleting the partition as mentioned by several sites. There’s a good one built into Windows (Disk Management) that you can get through from ‘Computer Management’. So right-clicked on the external disc and did a ‘Delete Volume’. And then right-clicked and created a new volume. [NOTE: I think the whole delete and create a new volume can be skipped if you already have the partition in NTFS).</p>  <p>Next tried the format.exe again. Still fails complaining that the disc is too big. At whim tried formatting without the /Q (quick format) option. Worked fine.</p>  <p>Here’s how you would go about it (replace Q: with the drive letter of your portable disc).</p>  <p><font face="Courier New">C:\&gt;<strong>format Q: /FS:FAT32</strong> </font></p>