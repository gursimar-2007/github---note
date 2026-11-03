def audit_attendance(registered_list, checkin_logs):
    registered_in_but_absent=[]
    logged_in_and_present=[]
    logged_in_and_is_in_list=[]
    logged_in_but_not_in_list=[]
    for register in registered_list:
        if register in checkin_logs:
            # print("yes")
            # registerer=list(registered_list)
            # print(f"{register} is checked in and present")
            # logged_in_and_present.append(register)
            # print(f"present:{logged_in_and_present}")
            pass
        else:
            # print(f"{register} is registered but is absent")
            registered_in_but_absent.append({register})
            print(f"no shows:{registered_in_but_absent}")
    for loggers in checkin_logs:
        if loggers in registered_list:
            # print("yes you are in checking logs")
            # newer=list(loggers.keys())
            # print(newer)
            # print(f"{loggers} is in the registered list")
            logged_in_and_is_in_list.append(loggers)
            print(f"present:{logged_in_and_is_in_list}")
        else:
            # print(f"{loggers}are in logs but not in registered list")
            logged_in_but_not_in_list.append(loggers)
            print(f"gatecrashers: {logged_in_but_not_in_list}")
# You can test it like this:
registered = ["Aarav Sharma", "Priya Verma", "Rohan Gupta", "Simran Kaur"]
logs = {

    "Aarav Sharma":"10:00 AM",
    "Priya Verma":"10:02 AM",
    "Vikram Singh":"10:15 AM"
}
logk=list(logs.keys())
audit_attendance(registered, logs)