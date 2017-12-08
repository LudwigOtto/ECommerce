# ECommerce
Django with MySQL

**shop**

Showing items in "ecommerce.Inventory" 
- Models: 1) Inventory
- Views: 1) inventory_list  2)inventory_detail
- Admin: 1) InventoryAdmin 


**cart**


Showing all items add in "ecommerce.Item"





**orders**

Showing history of each item bought buy each customer in "ecommerce.ShoppingCart"






_SQL commands_ 	

- Insert:
> insert into ecommerce.Inventory(`Item Id`, `Item Name`, `Quantity`, `Price`, `Seller`, `Type`) 
> VALUES (20, 'Amazon Alexa', 3, 89, 'Amazon', '' );
- Update:
> update ecommerce.Inventory set quantity=2 where `Item Id`=20;

