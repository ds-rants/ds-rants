---
title: The Angry Guide To Pandas Code - Applying Vengeance (Part 2)
author: "DS Rants"
date: "2025-12-05"
categories:
  - data science
  - pandas code
  - non-pessimization
  - performance
image: image.png
---

Beware I have returned and I'm looking for blood!

It is time to revisit the _pandas_ hell hole, and I'll bring you all down there with me.
You have no luck, I took methamphetamine instead of Xanax, so I'm up for intellectual murder in all kinds of degrees.
In case you have the intellectual IQ of a burnt sushi, I will repeat once more: what we did last time was no optimization!
We just did the bare minimum such that our code does not utterly suck, just enough for me to keep a human form and not bite your head off.

Let's recap for those who sniffed glue and ate the memo before reading it.
There are clear signs for _pandas_ code that should be drenched in gasoline and lit on fire:

1. For loops, because they literally transform your computer into a 1950's toaster, just producing waste heat.
2. The infamous `inplace=True`, because it doesn't save memory and introduces horrible mutations like in your horrible inbreed family.

On the opposite side, in the beautiful _pandas_ world, you use **method chaining** to perform successive transformations.
There, you can use a `lambda` to reference your **current DataFrame** in methods such as `.assign()` or `.loc[]`.

Now we're going to see some more anti-patterns that will demonstrate that, apparently, a simple Google search is beyond your reach.
After killing the King, today we're killing the Queen and the whole court—i.e., the self-joins and `.apply()`.

## The Nasty Inbreeding Caused By Self-Joins

### The Diagnostic

You need to recognize this horrendous habit of yours. It is a _pandas_ anti-pattern, demonstrating clearly that you are just vomiting code.
Here is how it will look in the wild:

```python
ugly_as_fuck_df = ...

stupid_calculation = (
    ugly_as_fuck_df
    .groupby(["patiend_id", "year"])
    .agg({"blood_pressure_value": "mean"})
    .rename(columns={"blood_pressure_value": "avg_blood_pressure"})
    .reset_index()
)

ugly_as_fuck_df = ugly_as_fuck_df.merge(
    stupid_calculation,
    on=["patient_id", "year"],
)
```

Do you understand that your criminal and deviant mind has been feeding your poor DataFrame with its own offspring?
Whenever you take an aggregated DF derived from a parent and merge it back with the parent, you are committing a cardinal sin.
In reality, you're just trying to create a new column with the result of an aggregation.
There is a name for this: this is called a **window function** in good ol' SQL, and in _pandas_ it's called a `groupby().transform()`.

### The Chained Solution

The `.transform()` method will produce an output with "the same indexes as the original object filled with the transformed values" meaning with the same DataFrame shape as **before** the `.groupby()`.

This is how you would do it:

```python
my_new_cool_df = (
    ugly_as_fuck_df.assign(
        avg_blood_pressure=lambda df: (
            df.groupby(["patient_id", "year"])
            ["blood_pressure_value"]
            .transform("mean")
        )
    )
)
```

For the slow data scientists with limited cerebrospinal fluid circulation and still drinking the OOP/imperative Kool-Aid, the code above will produce a similar output to the following one (but without the intermediate results saved inside moronic variables):

```python
ugly_as_fuck_df = ...

avg_blood_pressure = (
    ugly_as_fuck_df.groupby(["patient_id", "year"])
    ["blood_pressure_value"]
    .transform("mean")
)

ugly_as_fuck_df["avg_blood_pressure"] = avg_blood_pressure
```

Pathetic... You were close to greatness... My disappointment is immeasurable...

Do you see how concise, clearer, and cooler the first version is?
You are clearly expressing your motherfucking intent, which is:

- creating (assigning) a new column
- derived from "blood_pressure_value" aggregated with the "mean" function
- this calculation is done independently for each combination of "patiend_id" and "year".

Do you want more awesomeness in your awesomeness because I'm feeling generous?
Your function inside the `.transform` will work if it returns a single value (like mean, min, max) **OR** if it returns a Series with the same size as the current group (like cumsum).
In both cases, the `.transform` will be able to do the joining part for you and put the result of the calculation back with matching keys!

You can even supply your own aggregation functions as long as they return either a single value or an output with the same size (number of rows) as the input.
But don't start pulling some stupid-ass stunts like the ones we're going to address next...

