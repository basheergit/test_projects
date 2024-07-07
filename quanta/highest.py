import re
from collections import defaultdict

def parse_log(file_path):
    with open(file_path, 'r') as file:
        log_data = file.read()
    
    # Regular expression to match query entries
    query_pattern = re.compile(r'# Time: (.*?)\n# User@Host: (.*?)\n# Query_time: (.*?)\n# Lock_time: (.*?)\n# Rows_sent: (.*?)\n# Rows_examined: (.*?)\n(.*?)SET timestamp=.*?;\n(.*?);', re.DOTALL)
    
    queries = query_pattern.findall(log_data)
    return queries

def group_errors_by_type(queries):
    error_types = defaultdict(list)
    
    for query in queries:
        time, user_host, query_time, lock_time, rows_sent, rows_examined, command, sql_query = query
        
        # Example error types based on query content
        if "SELECT" in sql_query:
            error_types['SELECT'].append(sql_query)
        elif "INSERT" in sql_query:
            error_types['INSERT'].append(sql_query)
        elif "UPDATE" in sql_query:
            error_types['UPDATE'].append(sql_query)
        elif "DELETE" in sql_query:
            error_types['DELETE'].append(sql_query)
        else:
            error_types['OTHER'].append(sql_query)
    
    return error_types

def main():
    log_file_path = 'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\uat_mysql_logs\mysql'  # Path to your log file
    queries = parse_log(log_file_path)
    
    print(f"Total number of queries: {len(queries)}")
    
    error_types = group_errors_by_type(queries)
    
    for error_type, queries in error_types.items():
        print(f"\nError Type: {error_type}")
        print(f"Number of queries: {len(queries)}")
        for query in queries:
            print(query)

if __name__ == "__main__":
    main()