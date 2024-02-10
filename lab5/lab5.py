#student name: Ethan Watchorn
#student number: 16538530

import threading
import random #is used to cause some randomness 
import time   #is used to cause some delay in item production/consumption

class circularBuffer: 
    """ 
        This class implement a barebone circular buffer.
        Use as is.
    """
    def __init__ (self, size: int):
        """ 
            The size of the buffer is set by the initializer 
            and remains fixed.
        """
        self._buffer = [0] * size   #initilize a list of length size
                                    #all zeroed (initial value doesn't matter)
        self._in_index = 0   #the in reference point
        self._out_index = 0  #the out reference point

    def insert(self, item: int):
        """ 
            Inserts the item in the buffer.
            The safeguard to make sure the item can be inserted
            is done externally.
        """
        self._buffer[self._in_index] = item
        self._in_index = (self._in_index + 1) % SIZE

    def remove(self) -> int:
        """ 
            Removes an item from the buffer and returns it.
            The safeguard to make sure an item can be removed
            is done externally.
        """
        item = self._buffer[self._out_index]
        self._out_index = (self._out_index + 1) % SIZE
        return item

def producer() -> None:
    """
        Implement the producer function to be used by the producer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeProduced() -> int: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        return random.randint(1, 99)  #an item is produced

    for _ in range(SIZE * 2): #we just produce twice the buffer size for testing
        item = waitForItemToBeProduced()  #wait for an item to be produced
        print(f"DEBUG: {item} produced")
        #complete the function below here to correctly store the item in the circular buffer

        # Buffer initially starts empty, so producer can acquire "empty" semaphore right away
        # This will decrease value every time an item is produced. Once it reaches 0, that means the buffer is full
        # produced items will need to wait until more items are consumed before being added to the buffer.
        empty.acquire()

        # Critical section of the code invoves adding to the circular buffer.
        # Using "with" blocks consumer from removing items until producer finishes adding values to the buffer.
        with mutex:
            buffer.insert(item)

        # This increments "full" semaphore by 1, indicating that there is one additional value in the buffer.
        # Signals to consumer that it can move forward with move forward with consumption.
        full.release()

def consumer() -> None:
    """
        Implement the consumer function to be used by the consumer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeConsumed(item) -> None: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        #to simulate consumption, item is thrown away here by just ignoring it
        
    for _ in range(SIZE * 2): #we just consume twice the buffer size for testing
        #write the code below to correctly remove an item from the circular buffer

        # Acquires "full" semaphore (represents amount of items in the buffer)
        # If "full" is 0 (which is it's starting value), it will wait for producer to add an item, then release "full".
        # Once there is an item in the buffer, the consumer will acquire "full", and carry on with item consumption.
        full.acquire()

        # Critical section of the code invoves removing from the circular buffer.
        # Using "with" blocks producer from adding items until consumer finishes removing values from the buffer.
        with mutex:
            item = buffer.remove()
        # This increments "empty" semaphore by 1, indicating that there is an additional empty space in the buffer.
        # Signals to producer that it can move forward with move forward with production.
        empty.release()

        #end of your implementation for this function
        #use the following code as is
        waitForItemToBeConsumed(item)  #wait for the item to be consumed
        print(f"DEBUG: {item} consumed")

if __name__ == "__main__":
    SIZE = 5  #buffer size
    buffer = circularBuffer(SIZE)  #initialize the buffer

    full = threading.Semaphore(0)         #full semaphore: number of full buffers
                                          #initial value set to 0
    empty = threading.Semaphore(SIZE)     #empty semaphore: number of empty buffers
                                          #initial value set to SIZE
    mutex = threading.Lock()  #lock for protecting data on insertion or removal

    #complete the producer-consumer thread creation below


    # Initializes the producer/consumer threads, and starts them.
    thread_targets = [producer, consumer]
    threads: threading.Thread = []
    for targ in thread_targets:
        threads.append(threading.Thread(target=targ))
        threads[-1].start()

    # Don't technically need .join() since there's nothing else happening after
    # the threads end, but I feel like it's good practice to include.
    for i in range(2):
        threads[i].join()
