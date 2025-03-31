---
title: Device filter > Device platform
description: ""
date: 2023-08-23T13:12:44.070Z
preview: ""
tags: []
categories: []
---

When designing a conditional access policy and have the choice between using device filter and device platform always use device filter.

The catch is that device filter can only be applied to managed or hybrid joined devices.

It's a limitation since you can't use it with unmanaged devices, but that is exactly the reason why it is better to use it over device platform when your CA policy is targeting managed devices.

The device platform relies on the user agent string which can be easily spoofed. Nicola has a good write up on this over at [Bypassing Conditional Access Device Platform Policies
](https://tech.nicolonsky.ch/bypassing-conditional-access-device-platform-policies/)

![He man skeleton recommends using device filter over device platform]({{ site.url }}{{ site.baseurl }}/images/uploads/devicefiltervsdeviceplatform.jpg)