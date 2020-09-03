import unittest

class TestHash(unittest.TestCase):
    def test_assigment(self):
        ordered_input = []
        sum_in_file = set()
        assigment_path = 'graphs_search_shortest_paths_data_structures/week4/hash/assigment.txt'
        with open(assigment_path) as f: 
            for line in f: 
                number = int(line)
                ordered_input.append(number)

        ordered_input.sort()
        left_end = 0
        righ_end = len(ordered_input)-1
        print(ordered_input[:11])

        while left_end<righ_end:
            print(left_end,righ_end)
            if ordered_input[left_end]+ordered_input[righ_end] < -10000:
                left_end+=1
            elif ordered_input[left_end]+ordered_input[righ_end] > 10000:
                righ_end+=-1
            else:
                for number in ordered_input[left_end:righ_end]:
                    if number + ordered_input[righ_end] <=10000:
                        print("adding")
                        sum_in_file.add(number + ordered_input[righ_end])
                    else:
                        break
                left_end+=1
        
        print(len(sum_in_file))
        print(sum(sum_in_file))
            

if __name__ == "__main__":
    unittest.main()