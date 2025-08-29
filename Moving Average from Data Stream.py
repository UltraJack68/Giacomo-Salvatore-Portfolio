"""Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream."""

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.window_lenght = size
        self.sum = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val
        if len(self.queue) > self.window_lenght:
            self.sum -= self.queue.popleft()
            return float(self.sum / self.window_lenght)
        else:
            return float(self.sum / len(self.queue))
                
            
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)