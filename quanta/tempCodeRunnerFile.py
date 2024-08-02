print("\nAPI Statistics:")
for api, stats in api_stats.items():
  print(f"{api}: Highest = {stats['highest']} ms, Lowest = {stats['lowest']} ms, Average = {stats['average']:.2f} ms")