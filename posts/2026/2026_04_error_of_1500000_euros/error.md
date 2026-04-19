---
title: "Your Cloud Mistake Is Nothing Until You Hit A $1.5M Bill"
author: "DS Rants"
date: "2026-04-01"
categories: [data science, software engineering, tests, best practices]
# image: image.png
draft: true
draft-mode: visible
---

I started writing this on April 1st, and whish it was a joke.

Do you remember the typical horror stories you see on Hacker News where a random bloke spits out:
"This little configuration cost us thousand on our cloud bill and almost bankrupted our precious startup"?
Well, let me tell you, this is nothing, you're still talking baby playground.
Some companies bring this to the next level, and I am pretty sure there are even worse people out there, there are just not dumb enough to write their story.

But this one is worth being told, it's about the dilution of responsibilities, poor understanding of key principles of databases, little mistakes spiralling into giant ones because of a buggy software.
And Like any good story this one has 3 parts.

## The $40K Rehearsal

It's interesting that in many small companies a similar event would have probably generated strong guardrails to prevent it from ever happening again.
However, in large companies this kind of bill might be a drop in a large ocean.
This is probably the reason why nothing was really done, and the stage was set for yet another disaster.

## The $150K Fireball

Did you notice that the spending increased by an order of magnitude from the last one?

### What Actually Happened

This is the one I know best because I started sniffing around less than a day after it happened.
I was fortunate enough to lay my hands on the actual "code" that could generate a bill able to flatten your average startup 3 km under the ground.

Let's say you have a small database, nothing fancy, only 200 TB of data that is stored in a single table that has no partition, no cluster, no index.
Yes your eyebrows correctly jumped through the ceiling to take a vacation on the rooftop, this in itself is already egregious.
But people are not so malevolent, because this mistake originated in the will to copy everything in a properly managed table with partition and clusters.
Such an operation would at the time of the crime represent a $1000 bill (200 TB \* $5 / TB of data processing).
So how did things escalated so comically?
Well turns out, you only need **30 lines** of idiotic decisions to catapult your financial department into a coma.

Here is the actual code that trigger it, and let me tell you, it is a beauty!

```sql {code-line-numbers="true"}
-- Adjust the batch size according to your resources
DECLARE batch_size INT64 DEFAULT 200000000;
DECLARE row_count INT64;
DECLARE offset_value INT64 DEFAULT 0;

CREATE TABLE `project.dataset.new_partitioned_table`
    PARTITION BY DATE(column_with_insertion_date)
    OPTIONS(partition_expiration_days = 730)
AS SELECT * FROM `project.dataset.original_table`
WHERE 1 = 0;

-- Get the total number of rows in the original table
SET row_count = (
    SELECT COUNT(*) FROM `project.dataset.original_table`
);

-- Loop to insert data in batches
my_loop: WHILE offset_value < row_count DO

    EXECUTE IMMEDIATE FORMAT("""
        INSERT INTO `project.dataset.new_partitioned_table`
        SELECT * FROM `project.dataset.old_table`
        LIMIT %d OFFSET %d
        """, batch_size, offset_value);

    -- Increase offset for the next batch
    SET offset_value = offset_value + batch_size;
    -- Break the loop after the first insertion
    -- LEAVE my_loop;
END WHILE;
```

Isn't it magnificent? Just from looking at the comment style you know it was slop-vibe-coded.
Rather than simply copying the table with new options, they decided they needed to be smart about it.
Let's dissect this monstrosity for learning purpose:

1. _L2-4:_ This starts by a bunch of imperative logic, declaring variable and things like that...

1. _L6-10:_ This part is actually OK, if you want to copy the schema of a table, while changing its options. This is a way that is told you all over the internet.

1. _L13-15:_ Again here, using imperative logic to get the size of the table, because fuck a simple `select` statement to copy the table, right? Now, the heart of the beast, the horror and the curse, the magnificent abomination:

1. The problems continue with the `while` (_L18_), unless you know what you're **really** doing, don't fucking use this kind of stupid imperative logic in your SQL.

1. Then we have the most egregious of all: the `execute immediate` which as the name kindly suggests take up a string and try to evaluate said string immediately.
   This is akin to `eval` in Python and likewise you loose any kind of support with this.
   There is no syntax highlighting, no early detection of error, and most of all in BigQuery no evaluation of the costs before the execution.
   Indeed in the web UI, this whole package of garbage is beautifully evaluated as costing $0, because there is no way to dynamically estimate costs for a poorly meta-programmed query.
   The genius moron that spawned this abomination must have been quite happy about himself when he saw the small green dot in the UI...

