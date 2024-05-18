# Prepopulating data

1) using jinja templates to show errors in server error validation
I would replace this with JS

2) showing POST form processing and routes, funny part is the application factory design pattern to encapsulate local state for reliability
teh problem is it looks funny puttiing routes inside the create_app function. This isn't production code. 

3) I would add more error processing. The form doesnt work. the validators are only 1 step and it can be argued you 
do the validation in JS before reaching the server. The problem with reaching the server is you can get an exception in 
the server causing the server process to stop for ALL clients. 
