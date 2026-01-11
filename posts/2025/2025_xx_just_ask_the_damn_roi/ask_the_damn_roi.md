---
title: "Just Ask The Damn ROI"
author: "DS Rants"
date: "2025-11-31"
categories: [data science, software engineering, tests, best practices]
# image: image.png
# draft: true
# draft-mode: visible
---

Hell, you're deserving a goddamned answer!

Indeed today we are going to develop a mass murder weapon because we are going to face the apocalypse.
Today, we are tackling the problem of zombie projects that should have met their demise long ago.
These lifeless abominations are wasting enormous resources and everyone's time, only because some people do not want to face reality or cannot simply say the word: "No".
The expected Return On Investment (ROI) is your best nearby weapon to fight those beasts!

We will start by removing some obvious considerations when people show some good will and a shred of decency.
for instance, they may have a reasonable ROI estimation with sensible error margin (you have no idea of your sheer amount of luck).
Alternatively, they could be overly-optimistic, yet open to discussion, in which case your role as a data practitioner is to confront their numbers with better ones.

Our real problems arise when nobody has even tried to do some basic maths or even thought about assessing the project viability.
You'd be surprised how few people actually ask themselves this question, because for them its utility is "so obvious".
The main point of this rant is that 90% of the time when facing such situation no doing anything is the best course of action.

# A Missing ROI Estimation Is A Bad Sign

Indeed everyone, myself included twice over, think the latest idea they just pulled out of their asses will be the new Sun God.
So we need to write down a basic set of expectations that forces us when not met to mercifully terminate a failing stupidity with a double tap of .357 Mag.

Yet in a lot of places ROI is completely overlooked.
A certain times it can be difficult to estimate especially when estimating is so foreign to the current culture.
Similarly, a poorly defined scope can be a big obstacle to the ROI calculation.
These obstacles are real, but they should be on the contrary reasons for us to precise our expectations.

Despite this, people are forced to work on projects whose outcomes are beneficial to almost nobody.
Sometimes some of them are outright fully dystopian and go against any regulations with an absolute disregard for any legal considerations...
In order to avoid these pitfalls we need to have an intellectual tool that is easy to apply.

## Using Costs To Perform Napkin Calculation

For that we need to have a basic idea of labor costs because it is usually the main spending budget in most IT domains.
We will stick to 5th grade math, because nobody during a meeting can do anything more elaborate than that.
Beside the whole point here is to get rid of corporate bullshit and executive self-delusions, not to assess the viability of the project against all possible outcome.

For that, we need a general range of the salary for your region of choice.
Then we need a rough multiplier to estimate the total cost for the employer for a given raw salary.
Finally, you can calculate the hourly, weekly and yearly costs, using the number of worked hours or weeks in your region.

Here is how it looks for some generic data practitioners in the EU and US (Yes, I know Chad, your 500k$ salary for creating your dummy uber-startdown ripoff is not listed here):

| Origin | Base Salary | Multiplier | Hourly Employer Cost | Weekly Employer Cost | Yearly Employer Cost |
| ------ | ----------- | ---------- | -------------------- | -------------------- | -------------------- |
| EU - € | 50K - 80K   | 1.45       | 40.3 - 64.4          | 1600 - 2600          | 72K - 116K           |
| US - $ | 100K - 200K | 1.3        | 72.2 - 144.4         | 2900 - 5800          | 130K - 260K          |

Note that this numbers are conservative, because the multiplier is here to account most of the alleged "hidden" costs for the employer.

Now, pick on number that is easy to remember for each time horizon, not more because you sure as hell are not smart enough for more.
Here are mine for Europe: 60€/hour, 100k€/year, and 2500€/weak (which conveniently rounds up to 10k€ per month).
This allows me to be conservative but again the point here is just to have a ballpark idea how what people cost.
You need to be able to do the same maths your CEO does when he's about to fire your ass to improve his ratios before his shareholder meeting!

