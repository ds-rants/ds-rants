---
title: "Your Cloud Mistake Is Nothing Until The 1.5 M$ Bill"
author: "DS Rants"
date: "2026-04-01"
categories: [data science, software engineering, tests, best practices]
# image: image.png
draft: true
draft-mode: visible
---
I started writing this on April 1st, and whish it was a joke.

Do you remember the typical horror stories you see on Hacker News where a random bloke spits out: "This little configuration cost us thousand on our cloud bill and almost bankrupted our precious startup"?
Well, let me tell you, this is nothing, you're still talking baby playground.
Some companies bring this to the next level, and I am pretty sure there are even worse people out there, there are just not dumb enough to write their story.

But this one is worth being told, it's about the dilution of responsibilities, poor understanding of key principles of databases, little mistakes spiralling into giant ones because of a buggy software. And Like any good story this one has 3 parts.

## The 40 K$ Rehearsal

T

## The 150 K$

This is the one I know best because I started sniffing around less than a day after it happened.
I was fortunate enough to lay my hands on the actual "code" that could generate a bill able to flatten your average startup 3 km under the ground.

Let's say you have a small database, nothing fancy, only 200 TB of data that is stored in a single table that has no partition, no cluster, no index.
Yes your eyebrows correctly jumped through the ceiling to take a vacation on the rooftop, this in itself is already egregious.
But people are not so malevolent, because this mistake originated in the will to copy everything in a properly managed table with partition and clusters.
Such an operation would at the time of the crime represent a 1000$ bill (200 TB * 5€ / TB of data processing).
So how did things escalated so comically?




## The Final Nightmare
