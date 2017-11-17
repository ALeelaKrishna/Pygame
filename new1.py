import time
import random
import threading


class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, integers, condition):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition
        self.daemon = True
    
    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        while True:
            integer = random.randint(0, 4)
            self.condition.acquire()
            # print 'condition acquired by %s' % self.name
            if len(self.integers) == 3:
                print ("Full...")
            else:
                self.integers.append(integer)
                print '%d appended to list by %s' % (integer, self.name)
            # print 'condition notified by %s' % self.name
            self.condition.notify()
            # print 'condition released by %s' % self.name
            self.condition.release()
            time.sleep(random.randint(0, 1))

class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, integers, condition):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.daemon = True
        self.integers = integers
        self.condition = condition
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            self.condition.acquire()
            # print 'condition acquired by %s' % self.name
            while True:
                if len(self.integers) == 0:
                    print 'Empty ...'
                else:
                    if self.integers:
                        integer = self.integers.pop()
                        print '%d popped from list by %s' % (integer, self.name)
                        break
                # print 'condition wait by %s' % self.name
                self.condition.wait()
            # print 'condition released by %s' % self.name
            self.condition.release()
            time.sleep(random.randint(0, 4));


integers = []
condition = threading.Condition()
t1 = Producer(integers, condition)
t2 = Consumer(integers, condition)
t3 = Consumer(integers, condition)
t1.start()
t2.start()
t3.start()
while True:
    time.sleep(1)

