from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs
# iniciando projeto


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salary_list = list()

        for job in self.jobs_list:
            salary = job["max_salary"]

            if salary.isdigit():
                salary_list.append(int(salary))

        return max(salary_list)

    def get_min_salary(self) -> int:
        salary_list = list()

        for job in self.jobs_list:
            salary = job["min_salary"]

            if salary.isdigit():
                salary_list.append(int(salary))

        return min(salary_list)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
