---
title: "Y'All Motherfuckers Need Tests"
author: "DS Rants"
date: "2025-10-20"
categories: [data science, software engineering, tests, best practices]
# image: ouroboros.png
draft: true
---

## Big Brain Moment:

> “To me, legacy code is simply code without tests.”
>
> _Michael C. Feathers, Working Effectively with Legacy Code_

> "With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don't know if our code is getting better or worse.”
>
> _Michael C. Feathers, Working Effectively with Legacy Code_

##

Writing tests in data science is particularly difficult because most of the objects we deal with are collections of items, usually quite complex, and which are only independent in the best case scenarios but most likely related to each other in some kind of nasty way.
How many time did you had to do an analysis in which on record at a given time strongly influence what was to be done on surrounding elements but only until variable B changes to a different value ?

You don't believe me? Let's assume for ungodly reasons, that you can only use 50% of your dataset for training your model, are you keeping the latest 50%, the oldest, or randomly discarding data?
Even if we strip out this made-up convoluted scenario, I cannot recall since I started working in the industry, a single real-life dataset in which time played no role at all in some kind of weird way or disguised influence (say goodbye to your kaggle/tutorial static datasets).

This is a strong yet hidden form of coupling which is difficult to express in automated tests (unit- or integration) but is a major concern for any king of data science workflow.
This is a question that can remain largely unaddressed in the pure 'developer' world because as long as the object themselves remain valid and the code processing them remains correct, then the system is working properly.

Now, let's examine:

## The Different Strategies Of Testing

#### 1. Writing No Tests At All

You sir, are a dangerous. You should be thrown in jail, and your ugly, dishonest and deceiving notebook code should be lit on fire.
You are basically handing over a pile of garbage to your coworkers and yell as you exit the building: "And good luck with any changes in business requirements, upgrade in package versions, refactoring or generally future evolutions..."

I despise you with every fiber of my being and will definitively high five you at the first occasion... in the face... with a shovel!

#### 2. Writing Tests After Writing The Code

Either you probably have good intentions and don't know how to do it but you heart is in a good place. Or you have been told to write tests and you reluctantly follow the orders as a good soldier.
Regardless there are a few problems with that approach:

1. Assuming you are a not complete moron, you have at least manually run and tested your code visually, made sure it compiled.
   Then, the idea of writing a automated test already start to loose meaning because you just saw it with you own eyes: the code is running.
2. Because your code has not be written with testability as a core requirement, then writing the test afterwards will be extremely painful.
   Good luck being able to isolate some deterministic behavior in a 100 lines of spaghetti with mutation everywhere and no clear responsibilities.
3. As a direct consequence, the tests also tend to become coupled with the implementation details, making them brittle, sometimes flaky, and generally more difficult to maintain.
   This is the typical case were you want to change one line in your production code, you clearly see it but then you also have to change 20 tests...
4. Some large chunks of the system will very likely escape any form of testing (consequence of `2.`) because of the impossibility to control their inputs and outputs.

#### 3. Writing Tests At The Same Time You Are Writing The Code

Now we are finally getting somewhere. Most of the issues mentioned in the previous section start to erode with the main exception of `N°3`. The main risk with writing tests at the same time as the code, is to increase the coupling between the test and the code, beyond what is strictly required, thus impairing maintainability and limiting future changes and evolution.

However, there are cases were this approach can be actually fruitful, especially for certain scopes and contexts (More on that later).

#### 4. Writing Tests Before You Write Any Code

At last, for any sleeping data scientist that managed to open an eyelid, this is the bread and butter of any self-respecting developer these days. This is how you do Test Driven Development, a.k.a. **TDD**, properly:

1. **RED:** You write a **failing** test, which from well defined inputs asserts that a given piece of code has certain well defined outputs. This is akin to writing specifications in the code.
2. **GREEN:** You write the smallest, most simplistic, even idiotic code you can think of to make the test pass. Nothing more!
3. **REFACTOR:** You replace the idiotic part you just wrote, with something less stupid or ugly. **But pay attention!** You should not write anything that is not inside the test. The point is to let the tests and specifications drive the code.

And you repeat the cycle!

This (apparently contrived) way of testing has a dramatic advantages:

- It completely breaks the idea of: "I don't need a test because I just saw my code run" because the code does not even exist yet.
- It forces you to write code in very small, incremental steps, and all the great old wizards of software engineering are pretty saying this is the best way to work, period!
- You are usually able to fall back to working code with a bunch of automated tests within a few seconds. This is such a change that Kent Beck, the guy who coined the term TDD, called it Xanax for developers!
- The code becomes easier to test because you are writing with a clear goal to make it testable, otherwise you're just making your life difficult. Duh!
- The incremental nature forces a progressive decoupling between the code and the test which is a great sign for maintainability et increases the possibility of future changes.
- Because you want the things to be easy to test, you naturally limit the scope of what your functions/classes can do, which increase their internal cohesion. They tend to do fewer things but do them better.

Overall writing tests first has such a strong impact on your design, that it prevent you from doing stupid shit, from becoming your worst enemy and face-planting your project 3 meters underground.

