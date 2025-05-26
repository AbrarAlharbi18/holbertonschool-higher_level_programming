class VerboseList(list):
    """A list subclass that prints notifications for modifications"""
    
    def append(self, item):
        """Add an item to the end of the list with notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """Extend the list with items from iterable with notification"""
        initial_length = len(self)
        super().extend(iterable)
        added_items = len(self) - initial_length
        print(f"Extended the list with [{added_items}] items.")
    
    def remove(self, item):
        """Remove first occurrence of item with notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Remove and return item at index with notification"""
        item = self[index] if len(self) > 0 else None
        if item is not None:
            print(f"Popped [{item}] from the list.")
        return super().pop(index)
