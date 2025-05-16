---
title: "A Case Defense Of Casey Muratori: Non-Pessimization Vs. Optimization"
author: "DS Rants"
date: "2025-04-26"
categories: [data science, performance, CPU, optimization]
draft: true
draft-mode: unlinked
---

Sorry, I am not sorry about the orthographic pun.

Layout:

The main conundrum is this: There is a finite upper limit for the optimization of a given piece of code but there is no lower limit to how slow and crappy you can make it.

Not convinced? I'll give you a clear practical example to other moronic data scientists like me that have never seen the inside of a compiler.
Look at BigQuery: this stuff is pure magic for processing Petabyte-scale datasets, with almost infinite scalability, and infinite parallelization.
Yet, with the right amount of criminal intellectual deviance, you can still make it as slow as a blind horse overdosing on Xanax that you shot in the leg to give it a good head start.

Now that I have your ameboid brain on board, it's important to

## Definition Of Non-Pessimization And Optimization

1. Optimization:

   > Precisely **measuring, comparing and testing** various properties of your code (speed, throughput, latency...), through various implementations if possible done on **hardware/context similar to its final execution**.

   Difficult, time consuming, few people can do it, only useful for very key components of your system

2. Non-Pessimization

   > Not introducing tons of crap work for the computer to do.

   Accessible to most people with moderate knowledge of a given paradigm/language, applicable almost everywhere, fast.

   I will personally add: it usually makes the code more readable to humans as well...

3. Fake Optimization

   > Trying to do N°1. without measuring, rigorously testing or skills

   Typically happens when people are not able to do step 2. and jump directly to step 1.
   This usually makes things worse for everyone.

   Think people that try to strap multiprocessing/multiprocessing on your average code dumpster fire because "time will _SURELY_ be divided by 4 if I run my program on 4 cores"...

So

> - "But Dr. Rants, how can I possibly know when should I do N°1,2?"
> - "WRONG! N°1 does not exist for you! For you, it's myth! Otherwise you would not need to ask the question".
>   It's plain simple really. If you're trying to do Optimization on a code that bad because you just did not understand the concept of non-pessimization, then you're back to the whack-job N°3!
For you only one thing matter:
>
>   NON-PESSIMIZATION!"

Then comes the **Real** question: How can I make my code not suck?

Casey has a pretty simple answer:

## You Should Know A Bit Of Assembly

This is one the probably hottest takes of Casey, i.e. his focus on having us learn a bit of assembly.
I will paraphrase but the general idea is:

1. You should learn assembly and be able to view your compiled program in assembly.
2. This way you will be able to actually see and understand what HOW you program is doing what you instructed it to do.
3. The instruction set is limited and thus quite simple in comparison to other languages especially high level ones.
4. It makes a tremendous difference to be able to peak under the hood to develop an understanding of how the computer operates, because you removed the middle-man.
5. Even in high-level languages like javascript and python, it is possible to have a look at the low-level code and it's not that difficult.

In short, it's not too difficult, useful, and you really understand how things run.

I have to admit that my lazy ass cheeks are happily clapping in the realm of high-level languages.
I am doing data science, where most of my days are spent within a DSL of Python: polars/pandas or in the happy declarative land of SQL.
And behold! Once in a while on a hot day, I do a few network calls, yeah real thug life!
Clearly, I am not the target audience when everything need to be rewritten from scratch.

Only a madman would ask me to code a dictionary or an array manipulation framework from scratch!
Unless you really want your product to be a gaping security hell-hole, with nice entire chunks of memory leaks?
No? I thought so!
Anyway if such a set of basic things are not part of the standard library or the package eco-system, is of little use/appeal to me.
This is why I am more interested in Rust/Go with their promise on performance while offering some higher-level interface with little overhead.

But enough digressions, in the vast lands of SQL and data warehouses, each with its own engine, translating your code to assembly make no sense at all.
I am nevertheless genuinely curious to see if the large binary files for pandas/polars could be relatively "simple" as Casey tends to portray it.
And I would love to see the instruction sets and general layout there.

However beyond the dark fearful "assembly" thingy, there is pure gold. Assembly here is just a mean to obtain an understanding on how the computer operate and how you language of choice will choose to run certain operations.

This is where I am in complete agreement with Casey and where we can really witness:

## The Staggering Difference When People Have A General Idea Of How Their Code Run


I see way too many people exhibiting a blatant dead-fish stare whenever you mention the word `vectorization` for operating on a dataframe.
