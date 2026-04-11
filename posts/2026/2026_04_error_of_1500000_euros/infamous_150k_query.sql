DECLARE batch_size INT64 DEFAULT 200000000;  -- Adjust the batch size according to your resources
DECLARE offset_value INT64 DEFAULT 0;
DECLARE row_count INT64;


CREATE TABLE `project.dataset.new_partitioned_table`
    PARTITION BY DATE(column_with_insertion_date)
    OPTIONS(partition_expiration_days = 730)
AS
SELECT * FROM `project.dataset.original_table` WHERE 1 = 0;

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