> - "But Sir Rants, if TDD is that good, why are data scientists not doing it?"
> - "Young lad, thank you for the very interesting question, allow me to introduce to you: ..."

## The Top Obstacles That Prevent You From Testing

Dear reader, I apologize for the sudden surge of click-bait writing style, but this will likely be a long post, anyhow...

Writing tests is difficult. Writing test first in a TDD fashion is actually easier but also requires a stronger shift of mindset.

1.  Most people advocating for the practice of TDD will repeat that it is an acquired skill, one that you need to train regularly.
    It will take you time and practice to master it.
    Do not try to jump directly with code in the old legacy project if you have never written an automated test.
    You are setting yourself up for failure.

    > Solution: Start practicing regularly with simple code katas, do not try to jump directly to writing tests for legacy codebases or data science workflows.
    > It will very likely take you at least 6 months to get comfortable with the basics of testing.

    > If possible use a small side project at work where your hands are free to move.

1.  The more you wait to incorporate tests in your workflow, more difficult it will get to do it.
    Imagine saying to your Product Manager, that after 6 months of crunching and regurgitating code, suddenly you want to write tests because one day you woke up and decided you cared about quality (hopefully after reading this rant).

    Now imagine that at the start of your project, you said to that blissfully unaware PM: "There shall be a test for every bit of code produced, and no test means no code, means no feature!"

    > Solution: Start adopting a testing strategy as soon as possible in the project lifetime.
    > In the extremely likely case of a legacy project, you must be aware that some bit will be extremely difficult to test.
    > This is where practicing in isolation first (step 1.) will save you on more than a couple occasion.

1.  The things you will try to tests at first will probably be too large, and the scope poorly defined.
    This will make the size of the inputs probably larger than what would be reasonable,
    > Solution: Try to really limit the size, scope, functionalities you try to test at a given time.
    > Take a smaller sized approach.
1.  One very common error is to try to test the main functionality of a future piece of code right from the get-go. Rookie mistake!
    This is like head-butting a piece of concrete to make a wall fall down, it might work but you might not be able to repeat that feat once your skull is cracked open.

    > Solution: Do not jump directly to the core of the functionalities start with the simple things and let the behavior progressively emerge from the iterative process.
    > Let's take an idiotic example, imagine you want to sort elements of a list.
    > Rather than giving a list of 10 numbers and making sure they are sorted in the end, start by passing an empty list (Great! We just found an edge-case!), then perhaps a list with one element (shocker, input and output should be the same...).

1.  You will probably try to tests things while reading from the disk or worse the network or the database.
    You should refrain from committing such ungodly horrors.
    This will make your tests coupled to external dependencies, meaning you don't control them.
    This will make your tests brittle and flaky

    > Solution: Stay away from any kind of I/O, i.e. disk reads or writes, network calls, database calls, cloud interaction. They do not belong to your unit-testing strategy, and even in integration testing use them only if they **REALLY CAN NOT BE AVOIDED**.

1.  Not properly setting up your local environment, and not learning to use your IDE/text editor is a very good way to set you up for failure.
    Although it may seem secondary, you absolutely need to properly configure and be comfortable with your local environment, to help you write tests and navigate your code.
    Otherwise it will become a mental blocker and a hidden obstacle to your workflow.
    > Solution: Install test extensions or plugins for your language inside your editor.
    > You need first class support to be able to run a single test, or all of them for a given class/file, or you whole test suite at will, using single click or a small terminal call.

## Why Is Writing Tests So Difficult In Data Science?

What are features of good unit-tests:

- They need to be decoupled from the implementation details, i.e. they encode specifications
- They need to run fast
- They need to be deterministic, and produce always the same result when run multiple times
- They also need to be easy to write, and tests on dataframes are more difficult to write that the average test.

In order for a data scientist to write meaningful unit-tests, assuming a processing done largely on some kind of dataframe / array (which will encompass 95% of the `pandas` and `numpy` junkies), this setup may require a relatively large amount of boilerplate even for some simple data and light transformations.

As mentioned previously for the one sleeping in the back of the classroom, data scientists largely deal with large collections of records.
In order to write a test that is not excruciating to write, one needs to strip away all surrounding the complexity, meaning using the smallest amount of rows and columns.
A good rule of thumb is usually 2R _ xC or 3R _ xC to get you started.

But them comes another difficulty, assuming you have a shred of decency for your coworkers, meaning your transformations look like this:

```javascript
daily_awesome_ = (
    original_record_with_meaningful_name
    .drop_nulls()
    .filter(...)
    .group_by("day", "categorical_variable_B")
    .agg(...)
    .sort()
)
```

Here with the use of [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) like `pandas` / `polars`/ `numpy`, it can be tricky to determine if you are actually testing **your custom** logic or re-testing the methods of the library that are already (hopefully) battle-tested.

Expressing this again requires a fairly decent of time trying to determine the seams / separations in your coding where:

1. The test is easy to write.
2. There is not to much logic, to avoid that the test becomes too permissive (ex: just checking that I have more rows in my dataframe after 30 transformations is unlikely to be informative...)
3. There is a enough logic in the code so that the test is not redundant with those of the library.

## What About Integration And Acceptance Testing

## The Holy Grail Of Data Tests

You are one year away to production
