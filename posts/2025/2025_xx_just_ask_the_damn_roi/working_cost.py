from enum import unique
import polars as pl


WEEKLY_HOURS = 40
WORK_WEEK_NUMBER = 45
YEARLY_WORKING_HOURS = WEEKLY_HOURS * WORK_WEEK_NUMBER

base_salary = (
    pl.DataFrame(
        [
            ("EU - €", "lower", 50_000, 1.45),
            ("EU - €", "higher", 80_000, 1.45),
            ("US - $", "lower", 100_000, 1.3),
            ("US - $", "higher", 200_000, 1.3),
        ],
        schema=["origin", "estimated_bound", "base_salary", "multiplier"],
        orient="row",
    )
    .with_columns(
        yearly_employer_cost=(pl.col.base_salary * pl.col.multiplier).cast(int),
    )
    .with_columns(
        hourly_employer_cost=(pl.col.yearly_employer_cost / YEARLY_WORKING_HOURS).round(
            1
        ),
        weekly_employer_cost=(pl.col.yearly_employer_cost / WORK_WEEK_NUMBER)
        .mul(0.01)
        .round()
        .mul(100)
        .cast(pl.Int64),
    )
    .group_by("origin", "multiplier")
    .agg(
        (
            (pl.col("base_salary", "yearly_employer_cost") // 1000)
            .sort()
            .cast(pl.String)
            + "K"
        ).str.join(" - "),
        pl.col("hourly_employer_cost", "weekly_employer_cost").str.join(" - "),
    )
    .select(
        "origin",
        "base_salary",
        "multiplier",
        "hourly_employer_cost",
        "weekly_employer_cost",
        "yearly_employer_cost",
    )
    .sort("origin")
    .rename(lambda x: x.replace("_", " ").title())
    .to_pandas()
    .to_markdown(index=False)
)

if __name__ == "__main__":
    print(base_salary)
