---
title: "The Glorious One-Shot At Consultancy Obliteration"
author: "DS Rants"
date: "2025-04-24"
categories: [data science, grifters, consultants, stupidity]
draft: true
draft-mode: unlinked
---

## The Recap

Sorry, dear readers, this is a multi-step story.

For those currently boarding the train, here is a quick summary of the situation: The _big consulting firm_ was offering for a few **million euros** (clearly pocket money...) to create one solution to analyze JIRA tickets and deliver another machine learning project around stock prediction ([See more details here](../2025_04_19_Cancel_A_5.7M$_Deal/index.md)).

Your servitor, completely clueless, did a little bit of data analysis that made the JIRA solution irrelevant.
With the help of a very competent colleague, we demonstrated that the code for the ML project was a regurgitation from a junior high on the vibe-coding Kool-Aid.
In just 10 minutes, we also showed that for the _seniors_ reading logs and CPU loads on a Web GUI was beneath them and/or outside their skill set.
Too bad, that would have helped them understand why their solution was not working.

As a result, the negotiations for the several million contract were short, and the _big consulting firm_ was kindly requested to keep their incompetent hands off the code and stick to their primary area of non-expertise: PowerPoint and global strategy.
Sadly, it's impossible to completely get rid of leeches in large industrial companies, but hey... you have to take the small wins.

## The Set-Up

With the audit we made, a few recommendations were given to remove the garbage from the existing code base and produce something that has a minor chance of working.
They were overall pretty simple:

1. Don't do garbage within your pandas code (No for loops, pretty please), with a high potential for faster execution and a limited amount of work for a senior (probably a couple of weeks).
2. Reduce general complexity and improve design, which should yield fewer gains for execution time but is necessary for maintainability, and requires more time to fix.

Less than a week later, as the _big consulting firm_ is about to stop working on the code and hand over everything to my colleagues in a couple of weeks, we suddenly receive an invitation for a meeting: "last improvements and hand-over".
As I am not working directly on the project, I reluctantly accept the invitation.
I hate the smell of code garbage in the morning...

## The First Taste Of Blood

The meeting starts, there are 2 of them, _"seniors"_, and there are 5 of us, including one product leader for the department.
The atmosphere is tense. They don't like me one bit. Good, neither do I...

> Thank you for being here, we'd like to show you the last ameliorations we did on the project before we leave things to you guys. We used multi-threading to significantly improve the performance of our code, and it should now scale.

Some of you already know where this is going... I thought:

> Wait,... what? Multi-threading?
>
> On pandas code so dumb that it could have been written by my dead grandma tripping on codeine?
>
> What about the low-hanging fruits for performance we showed them?
> What about the so-needed design improvements for maintainability?
>
> None of that, obviously.

They start showing the very simple Merge Request, telling us how they managed to improve the running time.
Something is off, something is fishy.
I quickly use my ultimate power: the all-seeing eye.
I open their project in the GCP console, navigate to the Machine Learning pipelines.
Their previous garbage pipeline ran in 4 hours, a new one has been running for **[REDACTED]**.

I now feel the taste of blood between my teeth. I yearn for their demise.
I will inflict permanent damage on them.
From this point, I am not a Data Scientist, I morph into the most dangerous and ungodly species on earth, not even human anymore... I am now a lawyer.
Because the only thing I have for them are questions, but of the most dangerous kind, the kind for which you already know all the answers...

The smell of blood rises to my nose...

> Can you please give me the commit ID of your merge request? I asked innocently.

The trap has already been set in motion. I already looked at the tags on the pipeline that has been running for **[REDACTED]**. I know which commit triggered it.
**IT'S THEIRS.**
And sadly for them, I like to play with my food before eating it.

So I let them look for the commit ID. They give it to me. I double-check. I triple-check. And then:

> Do you guys know that your pipeline has been running for **4 DAYS**?
> Can you tell me how you managed to improve a runtime of 4 hours to **4 DAYS**?

The smell of Death is everywhere...

## The Wounded Consultants Attempt To Fight Back

The silence is deafening.

