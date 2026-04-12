---
title: "Using Pester to regression test Maester tests"
description: "Quick write up on regression testing and refactoring with Copilot."
date: 2025-04-18T08:00:00.000Z
preview: ""
tags: []
categories: []
---

![Pester tests for Maester](/images/uploads/2025/pester-maester-header.png)

*Pester tests for Maester tests!*

I was fixing a Maester bug and thought it would be good to share my process for going about it.

We start off with a Maester bug ([Issue with MT. 1016 #804](https://github.com/maester365/maester/issues/804)). In this instance the tenant had a CA policy for All Users but did not have one explicitly targeting guests.

> While it's always a better practice to have a separate set of policies for guests, Maester should not penalise them for this. Technically they are in the clear since MFA being applied to all users including guests.

Now the existing code for this check was getting too long and adding more parts to this expression was going to make it hard to maintain.

![Original code for Guest MFA check](/images/uploads/2025/pester-original-code.png)

GitHub Copilot to the rescue! I prompted and got a much cleaner implementation and was able to add the additional check.

![Refactored code for Guest MFA check](/images/uploads/2025/pester-refactored-code.png)

Now we need to test if it's working as expected. This involves creating a bunch of CA policies to test and how do we make sure it keeps working with future changes?

That's where Pester tests come in. I created a bunch of Pester tests to simulate various types of CA policies. Some targeting all users, others targeting just guests and also checking if any type of guest had been excluded.

![Pester tests to validate Test-MtCaMfaForGuest](/images/uploads/2025/pester-tests.png)

How I went about this was copying out the json of the CA policy. This one here targets guests but excludes the B2B Collab Guest type. This type of policy should be failed by Maester since the tenant is missing an important chunk of guest users being required to have MFA.

![JSON of CA policy used for mocking tests](/images/uploads/2025/pester-ca-policy-json.png)

- Maester Test: [Test-MtCaMfaForGuest.ps1](https://github.com/maester365/maester/blob/main/powershell/public/Test-MtCaMfaForGuest.ps1)
- Pester Test File: [Test-MtCaMfaForGuest.Tests.ps1](https://github.com/maester365/maester/blob/main/powershell/tests/functions/Test-MtCaMfaForGuest.Tests.ps1)
