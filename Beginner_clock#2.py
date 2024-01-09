def time_since_midnight(h, m, s):
    milliseconds_per_hour = 60 * 60 * 1000
    milliseconds_per_minute = 60 * 1000
    milliseconds_per_second = 1000

    total_milliseconds = (h * milliseconds_per_hour) + (m * milliseconds_per_minute) + (s * milliseconds_per_second)
    return total_milliseconds

# Example usage
hours = 1
minutes = 30
seconds = 45

result = time_since_midnight(hours, minutes, seconds)
print("Time since midnight in milliseconds:", result)