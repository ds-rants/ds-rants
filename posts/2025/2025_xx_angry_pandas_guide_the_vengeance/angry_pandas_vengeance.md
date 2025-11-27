---
title: The Angry Guide To Pandas Code - Applying Vengeance (Part 2)
author: "DS Rants"
date: "2025-11-31"
categories:
  - data science
  - pandas code
  - non-pessimization
  - performance
# image: image.png
draft: true
draft-mode: visible
---

Beware I have returned and I'm looking for blood...

It is time to revisit the pandas hell hole, and I'll bring you all down there with me.
You have no luck, I took methamphetamine instead Xanax, so I'm up for intellectual murder in all kinds of degrees.
In case you have intellectual IQ of a burnt sushi, I will repeat once more: what we did last time was no optimization!
We just did the bare minimum such that our code does not utterly suck, just enough for me to keep a human form and not bite your head off.

Let's recap for those who sniffed glue and ate the memo before reading it.
They are clear signs for a pandas code that should be drenched in gasoline and light on fire:

1. For loops because they literally transform your computer into a 1950's toaster, just producing waste heat.
2. The infamous `inplace=True` because they don't save memory and introduce horrible mutations like your horrible inbreed family.

On the opposite side, in the beautiful pandas world, you use **method chaining** to perform successive transformations, and there you can use a `lambda` to reference your **current DataFrame** in methods such as `.assign()` or `.loc[]`

Now we're going to see some more anti-patterns that will demonstrate that apparently a simple google search is beyond your reach.
After killing the King, today we're killing the Queen and and the whole court, i.e. self-joins and `.apply()`.

## The Nasty Inbreeding Caused By Self-Joins

### The Diagnostic

You need to recognized this horrendous habit of yours. It is a pandas anti-pattern demonstrating clearly that you are just vomiting code.
Here is how it will look in the wild:

```python
ugly_as_fuck_df == ...

stupid_calculation = (
    ugly_as_fuck_df
    .groupby(["patiend_id", "year"])
    .agg({"blood_pressure_value": "mean"})
    .rename(columns={"blood_pressure_value": "avg_blood_pressure"})
    .reset_index()
)

ugly_as_fuck_df = ugly_as_fuck_df.merge(
    stupid_calculation
    on=["patiend_id", "year"],
)
```

Do you understand that your criminal and deviant mind has been feeding your poor DataFrame with its own offsprings?
Whenever you take a aggregated DF derived from a parent,and merge it back with the parent, you are committing a cardinal sin.
In reality, you're just trying to create a new column with the result of aggregation.
There is a name for this; this is called a `window function` in good ol' SQL and in pandas it's called a `groupby().transform()`

### The Chained Solution

The `.transform()` method will produce a output with "the same indexes as the original object filled with the transformed values", meaning with the same dataframe shape as **before** the `.groupby()`.

This is how you would do it:

```python
my_new_cool_df = (
    ugly_as_fuck_df.assign(
        avg_blood_pressure=lambda df: df.groupby(["patiend_id", "year"])["blood_pressure_value"].transform("mean")
    )
)
```

For the slow data scientists with limited cerebrospinal fluid circulation and still drinking the OOP/imperative Kool-Aid, the code above will produce a similar output to the following one (but without the intermediate results saved inside moronic variables):

```python
ugly_as_fuck_df == ...

avg_blood_pressure = ugly_as_fuck_df.groupby(["patiend_id", "year"])["blood_pressure_value"].transform("mean")

ugly_as_fuck_df["avg_blood_pressure"] = avg_blood_pressure
```

Pathetic... You were close to greatness... My disappointment is immeasurable...

Do you see how concise and clearer, and cooler the first version is?
You are clearly expressing your motherfucking intent which is:

- creating (assigning) a new column
- derived from "blood_pressure_value" aggregated with the "mean" function
- this calculation is done independently for each combination of "patiend_id" and "year".

Do you want more awesomeness in your awesomeness because I'm feeling generous?
Your function inside the `.transform` will work if it returns a single value (like mean, min, max) **OR** if it returns a series with the same size as the current group (like cumsum).
In both cases, the `.transform` will be able to do the joining part for you, and put the result of the calculation back with matching keys!

You can even supply your own aggregation functions as long as they return either a single value or an output with the same size (number of rows) as the input. But don't start pulling some stupid-ass stunts like the ones we're going to address next...

## Killing All The Apply

Now that we killed the Queen, the self-joins, which serve no-purpose at all except begging for more brioche like a product owner begs for more features, we have to to take care of the court: the `.apply()`

Like princesses and princes of the old days, most of them are lazy, parasitic, and notoriously harmful for the whole country, and thus should be eliminated without any shred of regret.
Yet, on very few instances, some might hide a little bit of common sense, and one should just tolerate them, after stripping them of their privileges of course!
Fortunately, no need for a tribunal to tell them apart, one can recognize them at first glance.

### You're Too Dumb To Press "Dot" On Your Keyboard

This will be easy and quick, your shameful laziness will appear clear to all in a minute.

Have you ever done something like this:

```python
my_awesome_df["string_column"].apply(lambda x: x.strip().split(" "))

my_awesome_df["string_column"].apply(lambda x: x.strip().split(" "))
```

Have you ever heard of vectorized operation?
They are the ones that allow to process Gigabytes of data in few seconds, yes I said secondes, yes with pandas!
And do you know how ludicrous do you look?
In order to used these vectorized operations, rather than rushing for the `.apply`, all you had to do was to write `.str.something()` or `.dt.something_else()` instead.

Do you know understand how stupid you looks with your automated use of `.apply()`?
You exhibited a typical default flight response like a screeching libertarian billionaire confronted to the idea that taxes are actually necessary to educat people, and that he is going to have to pay.

Anyway go read the damn [documentation about pandas datetimes and derived](https://pandas.pydata.org/docs/user_guide/timeseries.html).

### Apply On Multiple Columns
