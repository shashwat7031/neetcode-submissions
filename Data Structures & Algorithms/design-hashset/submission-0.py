class MyHashSet:

    def __init__(self):
        self.my_dict = {}

    def add(self, key: int) -> None:
        self.my_dict[key] = 1

    def remove(self, key: int) -> None:
        self.my_dict[key] = 0

    def contains(self, key: int) -> bool:
        for k,v in self.my_dict.items():
            if k == key:
                if v == 0:
                    return False
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)