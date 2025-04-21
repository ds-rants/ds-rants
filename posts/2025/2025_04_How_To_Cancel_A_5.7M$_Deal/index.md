---
title: "How To Cancel A 5.5M$ Deal"
author: "DS Rants"
date: "2025-04-19"
categories: [data science, grifters, consultants]
draft: true
draft-mode: unlinked
---


There are some days where you feel like your work is pointless, void and without a meaning. But thankfully there are also fewer days when you feel and know that you actually made a difference. By working in data science, and more broadly in software engineering, it is particularly easy to loose a sense of purpose and become overwhelmed by the sheer amount of bullshit that tend to plague our profession. However I have never felt more helpful than when I contributed to cancel a small contract of 5.5M$ with a **very large and influential consulting firm**.


## The First Nail In The Coffin

On a very innocent day, I was innocently asked by my manager to start working on a high-profile / potentially political subject with the DevOps teams. It was mostly about framing a use-case because they were willing to use AI (of course) to analyze their tickets and improve their workflow. As I was frequently collaborating with other devops people, so it made sense for me to be onboarded on this subject. Thankfully my manager and I were both on the same page, as it clearly seemed like a classic case of someone committing the heinous crime of  bootstrapping chatGPT on everything because AI is going to solve all our problems, right? So we decided I was just to do a little bit of data analysis on those tickets to see if it can provide the insights they were looking for, and hopefully avoid a complex over-engineered system. And here I have to make a side note, because I am fortunate enough that my current manager is a technical person and she shares a similar aversion to bullshit as I do. If you are under the type of person that tends to jump on every shiny hype, because they are addicted to LinkedIn posts, you have my deepest sympathy.

As you probably guessed from this portrait, this use-case ended fairly simple, they even already had a few rules to extract information from tickets based on a few regexes. I just re-used these, made them a little more generic, sprinkled a few visualizations, added one logistic and one linear regression, talked with the DevOps managers and higher-ups, and... that was it. That was all they needed.

I learnt only a few weeks later that this subject was under a lot of scrutiny because the **big consulting firm** was attempting to embezzle a few millions from us. They were attempting to sell a AI based system to automatically analyze those tickets, promising high ROI, better synergy and faster treatment times before they even started working. Obviously they were going to request a lot of money for this high-end ~~con~~ service.

So my little shenanigans already showed in broad day light that their solution was completely unnecessary. And I have to insist on something crucial here, there was nothing I did here that was outside of the scope of the second or third week of your average data science bootcamp. Plain simple.


## The Second Nail In The Coffin
**Warning:** This rant is a follow-up to some events described at [the end of this post](../../2025/2025_04_your_pandas_code_is_bad/index.qmd), where a coworker and I was had a pleasure to audit a outstanding piece of garbage code produced by this big player of the consulting world. The one page report we produced was basically a call for a human sacrifice to appease the wrath of the gods in face of the insanity they dared try to release in the wild and call a product.

Little did I knew that around the time of the audit, that these *highly* skilled fraudsters/consultants where basically trying to play a particularly wicked game. The first part was to convinced us that the garbage proof of concept they hacked together was unlikely to scale because of communication and hand-over issues, or poor performance of our infrastructure (it's Google's BTW...), or because of the alleged lack of skills of our in-house data scientists. Or all of them, because then blame shifting becomes so much more effective. But the second and most appalling part was that they were also trying to renew there support contract with our firm. And as you can already guess from the title they were not talking pennies. No they were talking multi-year support to fully integrate their crappy piece of work in our environment, and I don't know how many full-time engineers.

Fortunately, sometimes organizations work, and our little report calling their bullshit managed to find its way to some part of the higher management. This included some of the people that intended


> By the way if you ever feel uneasy about your salary, just know that this particular consulting firm charges around 1000€/day for a junior and 5000€/day for the *seniors*, and that was probably a discounted price because our firm was a large customer. Yet in the best case scenario, which in our case meant 1 junior and at least 2-3 seniors managed to produce a machine learning code for which:
>
> - Predictions take more time than the training (on a similar amount of data).
> - None of them even thought about looking at the logs they themselves wrote.
> - None of them thought about looking at the CPU / RAM load which is 2 clicks away in the GCP console.
> - None of the seniors even bothered to look at the junior code in case there was something bad.
>
> So if you have impostor syndrome, believe me, you're probably fine.


## Why Do You Hate Consultants So Much?

Because everyone in their right minds should. The primary reason behind their dreaded existence is to repeat to their clients what all their other clients are doing (who spoke about large-scale industrial spying?). But my major beef with them comes from their sheer technical incompetence coupled with their proportion to wrap everything in pseudo-argumentative bullshit that for some reason seems to really appease the anxiety of the average CEO.

It is even worse when you factor in that their business model which rely largely on sending junior consultants while pricing them as if they were seniors.
