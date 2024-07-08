import os
import re
from collections import defaultdict, Counter

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
    Counts the number of queries in each log file in the specified directory and collects all queries.

    :param log_dir: Directory containing the log files.
    :return: Tuple containing a dictionary with file names as keys and query counts as values,
             a list of all queries, a dictionary with file type counts, and the number of files checked.
    """
    query_counts = {}
    all_queries = []
    file_type_counts = defaultdict(int)
    files_checked = 0
    
    for filename in os.listdir(log_dir):
        if filename.endswith('.log'):  # Assuming log files have a .log extension
            file_path = os.path.join(log_dir, filename)
            queries = extract_queries_from_log(file_path)
            query_counts[filename] = len(queries)
            all_queries.extend(queries)
            file_type_counts['log'] += 1
            files_checked += 1
        elif filename.endswith('.err'):  # Assuming error files have a .err extension
            file_type_counts['error'] += 1
            files_checked += 1
    
    return query_counts, all_queries, file_type_counts, files_checked

def group_logs_by_query_count(query_counts):
    """
    Groups log files by the number of queries.

    :param query_counts: Dictionary with file names as keys and query counts as values.
    :return: Dictionary with query counts as keys and lists of file names as values.
    """
    grouped_logs = defaultdict(list)
    for filename, count in query_counts.items():
        grouped_logs[count].append(filename)
    return grouped_logs

def find_top_n_longest_queries(queries, n=5):
    """
    Finds the top N longest queries.

    :param queries: List of queries.
    :param n: Number of top longest queries to find.
    :return: List of top N longest queries.
    """
    sorted_queries = sorted(queries, key=len, reverse=True)
    return sorted_queries[:n]

def find_most_called_queries(queries, n=5):
    """
    Finds the top N most called queries.

    :param queries: List of queries.
    :param n: Number of top most called queries to find.
    :return: List of tuples containing the top N most called queries and their counts.
    """
    query_counter = Counter(queries)
    most_called = query_counter.most_common(n)
    return most_called

# Example usage
log_directory = r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\web_mysql_logs\mysql'
query_counts, all_queries, file_type_counts, files_checked = count_queries_in_logs(log_directory)
grouped_logs = group_logs_by_query_count(query_counts)
top_5_longest_queries = find_top_n_longest_queries(all_queries, 5)
top_5_most_called_queries = find_most_called_queries(all_queries, 5)

print(f"Number of files checked: {files_checked}")

for count, files in grouped_logs.items():
    print(f"{count} queries: {files}")

print("\nTop 5 longest queries:")
for i, query in enumerate(top_5_longest_queries, 1):
    print(f"{i}. {query}")

print("\nTop 5 most called queries:")
for i, (query, count) in enumerate(top_5_most_called_queries, 1):
    print(f"{i}. {query} (called {count} times)")