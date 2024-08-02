import re
from collections import defaultdict
import statistics
import pandas as pd

# Define a regex pattern to extract API call information including the timestamp
log_pattern = re.compile(r'(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}\.\d{3}):.*?(\w+) /(\S+) .*?(\d+\.\d+) ms')

# Initialize data structures
api_calls = defaultdict(list)
api_counts = defaultdict(int)
line_count = 0

# Read the log file with the correct encoding
with open(r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\Access_logs\pm2outlog_30.txt', 'r', encoding='utf-8') as log_file:
  for line in log_file:
      line_count += 1
      match = log_pattern.search(line)
      if match:
          timestamp, method, endpoint, response_time = match.groups()
          response_time = float(response_time)
          api_calls[endpoint].append((timestamp, response_time))
          api_counts[endpoint] += 1

# Calculate most/least called APIs
most_called_api = max(api_counts, key=api_counts.get)
least_called_api = min(api_counts, key=api_counts.get)

# Calculate most/least time-taking APIs
average_times = {api: statistics.mean([time for _, time in times]) for api, times in api_calls.items()}
most_time_taking_api = max(average_times, key=average_times.get)
least_time_taking_api = min(average_times, key=average_times.get)

# Group APIs and calculate highest, lowest, and average times
api_stats = []
for api, times in api_calls.items():
  response_times = [time for _, time in times]
  api_stats.append({
      'Name of the API': api,
      'Number of Calls': api_counts[api],
      'Highest Time (ms)': max(response_times),
      'Lowest Time (ms)': min(response_times),
      'Average Time (ms)': statistics.mean(response_times)
  })

# Create a DataFrame for tabular representation
df = pd.DataFrame(api_stats)

# Sort the DataFrame by the number of calls in descending order
df_sorted = df.sort_values(by='Number of Calls', ascending=False)

# Save the sorted DataFrame to an Excel file
output_file = r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\Access_logs\api_statistics_sorted.xlsx'
df_sorted.to_excel(output_file, index=False)

# Print the results
print(f"Total lines read in the file: {line_count}")
print(f"Most called API: {most_called_api} ({api_counts[most_called_api]} calls)")
print(f"Least called API: {least_called_api} ({api_counts[least_called_api]} calls)")
print(f"Most time-taking API: {most_time_taking_api} ({average_times[most_time_taking_api]:.2f} ms on average)")
print(f"Least time-taking API: {least_time_taking_api} ({average_times[least_time_taking_api]:.2f} ms on average)")

# Print the sorted DataFrame
print("\nSorted API Statistics:")
print(df_sorted)
print(f"\nSorted API statistics have been saved to {output_file}")

# Create a detailed DataFrame with timestamps for each API call
detailed_stats = []
for api, times in api_calls.items():
  for timestamp, response_time in times:
      detailed_stats.append({
          'Timestamp': timestamp,
          'Name of the API': api,
          'Response Time (ms)': response_time
      })

# Create a DataFrame for detailed statistics
df_detailed = pd.DataFrame(detailed_stats)

# Save the detailed DataFrame to an Excel file
detailed_output_file = r'C:\Users\bashe\OneDrive\Desktop\Data Science\Projects\quantana\Access_logs\detailed_api_statistics.xlsx'
df_detailed.to_excel(detailed_output_file, index=False)

# Print the detailed DataFrame
print("\nDetailed API Statistics:")
print(df_detailed)
print(f"\nDetailed API statistics have been saved to {detailed_output_file}")