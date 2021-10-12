from hh_parser import get_jobs as get_hh_jobs
from ov_parser import get_jobs as get_ov_jobs
from save_csv import save_to_csv


hh_jobs = get_hh_jobs()
ov_jobs = get_ov_jobs()
jobs = hh_jobs + ov_jobs
save_to_csv(jobs)