## Killing All The Apply

Now that we killed the Queen, the self-joins, which serve no purpose at all except begging for more brioche like a product owner begs for more features, we have to take care of the court: the `.apply()`.

Like princesses and princes of the old days, most of them are lazy, parasitic, and notoriously harmful to the whole country, and thus should be eliminated without any shred of regret.
Yet, in very few instances, some might hide a little bit of common sense, and one should just tolerate them, after stripping them of their privileges, of course!
Fortunately, no need for a tribunal to tell them apart because one can recognize them at first glance.

### You're Too Dumb To Press "Dot" On Your Keyboard

This will be easy and quick; your shameful laziness will appear clear to all in a minute.

Have you ever done something like this?

```python
my_awesome_df["string_column"].apply(lambda x: x.strip().split(" "))
my_awesome_df["datetime_column"].apply(lambda x: x.date())
```

Have you ever heard of vectorized operation?
They are the ones that allow you to process gigabytes of data in a few seconds—yes, I said seconds, yes, with pandas!
And do you know how ludicrous do you look?
In order to use these vectorized operations, rather than rushing for the `.apply`, all you had to do was to write `.str.something()` or `.dt.something_else()` instead.

```python
my_awesome_df["string_column"].str.strip().str.split(" ")
my_awesome_df["datetime_column"].dt.date()
```

Did your foggy brain, saturated with scrum vapors, happen to notice that the `.str` and `.dt` accessors made the stupid-ass names "string_column" and "datetime_column" completely irrelevant?
Do you now understand how stupid you look with your automated use of `.apply()`?
You exhibited a typical default flight response at the idea of looking at the documentation.
You behaved like a screeching libertarian billionaire confronted with the idea that taxes are actually necessary to educate people and that he is going to have to pay.
You were literally one keystroke away from producing something useful and still managed to fail...

