def complaint_registration():
    complaints = {}
    ticket_number = 1000
    
    while True:
        name = input("Enter your name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        complaint = input("Enter your complaint: ")
        complaints[ticket_number] = (name, complaint)
        print(f"Your complaint has been registered. Ticket number: {ticket_number}")
        ticket_number += 1
    
    print("\nAll complaints registered:")
    for ticket, (name, complaint) in complaints.items():
        print(f"Ticket {ticket} - {name}: {complaint}")

complaint_registration()
