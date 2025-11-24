---
title: "Y'all Motherfuckers Need Tests, So Stop Making Lazy Excuses"
author: "DS Rants"
date: "2025-11-20"
categories: [data science, software engineering, tests, best practices]
image: image.png
---

![](image.png){fig-align="center" width="80%"}

This is the second part of a larger rant on tests with the first part available [here](../../2025/2025_11_yall_motherfuckers_need_tests/index.md).

In the first part, I mainly addressed the canonical definitions of testing, the typical difficulties that arise, and potential strategies to progressively get better at testing.
By now, with the bold assumption that you possess a shred of common sense (and survival instinct), you should at least feel strongly that testing in data science should have much greater importance, to say the least.

But sadly, there'll always be some junkie data scientists snorting LinkedIn posts and drunk on Jeff Bezos' apocryphal success stories, who will tell you how special their work is, how testing doesn't work for them, and how it would only slow them down.
Despite my strong desire to caress the frontal lobe of such a person with a shovel, vaporize them on the spot, and curse all their family branches for the next 13 generations, I'll momentarily refrain from violence.

Instead, I'll try to address some reasonable objections one could raise regarding the quirks and specificities that make testing in the data world trickier.
But don't mistake this moment of kindness for any form of weakness; at the end, you'll have no excuses left.

## The Specific Problems With Testing In Data Science

As mentioned previously for those sleeping in the back of the classroom, data scientists largely deal with large amounts of... data.
This means the first action is typically to pull something from a database (lucky you), read a decently structured CSV (we all have to eat), a manually filled Excel file (fly, you fools!), or something far worse—and believe me, you don't want to know.
Do you remember what I said about testing—let alone TDD—being difficult with I/O and external coupling?

### The Hidden Forms Of Couplings

In addition, the testing process is particularly difficult because most of the objects we deal with are collections of items, usually quite complex.
Now add a sprinkle of types and object structures which are usually looser than your own mother's morals.
On top of that, these items are usually independent only in the best-case scenarios but most likely related to each other in some nasty way.
How many times have you had to do an analysis in which one record at a given time strongly influenced what was to be done on surrounding elements, but only until variable B changed to a different value?

You don't believe me? Let's assume, for ungodly reasons, that you can only use 50% of your dataset for training your model: are you keeping the latest 50%, the oldest, or randomly discarding data?
Sure, we can set aside this scenario, which is as plausible as Mark Zuckerberg giving a rat's ass about your privacy or the people he fired.
But I cannot recall, since I started working in the industry, a single real-life dataset in which time played no role at all in some weird way or with disguised influence (say goodbye to your Kaggle/tutorial static datasets).

These questions can remain somewhat secondary in the pure 'developer' world.
Indeed, as long as the objects themselves remain valid and the code processing them remains correct, the system works properly.
This is a strong yet hidden form of coupling that is difficult to circumvent in automated tests but is a major concern for any data science workflow.

And it has only just begun...

### Issues With Dataframe-Like Testing And Remediation Strategies

For a data scientist, writing meaningful unit tests may require a decent amount of boilerplate even for simple data and light transformations.
This assumes processing done largely on some kind of dataframe/array (which will encompass 95% of `pandas` and `numpy` junkies).

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

If not, please go see [here](../../2025/2025_04_13_your_pandas_code_is_bad/index.qmd) and [there](../../2025/2025_04_28_angry_pandas_guide/angry_pandas_tutorial.qmd).
In the absence of any improvement on this matter, I will eagerly greet you with a shovel, as mentioned earlier.
You have been warned...

Here, with the use of [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) (Domain-specific Language) like `pandas`/`polars`/`numpy`, it can be tricky to determine if you are actually testing **your custom** logic or retesting the methods of a library that are already (hopefully) battle-tested.

For a dataframe test that is not excruciating to write, one needs to strip away all surrounding complexity.
This requires the ability to use the smallest number of rows and columns.
A good rule of thumb is usually 2-Rows \* x-Columns or 3-Rows \* x-Columns to get you started.
If you can manage with only one row, you should!

Regardless, here are some general pointers:

### Simple Advice For Writing DataFrame Tests

