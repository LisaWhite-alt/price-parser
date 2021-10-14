import csv


def save_to_csv(jobs):
    file = open("itog.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["site", "name", "link", "price_fail", "price_true"])
    for job in jobs:
        writer.writerow(list(job.values()))
