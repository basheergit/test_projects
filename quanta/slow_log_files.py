import re
import os
from collections import defaultdict

# Define a function to parse the log file
def parse_log(file_content):
  # Regular expressions to match the required fields
  query_time_re = re.compile(r'# Query_time: (\d+\.\d+)')
  rows_sent_re = re.compile(r'Rows_sent: (\d+)')
  rows_examined_re = re.compile(r'Rows_examined: (\d+)')
  query_re = re.compile(r'SET timestamp=\d+; (SELECT|UPDATE|INSERT|DELETE)')
  actual_query_re = re.compile(r'SET timestamp=\d+; (.+)')

  # Initialize data structures to store the parsed data
  query_times = []
  rows_sent = []
  rows_examined = []
  query_types = defaultdict(int)
  queries = []

  # Split the file content into lines
  lines = file_content.split('\n')

  # Iterate through the lines and extract the required information
  for i, line in enumerate(lines):
      query_time_match = query_time_re.search(line)
      rows_sent_match = rows_sent_re.search(line)
      rows_examined_match = rows_examined_re.search(line)
      query_match = query_re.search(line)
      actual_query_match = actual_query_re.search(line)

      if query_time_match:
          query_time = float(query_time_match.group(1))
          query_times.append(query_time)
          if actual_query_match:
              queries.append((query_time, actual_query_match.group(1)))
      if rows_sent_match:
          rows_sent.append(int(rows_sent_match.group(1)))
      if rows_examined_match:
          rows_examined.append(int(rows_examined_match.group(1)))
      if query_match:
          query_types[query_match.group(1)] += 1

  return query_times, rows_sent, rows_examined, query_types, queries

# Define a function to print the analysis
def print_analysis(query_times, rows_sent, rows_examined, query_types, queries):
  print("Query Time Analysis:")
  if query_times:
      print(f"Total Queries: {len(query_times)}")
      print(f"Average Query Time: {sum(query_times) / len(query_times):.2f} seconds")
      print(f"Max Query Time: {max(query_times):.2f} seconds")
      print(f"Min Query Time: {min(query_times):.2f} seconds")
  else:
      print("No query times found.")
  print()

  print("Rows Sent Analysis:")
  if rows_sent:
      print(f"Total Rows Sent: {sum(rows_sent)}")
      print(f"Average Rows Sent: {sum(rows_sent) / len(rows_sent):.2f}")
      print(f"Max Rows Sent: {max(rows_sent)}")
      print(f"Min Rows Sent: {min(rows_sent)}")
  else:
      print("No rows sent data found.")
  print()

  print("Rows Examined Analysis:")
  if rows_examined:
      print(f"Total Rows Examined: {sum(rows_examined)}")
      print(f"Average Rows Examined: {sum(rows_examined) / len(rows_examined):.2f}")
      print(f"Max Rows Examined: {max(rows_examined)}")
      print(f"Min Rows Examined: {min(rows_examined)}")
  else:
      print("No rows examined data found.")
  print()

  print("Query Type Analysis:")
  if query_types:
      for query_type, count in query_types.items():
          print(f"{query_type}: {count} queries")
  else:
      print("No query types found.")
  print()

  # Find the top 5 longest queries
  if queries:
      top_5_queries = sorted(queries, key=lambda x: x[0], reverse=True)[:5]
      print("Top 5 Longest Queries:")
      for time, query in top_5_queries:
          print(f"Time: {time:.2f} seconds, Query: {query}")
  else:
      print("No queries found.")
  print()

  # Find the most frequently called query
  if queries:
      query_count = defaultdict(int)
      for _, query in queries:
          query_count[query] += 1
      most_called_query = max(query_count.items(), key=lambda x: x[1])
      print(f"Most Called Query: {most_called_query[1]} times, Query: {most_called_query[0]}")
  else:
      print("No queries found.")

# Main function to read the log files from a directory and perform the analysis
def main():
  # Directory containing the log files
  log_dir = r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\web_mysql_logs\mysql'

  # Initialize aggregated data structures
  all_query_times = []
  all_rows_sent = []
  all_rows_examined = []
  all_query_types = defaultdict(int)
  all_queries = []

  # Process each log file in the directory
  for log_file in os.listdir(log_dir):
      if log_file.startswith('mysql-slow.log'):
          file_path = os.path.join(log_dir, log_file)
          try:
              with open(file_path, 'r') as file:
                  file_content = file.read()
              query_times, rows_sent, rows_examined, query_types, queries = parse_log(file_content)
              
              # Aggregate the data
              all_query_times.extend(query_times)
              all_rows_sent.extend(rows_sent)
              all_rows_examined.extend(rows_examined)
              for query_type, count in query_types.items():
                  all_query_types[query_type] += count
              all_queries.extend(queries)
          except PermissionError:
              print(f"Permission denied: {file_path}")
          except Exception as e:
              print(f"Error processing file {file_path}: {e}")

  # Print the analysis on the aggregated data
  print_analysis(all_query_times, all_rows_sent, all_rows_examined, all_query_types, all_queries)

# Run the main function
if __name__ == "__main__":
  main()