# main.py

from graph import Graph
from truck import Truck
from utils import load_graph, load_packages, save_delivery_log
from datetime import datetime, timedelta
import os

# ========== Setup ==========
graph = Graph()
load_graph(graph, "data/cities.json")
packages = load_packages("data/packages.csv")

# Create trucks
truck1 = Truck(1, start_city="Hub", capacity=3)
truck2 = Truck(2, start_city="Hub", capacity=3)

# ========== Assign packages ==========
# For now, simple round-robin
truck1.assign_packages(packages[0:3])
truck2.assign_packages(packages[3:6])

trucks = [truck1, truck2]

# ========== Simulate Delivery ==========
delivery_logs = []
current_time = datetime.strptime("08:00", "%H:%M")  # trucks start at 8:00 AM

for truck in trucks:
    print(f"\n🚚 Truck {truck.id} starting delivery...")

    for pkg in truck.packages:
        path, dist = graph.dijkstra(truck.current_city, pkg.destination)
        delivery_time = current_time + timedelta(minutes=dist)  # 1km = 1 min

        if pkg.deadline:
            deadline_time = datetime.strptime(pkg.deadline, "%H:%M")
            pkg.status = "On time" if delivery_time <= deadline_time else "Late"
        else:
            pkg.status = "Delivered"

        pkg.mark_delivered(delivery_time.strftime("%H:%M"))
        truck.total_distance += dist
        truck.current_city = pkg.destination

        # Record delivery
        delivery_logs.append({
            "truck_id": truck.id,
            "package_id": pkg.id,
            "destination": pkg.destination,
            "delivery_time": pkg.delivery_time,
            "status": pkg.status
        })

        print(f"Delivered {pkg.id} to {pkg.destination} at {pkg.delivery_time} → {pkg.status}")

# ========== Log Result ==========
if not os.path.exists("logs"):
    os.makedirs("logs")

save_delivery_log(delivery_logs, "logs/delivery_log.txt", "logs/delivery_log.csv")

print("\n✅ All deliveries complete.")
for truck in trucks:
    print(f"Truck {truck.id} distance: {truck.total_distance} km")
