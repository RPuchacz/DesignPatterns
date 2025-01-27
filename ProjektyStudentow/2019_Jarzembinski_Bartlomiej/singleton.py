from threading import Lock

class Singleton:
    _instances = {}
    _threading_lock = Lock()
  
    def __new__(cls):
        if type(object.__new__(cls)).__name__ not in cls._instances:
            with cls._threading_lock:
                if type(object.__new__(cls)).__name__ not in cls._instances:
                    cls._instances[type(object.__new__(cls)).__name__] = object.__new__(cls)
        return cls._instances[type(object.__new__(cls)).__name__]
