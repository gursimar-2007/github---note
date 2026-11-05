def process_inventory():
    pass




inventory = {"Mouse": 10, "Keyboard": 5, "Monitor": 3, "Headset": 8}
threshold = 3
sales_logs = [
    "Mouse - 4",
    "Keyboard - 3",
    "Monitor - 3",
    "Mouse - 3",
    "Webcam - 1"  # Item not in inventory, should be ignored
]

print(process_inventory(inventory, threshold, sales_logs))