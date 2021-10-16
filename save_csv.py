import csv


def save_to_csv(fails):
    file = open("fails.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["site", "name", "link", "price_fail", "price_true"])
    for fail in fails:
        writer.writerow(list(fail.values()))
