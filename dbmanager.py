import threading

connect_dict = {}
def getConn():
    current = threading.current_thread()
    if not connect_dict.has_key(current):
        connect_dict.