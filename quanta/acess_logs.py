import re
from collections import defaultdict
import statistics

# Define a regex pattern to extract API call information
log_pattern = re.compile(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}\.\d{3}:.*?(\w+) /(\S+) .*?(\d+\.\d+) ms')

# Initialize data structures
api_calls = defaultdict(list)
api_counts = defaultdict(int)
line_count = 0

# Read the log file
with open(r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\Access_logs\pm2outlog.txt', 'r') as log_file:
  for line in log_file:
      line_count += 1
      match = log_pattern.search(line)
      if match:
          method, endpoint, response_time = match.groups()
          response_time = float(response_time)
          api_calls[endpoint].append(response_time)
          api_counts[endpoint] += 1

# Calculate most/least called APIs
most_called_api = max(api_counts, key=api_counts.get)
least_called_api = min(api_counts, key=api_counts.get)

# Calculate most/least time-taking APIs
average_times = {api: statistics.mean(times) for api, times in api_calls.items()}
most_time_taking_api = max(average_times, key=average_times.get)
least_time_taking_api = min(average_times, key=average_times.get)

# Group APIs and calculate highest, lowest, and average times
api_stats = {}
for api, times in api_calls.items():
  api_stats[api] = {
      'highest': max(times),
      'lowest': min(times),
      'average': statistics.mean(times)
  }

# Print the results
print(f"Total lines read in the file: {line_count}")
print(f"Most called API: {most_called_api} ({api_counts[most_called_api]} calls)")
print(f"Least called API: {least_called_api} ({api_counts[least_called_api]} calls)")
print(f"Most time-taking API: {most_time_taking_api} ({average_times[most_time_taking_api]:.2f} ms on average)")
print(f"Least time-taking API: {least_time_taking_api} ({average_times[least_time_taking_api]:.2f} ms on average)")

print("\nAPI Statistics:")
for api, stats in api_stats.items():
  print(f"{api}: Highest = {stats['highest']} ms, Lowest = {stats['lowest']} ms, Average = {stats['average']:.2f} ms")