---
id: 737
title: Configure the Belkin Play Max router for SLT ADSL Broadband
date: 2011-09-16T21:57:54+00:00
author: Merill Fernando

guid: http://merill.net/?p=737
permalink: /2011/09/configure-the-belkin-play-max-router-for-slt-adsl-broadband/
dsq_thread_id:
  - "971115777"
categories:
  - Tips
tags:
  - config
  - router
---
I'm on vacation back home in Sri Lanka and became the tech support guy for the in-laws. They were using an old D-Link router which supported just 802.11b and a draft version of g. In short ancient. The house has two stories and a terrace but the wifi wouldn't even work on all the rooms on the same floor.

So I went to Unity plaza and checked out all the routers that are available. Unfortunately there's not much in terms of choice. All of the available routers were the low end versions by D-Link, a few have a low-end Linksys router and some Belkin routers. You also get a handful of Asian brands of which the Unity Plaza sales guys tout the TP-Link as being the best brand, far superior to D-Link, Linksys etc.

I finally settled on the <a href="http://www.belkin.com/IWCatProductPage.process?Product_Id=522112">Belkin Play Max N300+300</a> which sells here for Rs. 16,500/-

I got home plugged it in but couldn't get it to connect to the SLT ADSL. I spent a few hours trying various settings, calling SLT to verify the username/password all to no avail. I finally updated the router from v1.00.45 to <a href="http://en-au-support.belkin.com/app/answers/detail/a_id/4624/~/f7d4401au-play-max-wireless-modem-router---firmware-update">v1.00.46</a> and viola it worked.

The connectivity is really good and I don't have any dead spots in the house.

Here are a few screenshots of the config page for SLT's settings.

<a href="https://merill.net/wp-content/uploads/2011/09/Belkin-Router-Config-PPPoE.png"><img class="alignnone size-medium wp-image-739" title="Belkin-Router-Config-PPPoE" src="https://merill.net/wp-content/uploads/2011/09/Belkin-Router-Config-PPPoE-300x216.png" alt="" width="300" height="216" /></a>

<a href="https://merill.net/wp-content/uploads/2011/09/Belkin-Router-Config-PPPoE-VPI-VCI.png"><img class="alignnone size-medium wp-image-740" title="Belkin-Router-Config-PPPoE-VPI-VCI" src="https://merill.net/wp-content/uploads/2011/09/Belkin-Router-Config-PPPoE-VPI-VCI-300x206.png" alt="" width="300" height="206" /></a>