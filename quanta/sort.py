import re
from datetime import datetime

# Function to parse log entries and extract timestamp, note type, and message
def parse_log_entry(entry):
    # Regular expression to match timestamp, note type, and message
    pattern = r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+Z) (\d+) \[(\w+)\] (.*)$'
    match = re.match(pattern, entry)
    if match:
        timestamp_str = match.group(1)
        note_id = int(match.group(2))
        note_type = match.group(3)
        message = match.group(4)
        try:
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            return timestamp, note_id, note_type, message
        except ValueError:
            return None, None, None, None
    else:
        return None, None, None, None

# Function to read and sort MySQL error log by note type and timestamp
def sort_mysql_error_log(log_file_path):
    with open(log_file_path, 'r') as file:
        log_entries = file.readlines()

    parsed_entries = []
    for entry in log_entries:
        timestamp, note_id, note_type, message = parse_log_entry(entry)
        if timestamp:
            parsed_entries.append((timestamp, note_id, note_type, message))

    # Sort entries first by note type (alphabetically), then by timestamp
    parsed_entries.sort(key=lambda x: (x[2], x[0]))

    # Print or process sorted entries
    sorted_output = []
    for entry in parsed_entries:
        sorted_output.append(f'{entry[0]} [{entry[2]}] {entry[3]}')

    return sorted_output

# Example usage
if __name__ == "__main__":
    log_file_path = '/workspaces/test_projects/error.log.2'
    sorted_output = sort_mysql_error_log(log_file_path)
    
    # Print the sorted output
    for line in sorted_output:
        print(line)