Now, whenever some random genius comes up with a project that requires 4 full-time engineers, you can say in a split second: "Your stupid pet project better be delivering **at least** 400k€ per year, **in the worst possible conditions** otherwise I will legally mandated to perform a cervical dislocation without prior anaesthesia!".

The question you should aim to answer is: I am about to spend a potentially large amount of time on this project, does it have any chance to produce anything even remotely useful or financially sensible?
Anything that does not meet this simple criterion has a 99% chance of being a pointless self-jerking play that should be torched right here, right now, for everyone's benefit.
Think Ellen Ripley in "Alien" not wanting to open the airlock because of possible contamination, this is your new job now!

Sadly, many projects are immune to this very strong power, because you know, companies are the pinnacle of efficiency...
Regardless, it is worth knowing that certain types are worse than others.

## Typology Of Failed Project Without Estimated ROI

You are almost certain to encounter in the wild some projects that are doomed to fail, but still receive enough political support, enthusiasm from blind colleagues or simply fly under the radar.
Let assume for the argument' sake that your management requires your presence on this monstrous beast.
Depending on certain aspects of the zombie itself (and your personal situation), you could go from tolerating the situation to updating your resume and getting a ticket on the ejection seat for a prompt exit.
This is mostly based on how clueless or worse malevolent the people around you are:

1. It can be treated as a research project.

   With reasonable movement margin, support from coworkers, and decent skills it might still be possible to produce some decent bits of knowledge.
   Let's be honest, it's probably not the worst situation to be in, unless you are facing crazy expectation from management.
   As long as people are more or less conscious that they are burning money, with a fairly low probability of positive outcome.
   Otherwise you can just head to the next point.

1. It's corporate inefficiency at its finest!

   This means your chances of producing anything of value take a drop each time a clueless manager opens their mouth to speak about your project.
   In which case, you are definitely going to need some allies, and pretty good ones at that.
   Particularly, you're going to have to convince lots of people that embedding quality inside the project is not an overly defensive attitude, but the equivalent of putting on your seatbelt and checking your tires before crossing half the continent.
   It's going to take lot of efforts and a insane self-imposed disciple to overcome the contradictory injunctions you receive from your environment.
   The question remains are the promised rewards (if any) worth the effort you are about to deploy?

1. It's a political play!

   Well, you're clearly screwed, utterly doomed and absolutely fucked!
   Now, your objective is to save the only things that can be saved: yourself and your career.
   Produce something at all cost, just produce something to throw at the mouth of the monstrous executives to appease their greed.
   Stall time until you switch to a different position or company, because you don't want any responsibility when this cluster-fuck is falling apart!
   There is no God, she has left the channel!
   Everything is permitted: watermelon KPI, hardcoded lying stupidity for demos, blame shifting or kick in the nuts.
   This thing is aiming straight for the iceberg and you don't know how to swim...

Depending on your personal resilience and morbid satisfaction to head straight for burnout town, you can always try to tolerate some of this, but now you have been warned.

# Save Your Sanity

The point of demanding a ROI is not because I want to live in a libertarian dystopia where one should only work on things that generate clear money and similar outcomes.
Quite the contrary, I want you to retain control over your life.

## Save Yourself

I believe it is basic human right to work on something that is not a complete garbage dumpster setting money on fire.
At the very least, you have the right to know when you are working on the latest ludicrous fantasy of the upper management.
In the perspective, there is a huge difference between having even a rough ROI estimation versus knowing generally and intuitively.
With the numbers you can pretend to align yourself with your company goals (enriching their shareholders and executives) to make your situation more bearable.

