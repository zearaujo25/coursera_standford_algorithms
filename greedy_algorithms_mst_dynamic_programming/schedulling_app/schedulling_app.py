def optimize_schedule_by_difference(job_list):
    job_list.sort(key= lambda job: (job['diff'],job['weight']),reverse=True)

def optimize_schedule_by_ratio(job_list):
    job_list.sort(key= lambda job: job['ratio'],reverse=True)

def read_with_scores(path):
    schedule = []
    with open(path) as f: 
        for line in f:
            job = {}
            weight_len = line.split()
            if len(weight_len) == 1:
                continue
            job['weight'] = int(weight_len[0])
            job['lenght'] = int(weight_len[1])
            job['ratio'] = job['weight'] /job['lenght']
            job['diff'] = job['weight']-job['lenght']
            schedule.append(job)
    return schedule

