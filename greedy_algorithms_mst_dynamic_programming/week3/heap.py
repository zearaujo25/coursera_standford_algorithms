class Heap():
    def __init__(self,heap_type='min'):
        self.heap = []
        self.position_map = {}
        self.heap_type = heap_type

    def heap_insert(self,node):
        self.heap.append(node)
        self.position_map[node] = len(self.heap)-1
        self.bubble_up(node)

    def bubble_up(self,node):
        parent = self.heap[(self.position_map[node]+1)//2 -1]
        should_swap =  node.weight < parent.weight if self.heap_type == 'min' else node.weight > parent.weight
        while should_swap and self.position_map[node] != 0:
            self.swap_elements((node,parent))
            parent = self.heap[(self.position_map[node]+1)//2 -1]
            should_swap =  node.weight < parent.weight if self.heap_type == 'min' else node.weight > parent.weight

    def swap_elements(self,elements):
        positions = self.position_map[elements[0]],self.position_map[elements[1]]

        self.heap[positions[0]] = elements[1]
        self.heap[positions[1]] = elements[0]

        self.position_map[elements[0]] = positions[1]
        self.position_map[elements[1]] = positions[0]

    def heap_pop(self):
        self.swap_elements((self.heap[0],self.heap[-1]))
        popped_node = self.heap.pop()
        self.position_map.pop(popped_node)
        if len(self.heap) >1:
            self.bubble_down(self.heap[0])
        return popped_node

    def bubble_down(self,node):
        child_to_swap = self.get_swap_child(node)
        should_swap =  node.weight > child_to_swap.weight if self.heap_type == 'min' else node.weight < child_to_swap.weight
        while should_swap:
            self.swap_elements((node,child_to_swap))
            child_to_swap = self.get_swap_child(node)
            should_swap =  node.weight > child_to_swap.weight if self.heap_type == 'min' else node.weight < child_to_swap.weight

    def get_swap_child(self,node):
        if self.heap_type == 'min':
            left_child = self.heap[(self.position_map[node]+1)*2-1] if (self.position_map[node]+1)*2-1 < len(self.heap) else float("inf")
            right_child = self.heap[(self.position_map[node]+1)*2] if (self.position_map[node]+1)*2 < len(self.heap) else float("inf")
            return left_child if left_child.weight < right_child.weight else right_child
        else:
            left_child = self.heap[(self.position_map[node]+1)*2-1] if (self.position_map[node]+1)*2-1 < len(self.heap) else float("-inf")
            right_child = self.heap[(self.position_map[node]+1)*2] if (self.position_map[node]+1)*2 < len(self.heap) else float("-inf")
            return left_child if left_child.weight > right_child.weight else right_child

    def heap_delete(self,node):
        element_position = self.position_map[node]
        self.swap_elements((node,self.heap[-1]))
        self.heap.pop()
        self.position_map.pop(node)
        if len(self.heap) >1:
            self.bubble_down(self.heap[element_position])