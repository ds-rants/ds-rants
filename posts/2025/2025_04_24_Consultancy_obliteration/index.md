---
title: "The Glorious One-Shot At Consultancy Obliteration"
author: "DS Rants"
date: "2025-04-24"
categories: [data science, grifters, consultants]
draft: true
draft-mode: unlinked
---

## The Recap

Sorry, dear readers, this is a multi-steps story.
For those currently boarding the train, here is a quick recap of the situation: The _big consulting firm_ was offering for a few **millions euros** (clearly pocket money...) to create one a solution to analyze JIRA tickets and deliver another machine learning project around stock prediction ([See more details here](../2025_04_19_Cancel_A_5.7M$_Deal/index.md)).
Your servitor, completely clueless, did a little bit of data analysis that made the JIRA solution irrelevant.
With the help of a very competent colleague, we demonstrated that the code for the ML project had been regurgitated by a junior high on vibe-coding kool-aid.
In the next 10 minutes, we also showed that for the _seniors_ reading logs and CPU loads on a Web GUI was beneath them and/or outside their skill set.
Too bad, that would have helped them understand why their solution was not working.

As a result, the negotiations for the several million contract were short, and the _big consulting firm_ was kindly requested to keep their incompetent hands off the code and stick to their primary area of non-expertise: powerpoint and global strategy.
Sadly, it's impossible to completely get rid of leeches in large industrial companies, but hey... you have take the small wins.


## The Set-Up

With the audit we made, a few recommendations were given to remove the garbage from the existing code base, and produce something that has a minor chance of working.
They were overall pretty simple:

1. Don't do garbage within your pandas code (No for loops, pretty please).
    - Estimated rework time: 2 weeks for a senior.
    - Extremely high potential for faster execution
2. Reduce general complexity and improve design:
    - Estimated rework time: 1 month for a senior.
    - Few gains for execution time, but necessary for maintainability.

Less than a week later, as the _big consulting firm_ is about to stop working on the code, and hand-over everything to my colleagues in a couple of weeks, we suddenly receive an invitation for a meeting: "last improvements and hand-over".
As I am not working directly on the project, I reluctantly accept the invitation.
I hate the smell of code garbage in the morning...

## The First Bloodbath Smashing Consultant Brains

The meeting starts, they are 2 of them _"seniors"_, 5 of us including on product leader for the department.
The atmosphere is tense. They don't like me one bit, good, neither do I...

> Thank you for being here, we'd like to show you the last ameliorations we did on the project before we leave things to you guys. We used multi-threading to significantly improve the performance of our code, and it should now scale.

Some of you know where this is going...I thought:

> Wait,... what? Multi-threading? On pandas code so dumb that it could have been written by my dead grand-ma' tripping on codein?
>
> What about the low hanging fruits for performance we showed them?
> What about the so needed design improvements for maintainability?
> None of that obviously.

They start showing the very simple Merge Request, telling us how they managed to improve the running time.
Something is off, something is fishy.
I quickly use my ultimate power: the all-seeing eye.
I open their project in the GCP console, navigate to the Machine Learning pipelines.
Their previous garbage pipeline ran in 4 hours, a new one has been running for...

I now feel the taste of blood between my teeth. I yearn for their demise.
I will inflect permanent damage on them.
From this point, I a not a Data Scientist, I morphed into the most dangerous and ungodly species on earth, not even human anymore... I am now a lawyer.
Because, the only thing I have for them are questions, but of the most dangerous kind, the kind for which you already know all the answers...

The smell of blood goes up to my nose...

> Can you please give me the commit ID of your merge request? I asked innocently.

The trap has already been set in motion. I already looked a the tags on the pipeline that has been running for ... I know which commit trigger it.
It's theirs.
And sadly for them, I like to play with my food before I eat it.

So I let them look for the commit ID. They give it to me. I double-check. I triple-check. And then:

> Do you guys know that your pipeline has been running for **4 DAYS**?
> Can you tell me how you manage to improve a runtime of 4 hours to **4 DAYS**?

The smell of Death is everywhere...

## A Case Defense Of Casey Muratori: Non-Pessimization Vs. Optimization

Sorry, I am not sorry about the orthographic pun.
