import csv


def save_to_csv(jobs):
    file = open("test.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "link", "company", "location"])
    for job in jobs:
        writer.writerow(list(job.values()))