I am impressed by such dedication towards mediocrity.
Anyway, go read the damn [documentation about _pandas_ datetimes and derived](https://pandas.pydata.org/docs/user_guide/timeseries.html) before we head to the next abomination.

### Apply(..., index=1) Is For Zeroes

Do you really want me to start digging a grave for your challenged neo-cortex that went on permanent vacation?
This is a for loop in disguise, and you know what happens to people that use for loops around here, don't you?
Great, at least you seem to have developed enough survival instinct to calm my anger...for now!

From now on, you will have only one God, and its glorious name is **Vectorization**!
You will seek its favors at all times when you write _pandas_ code.
This will be your sole purpose in life, your only hope for salvation.
You will follow the holy scriptures derived from the mathematical operators or the built-in `.dt` and `.str` accessors.

You may _**very sparsely**_ consult a scripture from the nearby _NumPy_ church when no solace can be found in the original divine texts.
Beware: many heretics have abused the alternative scriptures and have fostered a blasphemous, unreadable hybrid, for which mercy compels us to shoot on sight.
Especially, you will burn at the stake if I see any instance of nested `np.where()`, because we have seen the light of the glorious [case_when in v2.2.0](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.case_when.html) (replacing the venerable [np.select](https://numpy.org/devdocs/reference/generated/numpy.select.html)).

Once you do everything we mentioned so far, your code will be largely free from vomit projections or gangrenous infections.
As long as you avoid those pitfalls carefully, _pandas_ will become quite fast.
To give you a ballpark idea, you should be able to process several GBs of **real-life data** in a matter of seconds—yes, I said seconds!
If you reach such a state, an encounter with your code will not induce any ferocious fury fit that typically makes me reach for a flamethrower, but may actually leave me in a decent mood.

This leaves us in good dispositions to talk about some edge-cases.

### Quirks Of Apply On Multiple Columns

Now it is time for a little confession; we're approaching the only instance where I might, maybe, perhaps, acknowledge distantly that method chaining is slightly less readable than traditional OOP syntax. Here is a quick example:

```python
import pandas as pd
import seaborn as sns


def z_score(col: pd.Series) -> pd.Series:
    return (col - col.mean()) / col.std()

```

Here is the traditional way:

```python
diamonds = sns.load_dataset("diamonds")
diamonds[["carat", "depth", "table", "price"]] = diamonds[
    ["carat", "depth", "table", "price"]
].apply(z_score)
diamonds.head()
```

Indeed, applying the same transformation on multiple columns using pure method chaining requires a combination of lambdas, dict-comprehension, and unpacking...
Now, this may look a little cabalistic for unaccustomed eyes:

```python
diamonds = sns.load_dataset("diamonds").assign(
    **{
        col: lambda df: z_score(df[col])
        for col in ["carat", "depth", "table", "price"]
    }
)
diamonds.head()
```

Let's decompose this quickly:

- `**` to transform the dictionary into kwargs,
- then the column name and a lambda to reference the **current DataFrame**,
- the function to use inside the body of the lambda,
- the columns to iterate over, which define our dict-comprehension,
- you can even add a prefix/suffix by swapping the dictionary key with an f-string: `f"prefix_{col}"`/`f"{col}_suffix"`.

Again, I will acknowledge that this may not be trivial to write, but at least I am sure you learned a thing or two.

Don't gloat, you overly inefficient entshitificator; this is not a moment of weakness from me.
The atrocities you committed and indulged in disqualify you from making any desirable comment!
The only reason for this is _pandas'_ venerable age and sadly the absence of a unified and clear syntax. But not all hope is lost, as larger animals will demonstrate much later.

> But, Sir Rants, you just used for loops with a _pandas_ DataFrame and you told me not to! That's not fair!

Sigh... Do I really have to explain everything?
Since your mind is equipped with the agility of a dead bird engulfed in an oil spill, I will articulate this more clearly.
What you just witnessed in the former example is indeed a for loop.
This for loop is used to create a **_finite collection of functions_**, but everything is done by the `.assign()` method.
This for loop is not involved in any calculation.
It does not iterate over the whole fucking DataFrame, nor perform 4 levels of nasty, nested group-by operations that even a moronic ape smashing on a keyboard would not dare to do!

### Advanced Apply Operations

Here we are mostly speaking about the pattern `.groupby().apply()`.
Again there is some leeway, because on one hand it allows you to perform simply some operations that could be quite complex when written with a different syntax.
On the other hand, it can become extremely fast a foot-gun loaded with unnecessary complexity, even faster than an executive sabotaging a good product because now it must use AI.

Regardless, use a more straightforward and explicit syntax if possible:

```python
(
    fancy_name_because_i_use_method_chaining
    .groupby(["column_name_1", "column_name_2"])
    .agg(
        avg_price=("price", "mean"),
        avg_price_change=("price", lambda x: x.diff().mean()),
        awesome_feature=("scores", function_defined_elsewhere),
    )
)
```

This very expressive syntax is usually a good seatbelt against our own stupidity while being only slightly more verbose.
But since when is the number of characters you type the bottleneck of your work?

## Final Thoughts

Let's recap one more time how to write _pandas_ that will not trigger the next maintainers of your code to spiral down into depression, hang themselves, and/or gouge their eyes out.

1. No ...

   > No fucking for loops, Sir Rants, I learned the message!

   Good lad!

1. No `inplace=True`. It prevents method chaining and does nothing for memory.
1. Use `lambda df: df...` to reference the current dataframe when filtering or creating new columns.
1. Do not create DataFrame inbreeding with horrible self-joins. You should use the `groupby().transform()` which are similar to SQL window functions.
1. The use of `.apply` is typically done be weak minded people who have no clue of the absolute glory of _**Vectorization**_.
1. The only places where `.apply` can be tolerated are usually when using the same transformation on multiple columns for sake of readability, or after `.groupby` operations but beware of the complexity demon here!
1. Any preprocessing of ≈10GBs on average hardware nowadays should definitely take less than a few 10s of seconds.
   Be extremely skeptic if you reach a minute or above.

Again, we are not doing any kind of optimization around here; we are just writing code that does not suck utterly and that is not a waste of CPU cycles.
Method chaining is a good way to limit your own ability to do stupid shit, and it keeps you within a decent range of the "optimal" processing time you can hope to have in pure _pandas_.

If you use these simple rules of thumb, you will have a code that is not only surprisingly fast even for _pandas_ but also extremely readable and debuggable.
Your coworker will stop despising you when you hand them over some code, your manager will give you the employee of the month trophy, and your significant other won't dump your sorry ass.
(The last two promises are only binding for those who believe in cryptocurrency or the tooth-fairy).
