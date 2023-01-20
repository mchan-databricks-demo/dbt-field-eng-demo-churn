{{
 config(
 materialized = 'table', 
 file_format = 'delta'
 )
}}

select * 
from field_eng_dbt_demo.dbt_c360.t1_bronze_orders