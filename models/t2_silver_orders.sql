{{
 config(
 materialized = “table”, 
 file_format = “delta”
 )
}}

select * 
from {{ ref('t1_bronze_orders') }}