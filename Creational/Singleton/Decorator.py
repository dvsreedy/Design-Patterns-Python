def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        
        return instances[cls]
    
    return get_instance

@singleton
class SingletonClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
def main():
    instance1 = SingletonClass(10)
    instance2 = SingletonClass(20)

    print(instance1.get_value())  # Output: 10
    print(instance2.get_value())  # Output: 10
    print(instance1 is instance2)  # Output: True
    print(instance1.value)  # Output: 10
    print(instance2.value)  # Output: 10
    instance1.value = 30
    print(instance1.get_value())  # Output: 30

if __name__ == "__main__":
    main()
    