# Write your MySQL query statement below
Select Product.product_name, Sales.year, Sales.price 
From Sales 
left Join Product
ON Sales.product_id = Product.product_id 