> - "Well, I set this up on my local installation and it reduced the processing time from 2 hours to 1 hour." says _big firm consultant_ (BFC) N°1.
> - "Are you telling me it works on your machine?" I ask slowly. "I will point out that the only thing that matters is that it runs on GCP, everything else is useless...".
> - "Sure, sure... there seems to be an issue with the current version of the code...".
> - "That's the least you could say." as I utter these words, and thus strike the first blow to the leg.
> - "I don't seem to have the possibility to stop the current job from running, do you..."
> - "There, it's already dead..." I say with an awoken appetite from killing the server job and already looking for another prey.
> - "Thank you, there seems to be a different behavior on the distant machine," says BFC N°1.
> - "Yes, you're attempting to spread the load on multiple threads or CPUs, but the behavior is highly dependent on which hardware you run it. You did not check that, this seems highly unprofessional." I continue calmly but now trying to bite their arms.
> - "That's not right, you have no right to call us unprofessional," interceded BFC N°2.
>   "You only reviewed our code and only gave negative feedback.
>   There was nothing constructive in what you said."
> - "We did give you constructive feedback. When we handed our audit report, we pointed out two areas of the code base where the major bottlenecks were.
>   They consist of 2 blocks of 15 lines each filled with poor pandas code.
>   We even showed them to you live in our first meeting, by just reading the logs.
>   For some reason, you decided to address the problem very differently," I say slowly, boiling with rage and fueled by anger.
>   I decide to push through and continue with a direct attack.
>   "Besides, on your previous runs, the CPU load was around 15-20% and now it's peaking at 1%. Whatever you did made the situation clearly worse.
>   You did not check that your _'optimization'_ actually works on the hardware running the job."

At this point, another senior MLOps engineer intervenes.
The dude is a totally legit contractor, probably better than I am in many areas, with really strong software engineering skills.
He rightfully points out that we can look at the logs to see what's really going on, and try to figure out why the job was stuck.

The opportunity for a killing blow will come later.

I retreat to my cave, still growling...

## Spiraling Down Into Madness

The logs are a clusterfuck, with only the message "A job is running" every minute for 4 whole days.
The reason behind this: when a Kubeflow job is running for a long time, there is basically a signal sent every minute to tell the user: "Hey, I'm still alive".
We only see that.
The other senior tells the two consulting clowns to go back to the very beginning of the job. They update the search.

Quickly, it appears that the job got stuck in a very particular place, right after the start of the program.
Where? In the same fucking preprocessing function that we uncovered in our audit!
What are the odds? (Dear concurrency experts reading, if you know exactly where this is going, I apologize.)
Who would have thought that sweeping garbage under the carpet does not make your room smell like orange perfume?

I sense some exasperation pearling through the words of my colleague:

> "How many threads did you set up for this job?"

We take a closer look at the merge request. Motherfucker, They put **16**. My colleague quietly says:

> "I believe you have put too many threads in your configuration and the CPU is in a deadlock."

Calling it a deadlock at this point is making them a favor.
The CPU is not locked, it is basically being chocked to death by the most absurd computer BDSM practice of the year.
This guys managed to send one of the beefiest Kubernetes machine directly in a drooling vegetative state, banned for eternity in the quantum dimension.

Again, trying to run concurrently multiple versions of the same dumpster code, what are the odds that something fucking stupid will happen?
My colleague adds another couple lines:

> "As we tried to tell you earlier, the behavior of a sub-process or a multi-threading job is highly dependent on the hardware actually running the job."
>
> "The optimization you did locally does not work on the Kubernetes cluster running your job because the hardware is fundamentally different from the one on your machine."

I'm stepping out from my cave, craving for blood and violence...

## A Methodic Verbal Annihilation

> "It appears that your solution is useless." I say.

The room is silent. A storm is coming. The consultants are frozen by fear. I can sense it. The Grim Reaper smiles...

> "You have put multi-processing on code that was deeply defective in an attempt to hide its mediocrity. You tried to call this an optimization but it made the situation worse in all aspects."
>
> "You did the same mistakes as last time, you did not even check that the job was running properly, you did not check the logs, you did not check the CPU load, all of which is one click away in the web GUI."
>
> "And finally you call everyone in a meeting, saying: 'We improved the situation', and nothing works! This is what I call highly unprofessional!"

The consultants lay there, silent, brain-dead, skulls cracked open.

## The Aftermath

We quickly end the meeting there because there is nothing more to discuss.
The good thing is that one representative of the business side witnessed the whole exchange.
The Senior Engineer and I repeat a few additional pieces of information, in order for him to fully grasp the details of the situation.

I ask him for a favor, because I saw the _leeching consultants_ record the Teams meeting but we don't have access to it. He kindly accepts to petition them for a copy of said recording.

To this day, we are still waiting for a reply to this email request.
