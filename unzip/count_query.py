import os
import re

def extract_queries_from_log(file_path):
    """
    Extracts SQL queries from a MySQL log file.

    :param file_path: Path to the log file.
    :return: List of queries.
    """
    queries = []
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming each query is on a new line and ends with a semicolon
            match = re.search(r'^(.*?);$$', line.strip())
            if match:
                queries.append(match.group(1))
    return queries

def count_queries_in_logs(log_dir):
    """
    Counts the number of queries in each log file in the specified directory.

    :param log_dir: Directory containing the log files.
    :return: Dictionary with file names as keys and query counts as values.
    """
    query_counts = {}
    for filename in os.listdir(log_dir):
        if filename.endswith('.log'):  # Assuming log files have a .log extension
            file_path = os.path.join(log_dir, filename)
            queries = extract_queries_from_log(file_path)
            query_counts[filename] = len(queries)
    return query_counts

# Example usage
log_directory = r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\uat_mysql_logs\mysql'
query_counts = count_queries_in_logs(log_directory)
print(query_counts)