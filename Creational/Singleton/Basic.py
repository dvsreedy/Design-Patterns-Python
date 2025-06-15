import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()  # Add a lock object for thread safety

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # First check without locking
            with cls._lock:  # Acquire lock
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super(Singleton, cls).__new__(cls)
        
        return cls._instance
    


def main():
    s1 = Singleton()
    s2 = Singleton()

    if s1 is s2:
        print("s1 and s2 are the same instance.")
    else:
        print("s1 and s2 are different instances.")
    
if __name__ == "__main__":
    main()
# This code demonstrates a simple Singleton pattern in Python.