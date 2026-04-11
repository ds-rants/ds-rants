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



```sql
DECLARE batch_size INT64 DEFAULT 200000000;  -- Adjust the batch size according to your resources
DECLARE offset_value INT64 DEFAULT 0;
DECLARE row_count INT64;

CREATE TABLE `project.dataset.new_partitioned_table`
    PARTITION BY DATE(column_with_insertion_date)
    OPTIONS(partition_expiration_days = 730)
AS SELECT * FROM `project.dataset.original_table` WHERE 1 = 0;

-- Get the total number of rows in the original table
SET row_count = (SELECT COUNT(*) FROM `project.dataset.original_table`);

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



## The Final Nightmare


The last part of the story is quite different. Here I receive only some echoes and. Only an assumor 's, but indirect. Summary for a treaty happen. Call birth picture. We were trying to integrate Dataiku into our current technical stack.
Things were looking pretty good, despite the fact that this tool is obviously utter garbage, and a creator of technical debt on par with the average LLM.

Regardless, there are a few things you should know about its so called intuitive recipes.
For some of them, it can be almost impossible to actually determine what will be the behavior.
Some could be executed in your database, here BigQuery, or run on your cluster GKE, or some by the frail DSS instance supporting the UI.
We're coming from nice work. You tends to organize things and. Missteps. That happens.
That's all through the cracks of the Confederation. Indeed, not until. Recently.
There was something weird with slight issue with partitioning (it starts to be a common theme...).
Whenever you were asking in the UI to partition the underlying table because you're well meaning and wanted to use best-practices,but the actual underlying data in BigQuery were not partitioned themselves, you ran into a little hiccup.
You received the gentle blue warning saying something like:  There was apparently a small mismatching and asking you if you wanted to proceed.
But whenever you clicked on that "confirm" button, the Dataiku software was about to recopy the full table underneath by chunks of 10,000 or 20,000 rows.
In this case it was combined with a bug that trigger the destruction / recreation of the table in the most wild billing loop that would give any founder a heart attack.
