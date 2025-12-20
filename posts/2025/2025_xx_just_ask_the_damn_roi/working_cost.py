import polars as pl


WEEKLY_HOURS = 40
WORK_WEEK_NUMBER = 45
YEARLY_WORKING_HOURS = WEEKLY_HOURS * WORK_WEEK_NUMBER

base_salary = pl.DataFrame(
    [
        ("eu", "lower", 70_000),
        ("eu", "higher", 100_000),
        ("us", "lower", 100_000),
        ("us", "higher", 150_000),
    ],
    schema=["origin", "estimated_bound", "yearly_salary"],
    orient="row",
).with_columns(
    hourly_salary=(pl.col.yearly_salary / YEARLY_WORKING_HOURS).round(2),
    weekly_salary=(pl.col.yearly_salary / WORK_WEEK_NUMBER).round(2),
)

if __name__ == "__main__":
    print(base_salary)
