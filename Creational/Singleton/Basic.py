'''
Singleton Pattern: Ensures that a class has only one instance and provides a global point of access to that instance.
'''

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

'''
Potential Drawbacks and Considerations: Unveiling the Other Side
The Singleton pattern might shine, but what about its shadows?

While the Singleton pattern provides clear advantages, it’s imperative to recognize its potential limitations. In fact, the Singleton pattern, despite its solutions, is occasionally labeled an “anti-pattern” due to the following reasons:

1) Single Responsibility Violation: Simultaneously addressing two concerns, the Singleton pattern can blur responsibilities.
2) Global Coupling: The globally accessible Singleton instance can foster tight interdependence between application sections, potentially complicating maintenance and testing.
3) Testing Dilemmas: Testing components reliant on a Singleton can pose difficulties, given the influence of the global state on test outcomes.
4) Multithreading Complexities: In multithreaded environments, special precautions are necessary to avert multiple thread-based Singleton creation.

Real-world Use Cases: Singleton in Action
The Singleton pattern is commonly used in various real-world scenarios:

1) Database Connection Pools: Enhancing database interaction efficiency via a unified connection pool.
2) Logger Services: Centralizing application logging through a single logger instance.
3) Configuration Management: Ensuring a solitary configuration manager instance oversees application settings.
4) Hardware Access: Controlling access to hardware resources, such as a printer or sensor, through a single instance.

'''