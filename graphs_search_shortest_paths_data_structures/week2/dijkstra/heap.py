class Heap():
    def __init__(self,heap_type='min'):
        self.heap = []
        self.position_map = {}
        self.heap_type = heap_type

    def heap_insert(self,node_weight):
        self.heap.append(node_weight)
        self.position_map[node_weight[0]] = len(self.heap)-1
        self.bubble_up(node_weight)

    def bubble_up(self,node_weight):
        parent = self.heap[(self.position_map[node_weight[0]]+1)//2 -1]
        should_swap =  node_weight[1] < parent[1] if self.heap_type == 'min' else node_weight[1] > parent[1]
        while should_swap and self.position_map[node_weight[0]] != 0:
            self.swap_elements((node_weight[0],parent[0]))
            parent = self.heap[(self.position_map[node_weight[0]]+1)//2 -1]
            should_swap =  node_weight[1] < parent[1] if self.heap_type == 'min' else node_weight[1] > parent[1]

    def swap_elements(self,elements):
        positions = self.position_map[elements[0]],self.position_map[elements[1]]

        self.heap[positions[0]] = elements[1]
        self.heap[positions[1]] = elements[0]

        self.position_map[elements[0]] = positions[1]
        self.position_map[elements[1]] = positions[0]

    def heap_pop(self):
        self.swap_elements((self.heap[0][0],self.heap[-1][0]))
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
            left_child = self.heap[(self.position_map[element[0]]+1)*2-1] if (self.position_map[element[0]]+1)*2-1 < len(self.heap) else (None,float("inf"))
            right_child = self.heap[(self.position_map[element[0]]+1)*2] if (self.position_map[element[0]]+1)*2 < len(self.heap) else (None,float("inf"))
            return left_child if left_child[1] <= right_child[1] else right_child
        else:
            left_child = self.heap[(self.position_map[element[0]]+1)*2-1] if (self.position_map[element[0]]+1)*2-1 < len(self.heap) else (None,float("-inf"))
            right_child = self.heap[(self.position_map[element[0]]+1)*2] if (self.position_map[element[0]]+1)*2 < len(self.heap) else (None,float("-inf"))
            return left_child if left_child[1] >= right_child[1] else right_child

    def heap_delete(self,element):
        element_position = self.position_map[element[0]]
        self.swap_elements((element,self.heap[-1]))
        self.heap.pop()
        self.position_map.pop(element)
        if len(self.heap) >1:
            self.bubble_down(self.heap[element_position])

    def get_node_element(self,node):
        return self.heap[self.position_map[node]]