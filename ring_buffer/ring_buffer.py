class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # make a while loop
    if self.current == self.capacity:
        self.current = 0
    self.storage[self.current] = item
    self.current += 1    

  def get(self):
    filtered_list = []
    for item in self.storage:
        if item != None:
            filtered_list.append(item)
    return filtered_list

rb = RingBuffer(5)

#print(rb.storage, "< ------- INITIAL STORAGE")
#print(rb.append(3))
#print(rb.append(4))
#print(rb.append(5))
#print(rb.get())
#print(rb.storage, "< ------- STORAGE")
#print(rb.append(6))
#print(rb.append(8))
#print(rb.append(7))
#print(rb.storage, "< ------- STORAGE")

