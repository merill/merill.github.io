---
title: Invoke-MgGraphRequest -OutputFilePath vs Out-File Performance Comparison
description: "Which is faster? Using Invoke-MgGraphRequest -OutputFilePath vs Invoke-MgGraphRequest | Out-File"
date: 2024-07-22T07:03:08Z
preview: ""
tags: []
categories: []
---

In case you were wondering which is faster.

```powershell
Invoke-GraphRequest -Uri 'beta/users' -OutputFilePath ./user.json
```

or

```powershell
Invoke-GraphRequest -Uri 'beta/users' | Out-File -FilePath ./user.json
```

Surprisingly, the answer is that Out-File is the fastest

Here's what I got when I ran the two commands:

```powershell
Measure-Command { Invoke-GraphRequest -Uri 'beta/users' -OutputFilePath ./user.json }

TotalSeconds      : 3.1084942
```

```powershell

Invoke-GraphRequest -Uri 'beta/users' | Out-File -FilePath ./user.json

TotalSeconds      : 0.5016927
```

That got me thinking. Does the performance change much when using different output types?

```powershell
Measure-Command { Invoke-GraphRequest -Uri 'beta/users' -OutputType Json | Out-File ./user.json }

TotalSeconds      : 0.4035508
```

Here's what I get when I ran the same command with different output types. There was no clear winner and they all ranged between 0.2 and 0.5 seconds.

| OutputType          | TotalSeconds |
| ------------------- | ------------ |
| Json                | 0.4035508    |
| Hashtable           | 0.3948994    |
| PSObject            | 0.4495978    |
| HttpResponseMessage | 0.5539832    |
