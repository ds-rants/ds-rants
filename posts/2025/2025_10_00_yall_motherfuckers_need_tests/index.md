---
title: "Y'All Motherfuckers Need Tests"
author: "DS Rants"
date: "2025-10-20"
categories: [data science, software engineering, tests, best practices]
# image: ouroboros.png
draft: true
draft-mode: visible
number-sections: true
---

## Big Brain Moment

> “To me, legacy code is simply code without tests.”
>
> _Michael C. Feathers, Working Effectively with Legacy Code_

> "With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don't know if our code is getting better or worse.”
>
> _Michael C. Feathers, Working Effectively with Legacy Code_

Note: [Big Brain Reference](https://grugbrain.dev/)

## I Am A Simple Data Scientist, Are You Sure I Need Tests?

Which blog are you on? _**Data Science Rants!**_ Of course you need tests!

### Why Should I Test?

Because it would be nice to have a data science project working once in a while that is not a complete dumpster-fire.
Just for context and reference, for developers nowadays the question is not "should I automate my tests?" but how, when, on which infrastructure to mirror prod as close as possible, and independently from other people working on different features.
All senior developers advocate for massive strategies, the "State of DevOps" reports shows testing as a major component of performance.

Sure, a lot of "recent" advances in the Developer and DevOps world have yet to make their entrée in the data world ([Data: The Land That DevOps Forgot](https://www.youtube.com/watch?v=459-H33is6o)).
One could say that we are poorly equipped in terms of tooling.
But one could also say that we missed the fucking memo.
Try convincing a junior DS to do something outside of his notebook without throwing a panic fit, or that the selection of model should be fully automated by a simple CI/CD pipeline.

Yet, the data science people are still curled up in a fetal position because these concepts are usually totally absent of our average workflow.
Why should we adopt something like this that is usually so different from our ways?

### Because Most Data Science Projects Never Reach Production

This means we are wasting time, money, and worse, we are wasting efforts in dead projects when we could do more interesting and useful things for society.
But it's fine because we have been told that companies are the pinnacle of efficiency.

However, this bitter state of the profession is grounded in some harsh realities.
In data science, we are usually in a much worse situation than typical developers, namely because their best practices have generally not reached us.
Some alleged data scientists will happily tell you that they don't version their code without trembling...

In addition, we have by nature a particularly strong coupling to the data (shocker right?).
Even small changes over time in the data distribution tend to have tremendous impact on machine learning systems, even though the structure of the data itself stays the same.
And you know when that happens? _All the damn time for every damn use-case!_

Finally, we usually need to produce large amounts of code and analysis to determine if a given model has even a chance of being remotely useful.
This creates a tension because the code seems constantly in a superposition of state: useless exploratory junk _AND_ awesome preprocessing for big gains model.
Then some very natural cognitive mechanism step in: "I don't need a test because I don't know if my code has any worth".
It is too late at this point, because we will see the tremendous forces that prevent us from writing tests after the code.

Facing those difficulties means we need discipline, and one hell of a kind!
We need to import key practices from other disciplines of IT, that have demonstrated effectiveness in creating reliable software.

One of these practices is testing, so let's recap briefly some generalities.

### The Main Types of Tests

Unless you are living under a rock, you probably heard of unit, integration and acceptance testing. Here's my pseudo-standard definition:

- **Unit tests:** performed to validate the behavior of isolated functions and methods (more rarely classes and modules).
  Fast: < 1 ms.

  My personal grain of salt: Without any dependency to I/O or external systems (disk access, internet, database...), with absolute control of inputs and precise evaluations of outputs.

- **Integration tests:** performed on a collection of functions, usually at the level of classes and modules.
  Slower in general but a few seconds max.

  I/O becomes possible, but my hot-take is: you should only interact with local elements (mostly disk, local database replica, components or binaries from other sub-systems) and nothing that touches the internet.

- **Acceptance tests:** performed on critical paths of the system to ensure key functionalities.
  Much slower and should aim to be around a few minutes or even lower, otherwise they are ran less often, and start to lose their value.

  Here, you can interact with other external systems over the network database and such.

These 3 types of tests constitute the cornerstone of a good test suite, that will allow you to determine with confidence if your system is working and behaving as expected.

## Adopting A Testing Strategy

### No Tests At All

You, sir, are dangerous. You should be thrown in jail, and your ugly, dishonest and deceiving notebook code should be lit on fire.
You are basically handing over a pile of garbage to your coworkers and yell as you exit the building:

> "And good luck with any changes in business requirements, upgrade in package versions, refactoring or generally future evolutions, because you know it works on my machine...oh and by the way, the business wants this model in production next week..."

I despise you with every fiber of my being and will definitively high five you at the first occasion... in the face... with a shovel...

### Writing Tests After Writing The Code

Either you probably have good intentions and don't know how to do it but you heart is in a good place. Or you have been told to write tests and you reluctantly follow the orders as a good soldier.
Regardless there are a few problems with that approach:

1. Assuming you are a not complete moron, you have at least run and tested your code manually, visually, or made sure it compiled.
   Then, the idea of writing a automated test already starts to lose meaning because you just saw it with you own eyes: the code is running.
   This mental block is, to me, and by far, the largest factor that prevents juniors from realizing the value of automated tests.

1. In addition, writing the test afterwards will be extremely painful and difficult, because your code has not been written with testability as a core requirement, then .
   Good luck being able to isolate some deterministic behavior in a 100 lines of spaghetti with mutations everywhere and no clear responsibilities.

1. As a direct consequence, the tests also tend to become coupled with the implementation details, making them brittle, or flaky, and generally more difficult to maintain.
   The typical example is when you want to change one line in your production code; you clearly see the change, but then you also have to change 20 tests...
   This is usually a sign of bad coupling between tests and implementation.

1. Some large chunks of the system will very likely escape any form of testing (a consequence of `reason N°2.`) because of the impossibility to control their inputs and outputs.

### Writing Tests And Code At The Same Time

Now we are finally getting somewhere. Most of the issues mentioned in the previous section start to erode, with the main exception of `reason N°3`. The main risk with writing tests at the same time as the code, is to increase the coupling between the test and the code, beyond what is strictly required, thus impairing maintainability and limiting future changes and evolution.

However, there are cases where this approach can be actually fruitful, especially for certain scopes and contexts (More on that later).

### Writing Tests Before Any Code

At last, for any sleeping data scientist that managed to open an eyelid, this is the bread and butter of any self-respecting developer these days. This is called Test-Driven Development, a.k.a. **TDD**, and this is how to do it properly:

1. **RED:** You write a **failing** test, which, from well-defined inputs, asserts that a given piece of code has certain well-defined outputs. This is akin to writing specifications in the code.
2. **GREEN:** You write the smallest, most simplistic, even idiotic code you can think of to make the test pass. Nothing more!
3. **REFACTOR:** You replace the idiotic part you just wrote with something less stupid or ugly. **But pay attention!** You should not write anything that is not inside the test. The point is to let the tests and specifications drive the code.

And you repeat the cycle!

This (apparently contrived) way of testing has dramatic advantages:

- It completely breaks the idea of: "I don't need a test because I just saw my code run" because the code does not even exist yet.
- It forces you to write code in very small, incremental steps, and all the great old wizards of software engineering are pretty much saying this is the best way to work, period!
- You are usually able to fall back to working code with a bunch of automated tests within a few seconds. This is such a change that Kent Beck, the guy who coined the term TDD, called it Xanax for developers!
- The code becomes easier to test because you are writing with a clear goal to make it testable, otherwise you're just making your life difficult. Duh!
- The incremental nature forces a progressive decoupling between the code and the test, which is a great sign for maintainability and increases the possibility of future changes.
- Because you want the things to be easy to test, you naturally limit the scope of what your functions/classes can do, which increases their internal cohesion. They tend to do fewer things but do them better.

Overall writing tests first has such a strong impact on your design, namely, it prevents you from doing stupid shit, like becoming your worst enemy and face-planting your project 3 meters underground. You will actually keep the possibility to continue making changes to your code (see the **excellent youtube channel** [Modern Software Engineering](https://www.youtube.com/@ModernSoftwareEngineeringYT/videos)).

> - "But Sir Rants, if TDD is that good, why are data scientists not doing it?"
> - "Young lad, thank you for the very interesting question, allow me to introduce you to: ..."

## The Top 7 Obstacles That Prevent You From Testing

Dear reader, I apologize for the sudden surge of click-bait writing style, but this will likely be a long post, anyhow...

Writing tests is difficult, even for seasoned developers. However, writing tests first with TDD is actually easier but also requires a strong shift of mindset.

1.  Most people advocating for the practice of TDD will repeat that it is an acquired skill, one that you need to train regularly.
    It will take you time and practice to master it.
    Do not try to jump directly with code in the old legacy project if you have never written an automated test.
    You are setting yourself up for failure.

    ::: {.callout-tip}

    ## Solution

    Start practicing regularly with simple code katas, do not try to jump directly to writing tests for legacy codebases or data science workflows.
    It will very likely take you at least 6 months to get comfortable with the basics of testing

    If possible use a small side project at work where your hands are free to move.
    :::

1.  The more you wait to incorporate tests in your workflow, the more difficult it will get to do it.
    Imagine saying to your Product Manager, that after 6 months of crunching and regurgitating code, suddenly you want to write tests because one day you woke up and decided you cared about quality (hopefully after reading this rant).

    Now imagine that at the start of your project, you said to that blissfully unaware PM: "There shall be a test for every bit of code produced, and no test means no code, means no feature!"

    ::: {.callout-tip}

    ## Solution

    Start adopting a testing strategy as soon as possible in the project lifetime.
    In the extremely likely case of a legacy project, you must be aware that some bits will be extremely difficult to test.
    This is where practicing in isolation first (step 1.) will save you on more than a couple of occasions.
    :::

1.  The things you will try to test at first will probably be too large, and the scope poorly defined.
    This will make the size of the inputs probably larger than what would be reasonable.

    ::: {.callout-tip}

    ## Solution

    Try to really limit the size, scope, functionalities you try to test at a given time.
    Take a smaller sized approach.
    :::

1.  One very common error is to try to test the main functionality of a future piece of code right from the get-go. Rookie mistake!
    This is like head-butting a piece of concrete to make a wall fall down, it might work but you might not be able to repeat that feat once your skull is cracked open.

    ::: {.callout-tip}

    ## Solution

    Do not jump directly to the core of the functionalities; start with the simple things and let the behavior progressively emerge from the iterative process.
    Let's take an idiotic example, imagine you want to sort elements of a list.
    Rather than giving a list of 10 numbers and making sure they are sorted in the end, start by passing an empty list (Great! We just found an edge-case!), then perhaps a list with one element (shocker, input and output should be the same...).
    :::

1.  You will probably try to test things while reading from the disk or worse the network or the database.
    You should refrain from committing such ungodly horrors.
    This will make your tests brittle and flaky.

    ::: {.callout-tip}

    ## Solution

    Stay away from any kind of I/O, i.e. disk reads or writes, network calls, database calls, cloud interaction.
    They do not belong in your unit-testing strategy, and even in integration testing, use them only if they **REALLY CAN NOT BE AVOIDED**.
    :::

1.  Not knowing your testing framework is a pretty good way to butcher and obscure your test suite.
    Similarly, you can abuse mocking and stubbing your classes and functions, to ensure that nobody, not even you in two weeks, understands whatever the test is doing.
    Continue in that direction, and you will even find tests that test nothing at all!

    ::: {.callout-tip}

    ## Solution

    Take the time to understand how your testing framework is designed, what it allows you to reuse and what you should rewrite.
    Limit the mocking to the strict minimum to avoid dependencies to external services, but beware of their dark side.
    :::

1.  Not properly setting up your local environment, and not learning to use your IDE/text editor is a very good way to set you up for failure.
    Although it may seem secondary, you absolutely need to properly configure and be comfortable with your local environment, to help you write tests and navigate your code.
    Otherwise it will become a mental blocker and a hidden obstacle to your workflow.

    ::: {.callout-tip}

    ## Solution

    Install test extensions or plugins for your language inside your editor.
    You need first-class support to be able to run a single test, or all of them for a given class/file, or your whole test suite at will, using single click or a small terminal call.
    :::

In this bit we are going to focus mostly on unit tests. Reminder the features of good unit-tests are: _fast, deterministic, reproducible, decoupled from implementation details_.

### The Specific Couplings In Data Science

As mentioned previously for the ones sleeping in the back of the classroom, data scientists largely deal with large collections of records.

Writing tests in data science is particularly difficult because most of the objects we deal with are collections of items, usually quite complex.
Those items are usually independent only in the best case scenarios but most likely related to each other in some kind of nasty way.
How many times did you have to do an analysis in which on record at a given time strongly influence what was to be done on surrounding elements, but only until variable B changes to a different value?

You don't believe me? Let's assume for ungodly reasons, that you can only use 50% of your dataset for training your model, are you keeping the latest 50%, the oldest, or randomly discarding data?
Even if we strip out this made-up convoluted scenario, I cannot recall, since I started working in the industry, a single real-life dataset in which time played no role at all in some kind of weird way or disguised influence (say goodbye to your kaggle/tutorial static datasets).

This is a strong yet hidden form of coupling which is difficult to circumvent in automated tests but is a major concern for any data science workflow.
This is a question that can remain largely unaddressed in the pure 'developer' world because as long as the object themselves remain valid and the code processing them remains correct, then the system is working properly.

### Issues With Dataframe-Like Testing And Remediation Strategies

As mentioned previously for the ones sleeping in the back of the classroom, data scientists largely deal with large collections of records.
In order for a data scientist to write meaningful unit-tests, assuming a processing done largely on some kind of dataframe/array (which will encompass 95% of the `pandas` and `numpy` junkies), this setup may require some amount of boilerplate even for some simple data and light transformations.

I will assume you have a shred of decency for your coworkers, meaning your transformations look like this:

```javascript
daily_awesome_calculations = (
    original_record_with_meaningful_name
    .drop_nulls()
    .filter(...)
    .group_by("day", "categorical_variable_B")
    .agg(...)
    .sort()
)
```

If not please go see [here](../../2025/2025_04_13_your_pandas_code_is_bad/index.qmd) and [there](../../2025/2025_04_28_angry_pandas_guide/angry_pandas_tutorial.qmd).

Here with the use of [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) (Domain-specific language) like `pandas` / `polars`/ `numpy`, it can be tricky to determine if you are actually testing **your custom** logic or re-testing the methods of the library that are already (hopefully) battle-tested.

For a dataframe test that is not excruciating to write, one needs to strip away all the surrounding complexity.
This means using the smallest amount of rows and columns.
A good rule of thumb is usually 2-Rows \* x-Columns or 3-Rows \* x-Columns to get you started. If you can manage with only one row, you should!
Expressing this again requires a fairly decent bit of expertise to determine the seams / separations in your coding where to make testing easier.

Regardless, here are some simple pointers:

1. Separate dataframe and pure Python logic as much as you can.
   Generally speaking, mixing pandas and Python, is a sure-fire way to make your code slow and in most cases, false.
   Additionally, Python logic is much easier to perform unit tests on.

1. Unit testing on dataframes is still possible with very small examples.
   Keep things as simple as you can with very small data subsets, here again, shapes of 2-Rows \* x-Columns or 3-Rows \* x-Columns or even smaller are your best friends.
   LLMs can help you with the first draft of the boilerplate.
   Once you have the general structure, it can usually be reused on multiple tests.

1. Make the data inside the example dataframe as plain, idiotic and stupid simple as possible (during test setup or 'given' stage).
   This will likely decrease the coupling with your implementation code.
   It will also increase the maintainability of your test in the long run.

   ```python
   given = pd.DataFrame(
        {
            "station": ["a", "b"],
            "temperature": [1.1, 2.3],
        }
    )
   ```

   is better than:

   ```python
   given = pd.DataFrame(
        {
            "station": ["NZ_EXT_1", "DE_INT_42"],
            "temperature": [1.132554, 2.3738687],
        }
    )
   ```

1. Testing on dataframes requires more skill and time to get used to than non-data science code.
   Again practice testing on pure Python first before jumping straight into the complexity ocean.
   Similarly, practice on things with smaller scope at first.

1. Be wary of the scope.
   With too many steps and too much logic, you might have to make your tests extremely permissive.
   For example, just checking that you have more rows in your dataframe after 30 transformations is unlikely to be highly informative...

## Testing At Larger Scale

There is a sort of opposition between scale and ease of applying TDD principles.
Indeed the cornerstone of a good testing strategy is **to obtain a fast, reliable and deterministic feedback** that allows the IT practitioner to have confidence about the proposed changes are safe to release.
Accounting for all use-cases would make the testing unnecessarily slow, bulky and in the end useless.

### What About Integration Testing?

The role of integration testing is to make sure that the sub-components and modules of your system are working properly and fit together to produce some expected behavior.

In the Data Land, integration tests can be usually done by taking a larger chunk of your datasets (plural, because have you ever seen a project with just one...).
For example in Machine Learning workflows, you can try to pass the smallest possible amount of data through your preprocessing, then assert that you indeed got rid of certain columns, managed to remove nulls in certain others.

You can then continue passing this small sample through your training and at least make sure that the training is able to start. There is a tremendous difference between fully automating this and using a pseudo manual verification (either inside a notebook, or via a CLI that you might forget to type).

Again the point here, is to ensure that preprocessing, training, evaluation and similar components can feed into each other, not to talk about model performance, nor to tune hyperparameters.

### Acceptance Testing In The Data World a.k.a Evaluation?

Traditionally, acceptance tests are designed to verify the bare minimum working state of your system, again by validating the critical or major hot paths within your application.
Similarly, they also tend to appear later through the life of IT projects, once the scope become clearer.

With them you should be able to obtain a definitive answer to the question: "Is my system in a working state so that it can be deployed?"
In that regard, data science systems make no exceptions; this is where you will be able to plug in your database, buckets and APIs.

In ML workflows, the automated evaluation of a model's performance, comparison with a previously deployed model can usually be a good approach to a form of acceptance testing.
However the scope of this question is so large that tons of books have been written on the subject, and sadly, this blog has very little to offer in comparison (especially on the politically correct side of things...).
The final strategy will vary very much depending on the size of your data, the necessary retraining frequency, the selected metrics and type of model considered.

### The Holy Grail Of Data Tests

Data tests, also called defensive testing, stand in a weird position because they can fit at all levels of the testing pyramid.
Similarly to integration tests for data science, the point here is to validate... the data!
These tests ensure that you actually got a primary key (unique **and** non-null for the sleepy ones), that numeric columns fit within a certain range, that you got rid of null...

This is where `dbt`, `dataform`, `SQLMesh` and similar frameworks that allow you to test data at a large scale really shine.
In this paradigm it is still possible to write code using TDD, simply, rather than starting to write SQL code, you will start by specifying in the metadata the types and the tests for a given column.
They are obviously SQL oriented but their contribution to our field is really a game changer.

In Python, few packages have been developed to help you use a TDD workkflow in data science.
One issue is perhaps that they tend to be quite different from the DSL you are working with. (While Kent Beck says that a testing framework should be in the same language as the code for TDD).
Another problem is that none of them has managed to obtain the same reach and influence as the SQL based, with the notable exceptions of `great-expectations` (which can be a little quirky and slow to use) and the great `pydantic` (more oriented for APIs).
The catch being again that they are not necessarily fitted for TDD in Data Science.
Other defensive analysis packages for `pandas` such as `engarde` or `bulwark` are not maintained anymore.
They also suffer from a decorator oriented approach and very sparse type-hinting, that is again not ideal for TDD.
On the `polars` side, there is one obscure package called `pelage`, fairly similar to dbt tests, but the level of adoption seems to be currently on par with the number of working brain cells for the average Elon Musk fanboy...

In the end, if you have the possibility to jam as many tests as you can within your SQL pipelines, please knock yourself out!
Worst case scenario, your analytics tables might end up having an actual working primary key, which would be a nice change once in a while... just saying...
And who knows, you could accidentally end up with a dashboard in which the numbers are not just straight-up lies, nor a rough estimate but actually accurate...

## Conclusion

Sure, there are specific issues with data science that make it more difficult to test.
Sure you might not know if you are going to keep that 500-line analysis you just wrote.
But let's be real for a minute, the fact that your 500-lines have not been tested is probably a good reason why it will go down the drain.
The main reason you are probably not doing it is that you have no idea how to test a function that is not FizzBuzz, let alone in a TDD workflow.
Testing in Data Science is hard but do not kid yourself, it is doable and should be done.

Clearly the "Dev" culture has not yet been imported in the Data Science world, and most of us definitely missed the DevOps train.
Yet people who have jumped on it are out there.
They deploy 5 times a day to production, doing canary-release after training 10 models concurrently on perfect copies of their prod environment, after a simple commit-push.
In the end, this is a shame because we all have to be **software engineers**.
If anything the specific hardships of Data Science should make us yearn for already proven solutions.

I hope you are now absolutely convinced, as I am, of the imperious necessity of importing good testing strategies into Data Science.
Otherwise, let's hope you and I will never find ourselves in the same room, because I will definitely reach for that shovel.
