class Heap():
    def __init__(self,heap_type='min'):
        self.heap = []
        self.position_map = {}
        self.heap_type = heap_type

    def heap_insert(self,element):
        self.heap.append(element)
        self.position_map[element] = len(self.heap)-1
        self.bubble_up(element)

    def bubble_up(self,element):
        parent = self.heap[(self.position_map[element]+1)//2 -1]
        should_swap =  element < parent if self.heap_type == 'min' else element > parent
        while should_swap and self.position_map[element] != 0:
            self.swap_elements((element,parent))
            parent = self.heap[(self.position_map[element]+1)//2 -1]
            should_swap =  element < parent if self.heap_type == 'min' else element > parent

    def swap_elements(self,elements):
        positions = self.position_map[elements[0]],self.position_map[elements[1]]

        self.heap[positions[0]] = elements[1]
        self.heap[positions[1]] = elements[0]

        self.position_map[elements[0]] = positions[1]
        self.position_map[elements[1]] = positions[0]

    def heap_pop(self):
        self.swap_elements((self.heap[0],self.heap[-1]))
        popped_element = self.heap.pop()
        self.position_map.pop(popped_element)
        if len(self.heap) >1:
            self.bubble_down(self.heap[0])
        return popped_element

    def bubble_down(self,element):
        child_to_swap = self.get_swap_child(element)
        should_swap =  element > child_to_swap if self.heap_type == 'min' else element < child_to_swap
        while should_swap:
            self.swap_elements((element,child_to_swap))
            child_to_swap = self.get_swap_child(element)
            should_swap =  element > child_to_swap if self.heap_type == 'min' else element < child_to_swap

    def get_swap_child(self,element):
        if self.heap_type == 'min':
            left_child = self.heap[(self.position_map[element]+1)*2-1] if (self.position_map[element]+1)*2-1 < len(self.heap) else float("inf")
            right_child = self.heap[(self.position_map[element]+1)*2] if (self.position_map[element]+1)*2 < len(self.heap) else float("inf")
            return min(left_child,right_child)
        else:
            left_child = self.heap[(self.position_map[element]+1)*2-1] if (self.position_map[element]+1)*2-1 < len(self.heap) else float("-inf")
            right_child = self.heap[(self.position_map[element]+1)*2] if (self.position_map[element]+1)*2 < len(self.heap) else float("-inf")
            return max(left_child,right_child)

    def heap_delete(self,element):
        element_position = self.position_map[element]
        self.swap_elements((element,self.heap[-1]))
        self.heap.pop()
        self.position_map.pop(element)
        if len(self.heap) >1:
            self.bubble_down(self.heap[element_position])