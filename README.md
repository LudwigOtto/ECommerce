# ECommerce
Django with MySQL

**shop**

Showing items in "ecommerce.Inventory" 
- Models: 1) Inventory
- Urls: 1) inventory_list  2)inventory_detail 
- Views: 1) inventory_list  2)inventory_detail
- Admin: 1) InventoryAdmin 


**cart**

Showing all items add in "ecommerce.Item"
- Models: 1) Item 2) Customer(Foreignkey)
- Urls: 1) item_detail 2) item_add 3) item_remove 
- Views: 1) item_detail 2) item_add 3) item_remove 
- Context_processor?



**orders**

Showing history of each item bought buy each customer in "ecommerce.ShoppingCart"
- Models: 
- 




**_SQL commands_** 	

- Insert:
> insert into ecommerce.Inventory(`Item Id`, `Item Name`, `Quantity`, `Price`, `Seller`, `Type`) 
> VALUES (20, 'Amazon Alexa', 3, 89, 'Amazon', '' );
- Update:
> update ecommerce.Inventory set quantity=2 where `Item Id`=20;

