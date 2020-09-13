# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Problem 2 - Solution
# MAGIC 
# MAGIC Read CSV, anonymise are first_name, last_name and address.
# MAGIC 
# MAGIC Anonymize using the lookup table.
# MAGIC 
# MAGIC Using a random number generator between 0 and 1 set true if it is greater than 0.45 create a column 'swap'.
# MAGIC If swap is true swap over first_name and last_name and mask leaving first letter and right pad to 6 characters with *.

# COMMAND ----------

# File location and type
file_location = "/FileStore/tables/contacts_small.csv"
file_type = "csv"

# CSV options
infer_schema = "true"
first_row_is_header = "true"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)

# COMMAND ----------

from pyspark.sql import functions as F
df = df.withColumn('swap', F.rand(2586) > 0.45)

df = df.withColumn('_first_name', F.when(
    F.col('swap'),
    F.rpad(
        F.substring(
            F.col('last_name'),1,1),
        6, 
        '*')).otherwise(F.rpad(
                              F.substring(
                              F.col('first_name'),1,1),
                              6, 
                              '*')
                        ))
df = df.withColumn('_last_name', F.when(
    F.col('swap'),
    F.rpad(
        F.substring(
            F.col('first_name'),1,1),
        6, 
        '*')).otherwise(F.rpad(
                              F.substring(
                              F.col('last_name'),1,1),
                              6, 
                              '*')
                        ))
df = df.withColumn('_address', F.sha2(F.col('address'), 256))

# COMMAND ----------

display(df)

# COMMAND ----------

# Create a view or table

df.select(df._first_name, df._last_name, df._address, df.date_of_birth) \
  .coalesce(1) \
  .write \
  .format('csv') \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .save('/FileStore/tables/contacts_small_anon.csv')

# COMMAND ----------

df \
  .coalesce(1) \
  .write \
  .format('csv') \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .save('/FileStore/tables/contacts_small_lookup.csv')
