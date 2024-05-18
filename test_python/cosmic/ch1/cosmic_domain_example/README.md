the smallest object defined for this example is orderline, not order or product. 
An order is composed of many order lines. 
An order line is a sku, quantity and price. There is a principle to keep these 3 objects together in a model dataclass
instead of having multiple data structures for products, orders, users. 

The idea is to start at the domain level defined as orders between System, buying team and customer. This is the domain definition. You can choose your domain definition and model from there. This is different approach than starting with the objects first, customers, buyers, orders, products.


Some rules: reads are easy. Simplyfing the problem to where there are only reads isn't difficult and design problems arent being addressed. 

R/W are a minimum. Testing the boundary conditions if out of inventory, incomplete transactions, writes from different
soruces are a minimum. Performance is part of the application. Adding this in early with e2e tests are necessary. 

Teh difficult part is in allocation, verify if you dont have enough in inventory can you sell it. this is the equivalent of the simplest write and simplest boundary condition. 
