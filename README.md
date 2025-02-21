[I developed a workaround](https://github.com/evan-kolberg/QZ-Python-WebSocket/blob/main/main_macOS.py) if someone would want to connect to the localhost websocket - Works on macOS, possibly Linux, and not Windows.  Thanks to @cagnulein for helping me via email. 

<img width="791" alt="Screenshot 2025-02-20 at 8 03 18 PM" src="https://github.com/user-attachments/assets/e02549df-f43d-4df8-a626-bbca70089267" />

How I did this:

1. Launched QZ
2. Went to ```General UI Options``` in Settings
3. Scrolled down and clicked on ```OPEN FLOATING ON A BROWSER```  - whatever the heck that means
4. Inspected the page and went to Sources
5. Found the ```main_ws_manager.js``` and ```global.js``` files
6. Noticed that the localhost port changed each time the QZ app restarted
7. Since on macOS, ran ```lsof -iTCP -sTCP:LISTEN``` in Terminal.app
8. Saw that there were 4 options for ports and 1 of them was the socket port.
9. Translated the JavaScript code into Python
10. Implemented a function to find the websocket port from the parent process named ```qdomyoszw```
11. Was able to successfully read data from the open websocket

How to run the code (if on macOS, maybe Linux):

1. Launch QZ
2. Git pull the repo (or add it as a submodule) and pip install the websocket library
3. Run ```main_macOS.py```

Your output should look like this:
<img width="607" alt="Screenshot 2025-02-20 at 8 19 27 PM" src="https://github.com/user-attachments/assets/62cffd65-43df-4aaf-b4b2-9fef4fbb4190" />


This doesn't directly give a static port for the browser app, but it offers a solution to those who want to connect to the localhost websocket. 

I still don't know what the ```Server Port: 36866``` option does under ```Experimental Features``` does. Is this for emitting Bluetooth signals with Mqtt or OSC? I don't know.

--
Evan
