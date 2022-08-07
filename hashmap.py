class HashMap:
    def __init__(self):
        self.arrMax = 100
        self.arr = [None for i  in range(self.arrMax)]
    
    def get_hash(self, key):
        h = 0
        for char in key :
            h += ord(char)
        return h % self.arrMax

    def __setitem__(self, key, val):
        index = self.get_hash(key)
        self.arr[index] = val

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]

hash = HashMap()
hash["luxoft"] = 1_300_000
print(hash["luxoft"])