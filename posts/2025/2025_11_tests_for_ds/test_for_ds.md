---
title: "Y'All Motherfuckers Need Tests And Stop Making Lazy Excuses"
author: "DS Rants"
date: "2025-10-20"
categories: [data science, software engineering, tests, best practices]
image: image.png
# draft: true
# draft-mode: visible
# number-sections: true
# number-depth: 3
---

![](image.png){fig-align="center" width="80%"}

This is the second part of a larger rant on tests with the first part available [here](../../2025/2025_11_yall_motherfuckers_need_tests/index.md).

In the first parts I mainly addressed the canonical definitions of testing, the typical difficulties that arise, and potential strategies to progressively get better at testing.
By now, with the bold assumption that you possess a shred of common sense (and survival instinct), you should at least have a strong feeling that testing in data science should have a much greater importance, to say the least.

But sadly, there will always be some junky data scientist snorting LinkedIn posts and drunk on Jeff Bezos' apocryphal success stories, to tell you how special his work is, and how testing does not work for him.
Despite my strong desire to pulverize said person on the spot and curse all their family branches for the next 13 generations, I will momentarily refrain from violence.

Instead I will try to address some reasonable objections one could raise regarding quirks and specificities that make testing in the data world trickier.
But don't mistake this moment of kindness for any form of weakness, at the end you will have no excuses left.


## The Specific Problems With Testing In Data Science

### The Hidden Forms Of Couplings

As mentioned previously for the ones sleeping in the back of the classroom, data scientists largely deal with large collections of records.

Writing tests in data science is particularly difficult because most of the objects we deal with are collections of items, usually quite complex.
Those items are usually independent only in the best case scenarios but most likely related to each other in some kind of nasty way.
How many times did you have to do an analysis in which on record at a given time strongly influence what was to be done on surrounding elements, but only until variable B changes to a different value?

You don't believe me? Let's assume for ungodly reasons, that you can only use 50% of your dataset for training your model, are you keeping the latest 50%, the oldest, or randomly discarding data?
Even if we strip out this made-up convoluted scenario, I cannot recall, since I started working in the industry, a single real-life dataset in which time played no role at all in some kind of weird way or disguised influence (say goodbye to your kaggle/tutorial static datasets).

This question can remain largely secondary in the pure 'developer' world.
Indeed, as long as the objects themselves remain valid and the code processing them remains correct, then the system is working properly.
This is a strong yet hidden form of coupling which is difficult to circumvent in automated tests but is a major concern for any data science workflow.
It is not the only one though.

### Issues With Dataframe-Like Testing And Remediation Strategies

As mentioned previously for the ones sleeping in the back of the classroom, data scientists largely deal with large collections of records.
For a data scientist, writing meaningful unit-tests may require decent amount of boilerplate even for some simple data and light transformations.
This assumes a processing done largely on some kind of dataframe/array (which will encompass 95% of the `pandas` and `numpy` junkies).

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
This requires the ability to use the smallest amount of rows and columns.
A good rule of thumb is usually 2-Rows \* x-Columns or 3-Rows \* x-Columns to get you started.
If you can manage with only one row, you should!
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
Indeed the cornerstone of a good testing strategy is **to obtain a fast, reliable and deterministic feedback** that allows the developer to have confidence that the proposed changes are safe to release.
Accounting for all use-cases in the integration and acceptance steps would make the testing unnecessarily slow, bulky and in the end useless.

### What About Integration Testing?

The role of integration testing is to make sure that the sub-components and modules of your system are working properly and fit together to produce some expected behavior.

In the Data Land, integration tests can be usually done by taking a larger chunk of your datasets (plural, because have you ever seen a project with just one...).
For example in Machine Learning workflows, you can try to pass the smallest possible amount of data through your preprocessing, then assert that you indeed got rid of certain columns, managed to remove nulls in certain others.

You can then continue passing this small sample through your training and at least make sure that the training is able to start. There is a tremendous difference between fully automating this and using a pseudo manual verification (either inside a notebook, or via a CLI that you might forget to type).

Again the point here, is to ensure that preprocessing, training, evaluation and similar components can feed into each other, not to talk about model performance, nor to tune hyper-parameters.

### Acceptance Testing In The Data World a.k.a Evaluation?

Traditionally, acceptance tests are designed to verify the bare minimum working state of your system, again by validating the critical or major hot paths within your application.
Similarly, they also tend to appear later through the life of IT projects, once the scope become clearer.

With them you should be able to obtain a definitive answer to the question: "Is my system in a working state so that it can be deployed?"
In that regard, data science systems make no exceptions; this is where you will be able to plug in your database, buckets and APIs.

In ML workflows, the automated evaluation of a model's performance, comparison with a previously deployed model can usually be a good approach for acceptance testing.
However the scope of this question is so large that tons of books have been written on the subject, and sadly, this blog has very little to offer in comparison (especially on the politically correct side of things...).
The final strategy will vary very much depending on the size of your data, the necessary retraining frequency, the selected metrics and type of model considered.
The main point remains: automate this as much as you can!

### The Holy Grail Of Data Tests

Data tests, also called defensive testing, are here to validate... the data!
They stand in a weird position because we mainly see them at the level of the whole data pipeline, although they can fit at many levels of the testing pyramid.
These tests ensure that you actually got a primary key (unique **and** non-null for the sleepy ones), that numeric columns fit within a certain range, that you got rid of null...

This is where `dbt`, `dataform`, `SQLMesh` and similar SQL-based frameworks really shine by allowing you to test data at a large scale.
Using such frameworks, it is still possible to write code using TDD.
Simply, rather than starting to write SQL code, you will start by specifying in the metadata the types and the tests for a given column.
They are obviously SQL oriented but their contribution to our field is really a game changer.

In Python, few packages have been developed to help you use a TDD workflow in data science.
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

This glorious landscape made of lying dashboards, misleading analyses, and an astonishing 80% of machine learning projects that die without reaching production, are just a clear sign that our profession still lacks discipline.
We will need to incorporate better practices in our work, which may take many different forms but I am sure that testing will be a part of it.

Sure, there are specific issues with data science that make it more difficult to test. Granted, you might not know if you are going to keep that freshly-made 500-line analysis.
But let's be real for a minute, the fact that your 500-lines have not been tested is probably a good reason why it will end up down the drain.
The main reason you are probably not testing is that you have no idea how to do it on anything beyond FizzBuzz, let alone in a TDD workflow.
Testing in Data Science is hard but do not kid yourself, it is doable and should be done.
If anything the specific hardships of Data Science should make us yearn for already proven solutions that increase software reliability and decrease our cognitive burden.
But I guess some people like their legacy projects served early in the morning with entire chucks of burn-out in them.

Clearly the "Dev" culture has not yet been imported in the Data Science world, and most of us definitely missed the DevOps train.
Yet people who have jumped on it are out there.
They deploy 5 times a day to production, use canary-release after training 10 models concurrently on perfect copies of their prod environment, after a simple commit-push.
None of these steps can be reached without strict automated testing, nor a strong self-discipline such as not touching the production with greasy data scientist fingers.
We should strive for better quality standards if we ever want to be considered as **serious software engineers**.

In the end, mastery is what we need. With this demonstration, I hope you are now absolutely convinced, as I am, of the imperious necessity of importing good testing strategies into Data Science.
Otherwise, it's better if you and I never find ourselves in the same room, because I will definitely reach for that shovel.
