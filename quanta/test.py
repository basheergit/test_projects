import re
from collections import defaultdict

# Define a function to parse the log file
def parse_log(file_content):
  # Regular expressions to match the required fields
  query_time_re = re.compile(r'# Query_time: (\d+\.\d+)')
  rows_sent_re = re.compile(r'Rows_sent: (\d+)')
  rows_examined_re = re.compile(r'Rows_examined: (\d+)')
  query_re = re.compile(r'SET timestamp=\d+; (SELECT|UPDATE|INSERT|DELETE)')

  # Initialize data structures to store the parsed data
  query_times = []
  rows_sent = []
  rows_examined = []
  query_types = defaultdict(int)

  # Split the file content into lines
  lines = file_content.split('\n')

  # Iterate through the lines and extract the required information
  for line in lines:
      query_time_match = query_time_re.search(line)
      rows_sent_match = rows_sent_re.search(line)
      rows_examined_match = rows_examined_re.search(line)
      query_match = query_re.search(line)

      if query_time_match:
          query_times.append(float(query_time_match.group(1)))
      if rows_sent_match:
          rows_sent.append(int(rows_sent_match.group(1)))
      if rows_examined_match:
          rows_examined.append(int(rows_examined_match.group(1)))
      if query_match:
          query_types[query_match.group(1)] += 1

  return query_times, rows_sent, rows_examined, query_types

# Define a function to print the analysis
def print_analysis(query_times, rows_sent, rows_examined, query_types):
  print("Query Time Analysis:")
  print(f"Total Queries: {len(query_times)}")
  print(f"Average Query Time: {sum(query_times) / len(query_times):.2f} seconds")
  print(f"Max Query Time: {max(query_times):.2f} seconds")
  print(f"Min Query Time: {min(query_times):.2f} seconds")
  print()

  print("Rows Sent Analysis:")
  print(f"Total Rows Sent: {sum(rows_sent)}")
  print(f"Average Rows Sent: {sum(rows_sent) / len(rows_sent):.2f}")
  print(f"Max Rows Sent: {max(rows_sent)}")
  print(f"Min Rows Sent: {min(rows_sent)}")
  print()

  print("Rows Examined Analysis:")
  print(f"Total Rows Examined: {sum(rows_examined)}")
  print(f"Average Rows Examined: {sum(rows_examined) / len(rows_examined):.2f}")
  print(f"Max Rows Examined: {max(rows_examined)}")
  print(f"Min Rows Examined: {min(rows_examined)}")
  print()

  print("Query Type Analysis:")
  for query_type, count in query_types.items():
      print(f"{query_type}: {count} queries")

# Main function to read the log file and perform the analysis
def main():
  # Read the log file content
  file_path = r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\uat_mysql_logs\mysql\error.log.5'
  try:
      with open(file_path, 'r') as file:
          file_content = file.read()
  except PermissionError as e:
      print(f"PermissionError: {e}")
      return
  except FileNotFoundError as e:
      print(f"FileNotFoundError: {e}")
      return
  except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return

  # Parse the log file
  query_times, rows_sent, rows_examined, query_types = parse_log(file_content)

  # Print the analysis
  print_analysis(query_times, rows_sent, rows_examined, query_types)

# Run the main function
if __name__ == "__main__":
  main()