from heapq import heapify,heappop,heappush
class Node():
    def __init__ (self,weight,info=None,left_child=None,right_child=None):
        self.info = info
        self.weight = weight
        self.left_child = left_child
        self.right_child = right_child


class HuffmanCode():
    def __init__(self):
        self.heap = []
        self.entries_added = 0
        self.root_node = None
    
    def add_symbol(self,weight,symbol_info=None):
        symbol_node = Node(weight,symbol_info)
        self.entries_added +=1
        heappush(self.heap,(weight,self.entries_added,symbol_node))
    
    def huffman_encode(self):

        while len(self.heap) > 1:
            node1 = heappop(self.heap)[2]
            node2 = heappop(self.heap)[2]
            merged_node = self.__merge_nodes(node1, node2)
            self.push_to_heap(merged_node)
        self.root_node = heappop(self.heap)[2]
        return self.root_node

    def push_to_heap(self, merged_node):
        self.entries_added+=1
        heappush(self.heap,(merged_node.weight,self.entries_added,merged_node))

    def __merge_nodes(self, node1, node2):
        left_child = node1 if node1.weight >= node2.weight else node2
        right_child = node1 if node1.weight < node2.weight else node2
        new_weight = node1.weight + node2.weight
        merged_node = Node(weight=new_weight,left_child=left_child,right_child=right_child)
        return merged_node
    
    def create_encode_map_string(self):
        encoding_map = {}
        self.__traverse_tree(self.root_node,"",encoding_map)
        return encoding_map

    def __traverse_tree(self,current_node,prefix,encoding_map):
        if current_node.left_child is None and current_node.right_child is None:
            encoding_map[(current_node.info,current_node.weight)] = prefix
        else:
            self.__traverse_tree(current_node.left_child,prefix + "0",encoding_map)
            self.__traverse_tree(current_node.right_child,prefix + "1",encoding_map)


            


                
