from queue import Queue
from threading import Lock

class MessageBus:
    def __init__(self):
        self.channels = {}
        self.lock = Lock()

    def register(self, agent_name):
        with self.lock:
            if agent_name not in self.channels:
                self.channels[agent_name] = Queue()

    def send(self, recipient, message):
        with self.lock:
            if recipient in self.channels:
                self.channels[recipient].put(message)

    def receive(self, agent_name):
        with self.lock:
            if agent_name in self.channels and not self.channels[agent_name].empty():
                return self.channels[agent_name].get()
        return None
