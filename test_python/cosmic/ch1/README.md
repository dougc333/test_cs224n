test code to allocate orderlines and batches
why choose orderlines? 

Domain modeling uses a higher level abstractdion than individual objects
1) model business problems via interviews and define a domain language. This examples uses batches and allocations
2) the domain language leads to a domain model. 
the tests are use cases. The batch/allocation tests come from an interview process with the stakeholders. 


we consider domain level operations like sales orders as one operation, inventory as one order,
manufacturing as one order. These domain roles define the responsibility of the domain objects
and the services they provide. 

Higher levels allow for decomposition. if you start at too low a level you cant add in generalizing
abstractions for testing flexibility. Remove out the low level implementation. 

