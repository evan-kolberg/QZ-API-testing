import json
import re
import subprocess
import threading
import time
import websocket

def find_working_ws_port():
    try:
        output = subprocess.check_output(['lsof', '-iTCP', '-sTCP:LISTEN', '-n', '-P'], universal_newlines=True)
    except Exception as e:
        print('Error running lsof:', e)
        return []
    ports = set()
    for line in output.splitlines():
        if 'qdomyoszw' in line:
            m = re.search(r'\*:(\d+)', line)
            if m:
                ports.add(m.group(1))
    for port in list(ports):
        test_url = f'ws://localhost:{port}/floating-ws'
        try:
            ws = websocket.create_connection(test_url, timeout=3)
            ws.close()
            return port
        except:
            continue
    return None

def main_ws_connect(ws_url):
    ws_app = websocket.WebSocketApp(ws_url,
                                    on_open=lambda ws: print('Upgrade HTTP connection OK'),
                                    on_close=lambda ws, code, msg: reconnect(ws_url),
                                    on_error=lambda ws, error: print('Socket encountered error:', error),
                                    on_message=lambda ws, msg: print(json.dumps(json.loads(msg), indent=4)))
    ws_thread = threading.Thread(target=ws_app.run_forever)
    ws_thread.daemon = True
    ws_thread.start()

def reconnect(ws_url):
    print('Socket is closed. Reconnect will be attempted in 5 seconds.')
    time.sleep(5)
    main_ws_connect(ws_url)

if __name__ == '__main__':
    working_port = find_working_ws_port()
    if working_port is None:
        print('No working websocket port found. Exiting.')
        exit(1)

    ws_url = f'ws://localhost:{working_port}/floating-ws'
    print('Using WebSocket URL:', ws_url)

    main_ws_connect(ws_url)
    threading.Event().wait()





