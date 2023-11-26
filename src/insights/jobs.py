from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, newline='') as file:
            csvReader = csv.DictReader(file)

            for row in csvReader:
                self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set()

        for row in self.jobs_list:
            job_type = row['job_type']

            if job_type:
                unique_job_types.add(job_type)
        return list(unique_job_types)

    def filter_by_multiple_criteria(self, jobs, filter: dict) -> List[dict]:

        job_list = []

        if not isinstance(filter, dict):
            raise TypeError("Filter must be a dict")

        for job in jobs:
            criteria = all(
                job.get(key) == value for key, value in filter.items()
            )

            if criteria:
                job_list.append(job)

        return job_list
