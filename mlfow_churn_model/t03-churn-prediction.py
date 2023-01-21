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
# MAGIC USE CATALOG field_eng_dbt_demo;
# MAGIC USE dbt_c360;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE VIEW t3_gold_churn_prediction_report 
# MAGIC AS 
# MAGIC SELECT predict_churn(struct(user_id, age_group, canal, country, gender, order_count, total_amount, total_item, platform, event_count, session_count, days_since_creation, days_since_last_activity, days_last_event)) as churn_prediction, * FROM STREAM(live.churn_features)