Being aligned (loosely) with your company goals such as not setting money on fire, or not wasting everyone's time, give a few benefits:
First, exercising the spectacular ability to say the magic word "NO" is very powerful.
It needs to be used with measure otherwise people will think you are not a "team player", "not constructive", always shitting on others, and that again my dear reading friend is no bueno.
You will start to see increasing amounts of shit that people try to shove down your throat because you have pierced the veil of ignorance.
Pick your battles, sometimes let it slide, or train your coworkers to replace you instead, contrary to the [Immortals](https://highlander.fandom.com/wiki/There_can_be_only_one) there can be more than one...

Second, you can become quite quickly a credible stakeholder because suddenly you consider a larger scope than your notebook.
As direct consequence, people will likely consult you more on high profile stuff.
Although as mentioned some will not like it when you pour liters gasoline on their stupid projects.
But everything is fine, their screams and the bonfire is what will bring joy to your soul.

Finally a more evanescent aspect regarding this alignment with profitability, is the progressive development of your ability to form a judgement of your current projects that goes beyond "The whole thing is a mess".
Not only that, it will also improve your ability to transmit your vision to upper management, because you will start to speak a different language.
This is the hidden language of the executives, where one devises strategy, moves pawns and allocates resources and time.

## Save Tour Time

Similarly, it is critical for engineers to safeguard some time from the greed of their managers or dissociating executives in order to alleviate the pressure coming from the business.
Knowing the expected ROI on a project is precisely a weapon for this.
The point is to consciously choose when to work on the high-profile high-return project and when to take time to work on something else entirely because you're a fucking adult!

Indeed, you should have some time to allocate to things that have **apparently no up-front value** for your company.
In order to develop the creative part that is mandatory to do a good job in our profession, you will need some time to learn completely new things, or better understand some foreign concepts.
Getting to know a new framework or programming language, understanding roughly what are conflict-free replicated data types (I don't...), or being able to read a bit of assembly are valuable skills even if you don't use them in your day job!
For the screeching workaholic in the background, vacations and sick days are not meant for that...

This ability to do something that is not tied to your stupid yearly objectives nor imposed by scrum-junkies overlords, is critical to the development of your IT culture.
How are you going to know that there are better ways to manage your data pipelines when your are so neck deep into bug-fixing?
You will not be able to see that on the other side of the street some people can actually sleep because their projects have motherfucking automated tests executed on a perfect and independent replica of the prod, deployed in minutes thanks to a merciless CI/CD.

You need time to learn all of this.
You need time to be able to learn how to do your job correctly.
Time is your one of your most precious resources.
Knowing what outcomes you can expect from a given project is an excellent way to better allocate and retrieve control over your time.

## Set Up The Right Context For Incremental Improvement

With what I described so far, one person without charitable intentions might be tempted to put the following words into my mouth: "Well, from now you should work only on projects that have demonstrated from the start that they are going to deliver value".
My answer to this statement is: **Bullshit!**

Indeed, their is a tremendous difference between producing a rough estimate, even better an interval, and publishing a financial report before the project even began.
This brings us to necessarily explore the difference between project framing and waterfall approach through the lenses of DevOps and Continuous Delivery philosophies.

There is a clear difference between establishing a air-tight battle plan from the start (waterfall) and making sure that expected outcomes align the the company capabilities, resources and plain ol' reality.
I'm a very strong defender of approaches that aim to maintain velocity of development through the project lifecycle.
As a consequence designing your system to encourage learning, trials and errors, while safeguarding your ability to correct the scope, are extremely valuable in this perspective.
Indeed these principles are core components of the efforts required for Continuous Delivery.

But Continuous Delivery does not mean we need to stop any effort to establish the boundaries of our system, or estimate the likely outcomes.
What continuous delivery suggests is that our initial assumptions are unlikely to be correct in the long run.
In terms of ROI, this means we should periodically revisit our calculations, because some of these assumptions will become completely moronic.
The unexpected things that are bound to happen through the project lifetime might completely change what we could hope to achieve, sometimes for the better some other times for the worse.

# Conclusion

Whenever someone asks you: "Can you _just_ do that for me? It will be quick.", I strongly urge you to ask for the ROI and do the maths in your head.
What you decide afterwards is up to you, but intellectual murder is always an option.
At least now you have the numbers to justify your decision.
Think about that the next time you are pulled in a meeting with 20+ people, just multiply by the numbers you picked, tally everything, and breathe out...
We are all going to need to take a motherfucking step back.
