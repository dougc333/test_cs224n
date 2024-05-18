refactor into events and handlers

decompose into a subscribe ane post_event 
subscribe contains a callback fn for each event type. It only keeps the last
one added. there are no lists of subcribers only event type to callback fn. 
def subscribe(event_type:str, callback_fn)
def post_event(event_type:str, data)

#why did he do this vs {}? 
subscribers = dict()



post_event runs the callback fn on data from post_event. Look up the callback function using event type. 

EVENT type-> callback fn. is subscribe
fn(data) is post_event. 

subscribe is add callback fn to event type
post_event or notify is running the callback fn based on event type and provided data. 



Listeners a fn which waits for an event to occur. Add a listener and it waits/ like
the event type callback fn dict. 
