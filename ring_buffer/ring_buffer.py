class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < len(self.storage):
      self.storage[self.current] = item
      self.current += 1
      return self.storage
    else: 
      self.current = 0
      return self.append(item)

  def get(self):
    res = []
    for i in range(len(self.storage)):
      if self.storage[i] is not None:
        res.append(self.storage[i])
    return res

# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# print(buffer.get() )  # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# print(buffer.get())   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())   # should return ['d', 'e', 'f']