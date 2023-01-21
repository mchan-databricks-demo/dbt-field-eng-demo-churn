# Databricks notebook source
# MAGIC %md
# MAGIC ## 3.1: Load the model as a SQL Function

# COMMAND ----------

# MAGIC %python
# MAGIC import mlflow
# MAGIC #                                                                              Stage/version    output
# MAGIC #                                                                 Model name         |            |
# MAGIC #                                                                     |              |            |
# MAGIC predict_churn_udf = mlflow.pyfunc.spark_udf(spark, "models:/dbdemos_customer_churn/Production", "int")
# MAGIC spark.udf.register("predict_churn", predict_churn_udf)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3.2: Call our model and predict churn on customers

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG field_eng_dbt_catalog; 
# MAGIC USE dbt_c360;

# COMMAND ----------