1. Separate DataFrame and pure Python logic as much as you can.
   Generally speaking, mixing pandas and Python is a sure-fire way to make your code slow and, in most cases, false.
   Additionally, Python logic is much easier to perform unit tests on.

1. Unit testing on DataFrames is still possible with very small examples.
   Keep things as simple as you can with very small data subsets, here again, shapes of 2-Rows \* x-Columns or 3-Rows \* x-Columns or even smaller are your best friends.
   Your favorite LLM overlord can help you with the first draft of the boilerplate.
   Once you have the general structure, it can usually be reused on multiple tests.

1. Make the data inside the example dataframe as plain, idiotic and stupid simple as possible.
   You should aim for the average cryptobro level here, especially during test setup or 'given' stage.
   This will likely decrease the coupling with your implementation code.
   It will also increase the maintainability of your test in the long run.

   ```python
   given = pd.DataFrame(
        {
            "station": ["a", "b"],
            "temperature_in_celsius": [1.1, 2.3],
        }
    )
   ```

   is better than:

   ```python
   given = pd.DataFrame(
        {
            "station": ["NZ_EXT_1", "DE_INT_42"],
            "temperature_in_celsius": [1.132554, 2.3738687],
        }
    )
   ```

1. Testing on DataFrames requires more skill and time to get used to than non-data science code.
   Again, practice testing on pure Python first before jumping straight into the ocean of complexity.
   Similarly, practice on things with a smaller scope at first.

1. Be wary of the scope: with too many steps and too much logic, you might have to make your tests extremely permissive.
   For example, just checking that you have more rows in your DataFrame after 30 transformations is unlikely to be highly informative...

Again, combining those ideas requires a fairly decent bit of expertise to determine the seams/separations in your code to make testing easier.

## Testing At Larger Scale

There is a sort of opposition between scale and the ease of applying TDD principles.
Indeed, the cornerstone of a good testing strategy is **to obtain a fast, reliable, and deterministic feedback** that allows the developer to have confidence that the proposed changes are safe to release.
Accounting for all use cases in the integration and acceptance steps would make the testing unnecessarily slow, bulky, and probably as useful as a statement from Sam Altman on AGI.

### What About Integration Testing?

The role of integration testing is to make sure that the sub-components and modules of your system work properly and fit together to produce some expected behavior.

In the Data Land, integration tests can usually be done by taking a larger chunk of your datasets (plural, because have you ever seen a project with just one...).
For example, in Machine Learning workflows, you can try to pass the smallest possible amount of data through your preprocessing, then assert that you indeed got rid of certain columns and managed to remove nulls in certain others.

You can then continue passing this small sample through your training and at least make sure that the training can start.
There is a tremendous difference between fully automating this and using a pseudo-manual verification (either inside a notebook or via a CLI that you might forget to type).

Again, the point here is to ensure that preprocessing, training, evaluation, and similar components can feed into each other.
We are not talking about model performance or hyper-parameter tuning.

### Acceptance Testing In The Data World a.k.a Evaluation?

Traditionally, acceptance tests are designed to verify the bare-minimum working state of your system, again, by validating the critical or major hot paths within your application.
Similarly, they also tend to appear later in the life of IT projects, once the scope becomes clearer.

With them, you should be able to obtain a definitive answer to the question: "Is my system in a working state so that it can be deployed?"
In that regard, data science systems make no exception.
This is where you'll be able to plug in your database, buckets, and APIs.

In ML workflows, the automated evaluation of a model's performance and its comparison with a previously deployed model can usually be a good approach for acceptance testing.
However, the scope of this question is so large that tons of books have been written on the subject, and sadly, this blog has very little to offer in comparison (especially on the politically correct side of things...).
The final strategy will vary greatly depending on the size of your data, the necessary retraining frequency, the selected metrics, and the type of model considered.
The main point remains: automate this as much as you can!

### The Holy Grail Of Data Tests

Data tests, also called defensive testing, are here to validate... the data!
They stand in a weird position because we mainly see them at the level of the whole data pipeline, although they can fit at many levels of the testing pyramid.
These tests ensure that you actually have a primary key (unique **and** non-null for the sleepy ones), that numeric columns fit within a certain range, and that you got rid of nulls...

