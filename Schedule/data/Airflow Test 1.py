def mb_dag1_test1():
    import csv
    from datetime import datetime

    # Define the message to be added
    message = "Message:"

    # Get the current timestamp
    current_timestamp = datetime.now()

    # Define the CSV file name
    csv_file = 'timestamps.csv'

    # Check if the file exists to write the header only once
    file_exists = False
    try:
        with open(csv_file, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    # Write the message and timestamp to the CSV file
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Message', 'Timestamp'])  # Write header only if the file doesn't exist
        writer.writerow([message, current_timestamp])

    print(f"Message '{message}' with timestamp {current_timestamp} has been appended to {csv_file}")

if __name__ == "__main__":
    mb_dag1_test1()