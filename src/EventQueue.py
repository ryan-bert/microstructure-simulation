from enum import Enum
from collections import deque
from time import time

class EventType(Enum):
    NEW_ORDER = "New Order"
    CANCEL_ORDER = "Cancel Order"
    UPDATE_ORDER = "Update Order"

class Event:

    # Constructor for the Event class
    def __init__(self, sent_timestamp, event_type, order):
        self.sent_timestamp = sent_timestamp
        self.processed_timestamp = None     # Set by engine
        self.type = event_type
        self.order = order

class EventQueue:

    # Constructor for the EventQueue class
    def __init__(self):
        self.active_events = deque()
        self.processed_events = deque()

    
