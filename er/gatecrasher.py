def audit_attendance(registered_list, checkin_logs):
    for register in registered:
        # print(register)
        if register in logs:
            print("yes")
        else:
            print("no")
# You can test it like this:
registered = ["Aarav Sharma", "Priya Verma", "Rohan Gupta", "Simran Kaur"]
logs = {

    "Aarav Sharma":"10:00 AM",
    "Priya Verma":"10:02 AM",
    "Vikram Singh":"10:15 AM"
}
logk=list(logs.keys())
audit_attendance(registered, logs)