1. The `limit` trap (_L23_): this is how we know for sure that this guy has no idea what he is doing.
   BigQuery is a column oriented database, that means the `limit` does absolutely jack shit for data selection.
   It only applies at the very end for display and combined with the `select *` statement right above, it means your are scanning and being billed for the **whole** table for each iteration of this retarded loop!
   Yes this means $1000 per iteration! How many are you asking?
   Motherfucker, we were lucky that this job was actually cancelled "rapidly" because the whole shit-show would have resulted in about 700-800 iterations for a total cost of $700-800k!

1. The rest is basically a continuation of the same stupid imperative logic to update the selection window and exit the loop upon completion.
   This is also sprinkled with the stains indicating the crime committed by the LLM.

To this day, I am still amazed that something so simple can have such a blast radius.
It is almost poetic in a sense.

### Hard Truths And Moderation

In a normal world, what should have happened is this:

```sql
CREATE TABLE `project.dataset.new_partitioned_table`
    PARTITION BY DATE(column_with_insertion_date)
    OPTIONS(partition_expiration_days = 730)
AS SELECT * FROM `project.dataset.original_table`
```

That's it! And this would have cost only $1000 in total, and I would have nothing to scream about during my late evenings plagued with anxiety-induced insomnias.

But we don't live in a normal world, do we?
The reason they performed such unreasonable ass-wiggling instead of shitting straight, was because the straight solution did not seem to work in the first place.
It appears that once in a while organizations put up safety measure and apparently one of them was the inability to run queries whose **_upfront cost_** is above a certain limit.
Probably not the best measure, but I guess some is better than none, unless it contribute to a false sentiment of safety...
Trust me this story is full of bittersweet irony.

Now, this clueless cowboy contractor when facing an infuriating rebuttal decided to go solo rather than asking people around.
One Chat-GPT eructation later, he receives a solution that happily limbo under the restriction bar, and completely unaware of his own shortcomings, his crude ignorance, and globally the fact that he should not be allowed near a database system he doesn't comprehend, he then send his marvelous job to execution.
He at least gets a shred of correct intuition when after two hours the job continues to run, and mercifully decide to cancel the upcoming nightmare.

This whole thing could have been stopped dead in its tracks if only we had set quotas across the organization to limit the BigQuery spending per project.
Hold on! Now, is the time for a short trip to corporate vaudeville.
As it happens, this project was part of our data platform and our datalake team **used** to have quotas in place to catch footguns like this.
But then what happened?
In a beautiful move, it was decided that the responsibility of setting quotas was to be handed to the finops team.
Thus the datalake team removed the ones they had, while the finops never had the time to implement theirs.
Ain't that fucking diabolical?

Unfortunately, we are never really far from annihilation.
It just takes a few bad guardrails, a clueless moron determined to overcome them in hurry, and the absence of larger safety net.
But surely after such an episode, one can hope that we learned from our mistakes, right?

Oh my sweet sweet summer child...

## The Final $1.5M Armageddon

The last part of the story is quite different.
Here, I receive the information from the people who dealt with the aftermath because we were in the same team.
For the general picture, we were integrating Dataiku into our current technical stack.
Things were looking pretty good, despite the fact that this tool is obviously utter garbage, and a creator of technical debt on par with the average LLM.
But hey, who am I to judge?

Regardless, there are a few things you should know about Dataiku and its so called "intuitive" recipes.
For some of them, it can be almost impossible to actually determine what will be the behavior.
Some could be executed in your database, here BigQuery, or run on your GKE cluster, or some by the frail DSS instance supporting the Web UI, which have the nasty little habit to take down the whole instance when there are too many.

Life is so full of happy little accidents.
Among those accidents something really hilarious happens when you fall through the cracks.
Indeed, until recently there was some kind of weird little issue with partitioning (it starts to be a common theme...).

Whenever you were trying to do good and use best-practices like a reasonable human being, as you were asking in the UI to partition your data because but the actual underlying data in BigQuery was not itself partitioned, you ran into a little hiccup.
You received the gentle blue warning saying something like: There was apparently a small mismatching and asking you if you wanted to proceed.
But whenever you clicked on that "confirm" button, the Dataiku software was about to recopy the full table underneath by chunks of 10,000 or 20,000 rows.
In this case it was combined with a bug that trigger the destruction / recreation of the table in the most wild billing loop that would give any founder a heart attack.

## Conclusion

Some of us make small mistakes, bring home a cloud bill of a few thousands of dollars and then talk about it on Hacker News.

But some of us are the reason why we now have **A Worldwide Policy That Set Quotas on BigQuery By Default**! You're welcome!
