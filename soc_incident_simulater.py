print("Mini SOC Incident Report Simulator 🛡️\n")

incident_type = input("Enter type of suspicious activity: ")
severity = input("Enter severity (Low/Medium/High): ")
response = input("Enter response taken: ")

print("\n--- Incident Report ---")
print(f"Incident Type: {incident_type}")
print(f"Severity: {severity}")
print(f"Response: {response}")
print("Investigation Status: Completed")
print("-----------------------\n")
print("This simulation helps understand SOC incident reporting workflow.")