This is where `dbt`, `dataform`, `SQLMesh`, and similar SQL-based frameworks really shine by allowing you to test data at a large scale.
Using such frameworks, it is still possible to write code using TDD.
Simply put, rather than starting to write SQL code, you will start by specifying in the metadata the types and tests for a given column.
They are obviously SQL-oriented, but their contribution to our field is really a game changer.

In Python, few packages have been developed to help you use a TDD workflow in data science.
One issue is perhaps that they tend to be quite different from the DSL you are working with (while Kent Beck says that a testing framework should be in the same language as the code for TDD).
Another problem is that none of them have managed to obtain the same reach and influence as the SQL-based ones, with the notable exceptions of `great-expectations` (which can be a little quirky and slow to use) and the great `pydantic` (more oriented for APIs).
The catch, again, is that they are not necessarily fitted for TDD in Data Science.

Other defensive analysis packages for `pandas`, such as `engarde` or `bulwark`, receive less maintenance than your great-great-great-grandparent's tomb.
They also have a MAJOR design flaw, because someone thought it would be a good idea to promote a decorator-oriented approach.
Clearly, simple designs are for weak-minded people.
Similarly, type hints, which have been around since 2015, have been carefully omitted to ensure that after one step my IDE has no fucking idea of the object type it is currently dealing with.
That is, again, not ideal for TDD.

On the `polars` side, there is one obscure package called `pelage`, providing fairly similar functionality to dbt tests.
Thanks to a total absence of marketing, the level of adoption is currently on par with the number of working brain cells of the average Elon Musk fanboy...

In the end, if you have the possibility to jam as many tests as you can within your SQL pipelines, please, knock yourself out!
Worst-case scenario, your analytics tables might end up with an actual working primary key, which would be a nice change for once... just saying...
And who knows, you could accidentally end up with a dashboard in which the numbers are not just straight-up lies or a rough estimate, but are actually accurate...

## Conclusion

This glorious landscape—made of lying dashboards, misleading analyses, and an astonishing 80-90% of machine learning projects that die without reaching production—is just a clear sign that our profession still lacks discipline.
We need to incorporate better practices into our work.
It may take many different forms, but I am sure that testing will and should be a part of it.

Certainly, there are specific issues with data science that make it more difficult to test.
Granted, you might not know if you are going to keep that freshly made 500-line analysis.
But let's be real for a minute: the fact that your 500 lines haven't been tested is probably a good reason why it will end up down the drain.
The main reason you are probably not testing is that you have no idea how to do it on anything beyond FizzBuzz, let alone in a TDD workflow.
Testing in Data Science is hard, but do not kid yourself: it is doable and should be done.
If anything, the specific hardships of Data Science should make us yearn for already-proven solutions that increase software reliability and decrease our cognitive burden.
But I guess some people like their legacy projects served early in the morning with entire chunks of burnout in them.

Clearly, the "Dev" culture has not yet been imported into the Data Science world, and most of us definitely missed the DevOps train.
Yet, people who have jumped on it are out there.
They deploy 5 times a day to production, use canary releases after training 10 models concurrently on perfect copies of their prod environment, after a simple commit-push.
None of these steps can be reached without strict automated testing or a strong self-discipline, such as not touching production with greasy data scientist fingers.
We should strive for better quality standards if we ever want to be considered **serious software engineers**.

In the end, mastery is what we need. With this demonstration, I hope you are now as absolutely convinced as I am of the imperious necessity of importing good testing strategies into Data Science.
Otherwise, it's better if you and I never find ourselves in the same room, because I will definitely reach for that shovel.

### Good Reading {.unnumbered}

- Modern Software Engineering - David Farley - ISBN: 9780137314867
- Extreme Programming Explained: Embrace Change - Beck, Kent; Andres, Cynthia - ISBN 10: 0321278658 / ISBN 13: 9780321278654
- Team Topologies - Matthew Skelton; Manuel Pais - ISBN: 9781966280002
- Accelerate: The Science of Lean Software and DevOps - Gene Kim, Jez Humble, Nicole Forsgren - ISBN 10: 1942788339 / ISBN 13: 9781942788331
- Test Driven Development: By Example - Kent Beck - ISBN: 9780321146533
