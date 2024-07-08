import re
from collections import Counter

# Use raw string to handle backslashes in the file path
log_file_path = r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\uat_mysql_logs\mysql\error.log.5'

# Regular expression to match error lines
error_pattern = re.compile(r'ERROR\s+(\d+):')

error_counts = Counter()

try:
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = error_pattern.search(line)
            if match:
                error_code = match.group(1)
                error_counts[error_code] += 1

    # Print sorted error counts
    for error_code, count in error_counts.most_common():
        print(f'Error Code: {error_code}, Count: {count}')
except PermissionError:
    print(f"Permission denied: '{log_file_path}'")
except FileNotFoundError:
    print(f"File not found: '{log_file_path}'")
except Exception as e:
    print(f"An error occurred: {e}")