import unittest
from schedulling_app import read_with_scores,optimize_schedule_by_difference,optimize_schedule_by_ratio

assigment_path = 'greedy_algorithms_mst_dynamic_programming/schedulling_app/assigment.txt'


class TestSchedullingApp(unittest.TestCase):
    
    
    
    def test_assingment_by_difference(self):
        jobs = read_with_scores(assigment_path)
        optimize_schedule_by_difference(jobs)
        completion_time = 0
        completion_times = []
        for job in jobs:
            completion_time+=job['lenght']
            completion_times.append(job['weight']*completion_time)
        self.assertEqual(69119377652,sum(completion_times))

    def test_assingment_by_ratio(self):
        jobs = read_with_scores(assigment_path)
        optimize_schedule_by_ratio(jobs)
        completion_time = 0
        completion_times = []
        for job in jobs:
            completion_time+=job['lenght']
            completion_times.append(job['weight']*completion_time)
        self.assertEqual(67311454237,sum(completion_times))

    
    def test_read_assignment(self):
        jobs = read_with_scores(assigment_path)
        self.assertEqual(10000,len(jobs))
        for job in jobs:
            self.assertEquals(4,len(job))

if __name__ == "__main__":
    unittest.main()