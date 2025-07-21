# utils.py
import csv
import json
from package import Package

def load_packages(filename):
    packages = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            packages.append(Package(row["id"], row["destination"], row.get("deadline")))
    return packages

def save_graph(graph, filename="data/cities.json"):
    with open(filename, "w") as f:
        json.dump(graph.g, f)

def load_graph(graph, filename="data/cities.json"):
    with open(filename, "r") as f:
        data = json.load(f)
        for city in data:
            for neighbor, dist in data[city]:
                graph.add_edge(city, neighbor, dist)

# utils.py (add at the bottom)
import csv

def save_delivery_log(deliveries, txt_file, csv_file):
    with open(txt_file, "w") as txt, open(csv_file, "w", newline='') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(["truck_id", "package_id", "destination", "delivery_time", "status"])
        for d in deliveries:
            txt.write(f"Truck {d['truck_id']} delivered {d['package_id']} to {d['destination']} at {d['delivery_time']} → {d['status']}\n")
            writer.writerow([d["truck_id"], d["package_id"], d["destination"], d["delivery_time"], d["status"]])

