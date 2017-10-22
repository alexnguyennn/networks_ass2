import heapq
import warnings


# assume - unique items; will throw warning if duplicate is added. Duplicates are both updated if found
# NOTE: make sure item_tuple is always in form of (priority, item)
class UpdateablePriorityQueue:
    def __init__(self, init_list):
        self.heap_list = init_list
        heapq.heapify(self.heap_list)

    def __len__(self):
        return len(self.heap_list)

    def __contains__(self, vertex):
        for item_tuple in self.heap_list:
            if item_tuple[1] == vertex:
                return True
        return False

    # input in (priority, item)
    def insert(self, item_tuple):
        if (item_tuple in self.heap_list):
            warnings.warn(
                "tuple already exists; any updates will update both iterations",
                UserWarning)
        heapq.heappush(self.heap_list, item_tuple)

    def pop(self):
        return heapq.heappop(self.heap_list)

    # input in (priority, item)
    def update_priority(self, item_tuple):
        if len(item_tuple) > 2 and isinstance(
                item_tuple[0], int) and isinstance(item_tuple[1], str):
            raise AttributeError('expected tuple in the form (item, value)')
        update_flag = False
        for t in self.heap_list:
            if t[1] == item_tuple[1]:
                self.heap_list.remove(t)
                heapq.heapify(self.heap_list)
                self.insert(item_tuple)
                update_flag = True
        if not update_flag:
            warnings.warn("tuple not found - no update made", UserWarning)

    def peek_largest(self, n):
        return heapq.nlargest(n, self.heap_list)

    def is_empty(self):
        return len(self.heap_list) == 0
