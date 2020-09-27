from heap import Heap
class Node():
    def __init__ (self,weight,info=None,lef_child=None,righ_child=None):
        self.info = info
        self.weight = weight
        self.lef_child = lef_child
        self.righ_child = righ_child


class HuffmanCode():
    def __init__(self):
        self.heap = Heap()
        self.root_node = None
    
    def add_symbol(self,weight,symbol_info=None):
        symbol_node = Node(weight,symbol_info)
        self.heap.heap_insert(symbol_node)
    
    def huffman_encode(self):

        while len(self.heap.heap) > 1:
            node1 = self.heap.heap_pop()
            node2 = self.heap.heap_pop()
            merged_node = self.__merge_nodes(node1, node2)
            self.heap.heap_insert(merged_node)
        self.root_node = self.heap.heap_pop()
        return self.root_node

    def __merge_nodes(self, node1, node2):
        left_child = node1 if node1.weight >= node2.weight else node2
        righ_child = node1 if node1.weight < node2.weight else node2
        new_weight = node1.weight + node2.weight
        merged_node = Node(weight=new_weight,lef_child=left_child,righ_child=righ_child)
        return merged_node
    
    def create_encode_map_string(self):
        encoding_map = {}
        return self.__traverse_tree(self.root_node,"",encoding_map)

    def __traverse_tree(self,current_node,prefix,encoding_map):
        if current_node.lef_child is None and current_node.right_child is None:
            encoding_map[(current_node.info,current_node.weight)] = prefix
            return encoding_map
        encoding_map = self.__traverse_tree(current_node.left_child,prefix + "0",encoding_map)
        encoding_map = self.__traverse_tree(current_node.righ_child,prefix + "1",encoding_map)


            


                
