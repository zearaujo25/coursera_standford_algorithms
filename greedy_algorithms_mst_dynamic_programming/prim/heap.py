class Heap():
    def __init__(self,heap_type='min'):
        self.heap = []
        self.position_map = {}
        self.heap_type = heap_type

    def heap_insert(self,edge):
        if edge not in self.position_map:
            self.heap.append(edge)
            self.position_map[edge] = len(self.heap)-1
            self.bubble_up(edge)

    def bubble_up(self,edge):
        parent = self.heap[(self.position_map[edge]+1)//2 -1]
        should_swap =  edge[1] < parent[1] if self.heap_type == 'min' else edge[1] > parent[1]
        while should_swap and self.position_map[edge] != 0:
            self.swap_elements((edge,parent))
            parent = self.heap[(self.position_map[edge]+1)//2 -1]
            should_swap =  edge[1] < parent[1] if self.heap_type == 'min' else edge[1] > parent[1]


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
        should_swap =  element[1] > child_to_swap[1] if self.heap_type == 'min' else element[1] < child_to_swap[1]
        while should_swap:
            self.swap_elements((element,child_to_swap))
            child_to_swap = self.get_swap_child(element)
            should_swap =  element[1] > child_to_swap[1] if self.heap_type == 'min' else element[1] < child_to_swap[1]

    def get_swap_child(self,element):
        if self.heap_type == 'min':
            left_child = self.heap[(self.position_map[element]+1)*2-1] if (self.position_map[element]+1)*2-1 < len(self.heap) else (None,float("inf"))
            right_child = self.heap[(self.position_map[element]+1)*2] if (self.position_map[element]+1)*2 < len(self.heap) else (None,float("inf"))
            return left_child if left_child[1] <= right_child[1] else right_child
        else:
            left_child = self.heap[(self.position_map[element]+1)*2-1] if (self.position_map[element]+1)*2-1 < len(self.heap) else (None,float("-inf"))
            right_child = self.heap[(self.position_map[element]+1)*2] if (self.position_map[element]+1)*2 < len(self.heap) else (None,float("-inf"))
            return left_child if left_child[1] >= right_child[1] else right_child

    def heap_delete(self,element):       
        if element != self.heap[-1]:
            element_position = self.position_map[element]
            self.swap_elements((element,self.heap[-1]))
            self.heap.pop()
            self.position_map.pop(element)
            if len(self.heap) >1:
                self.bubble_down(self.heap[element_position])
        else:
            self.heap.pop()
            self.position_map.pop(element)
