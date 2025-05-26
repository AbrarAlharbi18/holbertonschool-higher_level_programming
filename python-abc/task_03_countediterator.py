class CountedIterator:
    """An iterator that keeps track of how many items have been iterated over"""
    
    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0"""
        self.iterator = iter(iterable)
        self.counter = 0
    
    def __next__(self):
        """Get next item, increment counter, and return item"""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise
    
    def get_count(self):
        """Return the number of items that have been iterated over"""
        return self.counter
    
    def __iter__(self):
        """Return self to allow the iterator to be used in for loops"""
        return self
