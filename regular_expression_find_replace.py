import re
# Lets try and reverse the order of the day and month in a date
# string. Notice how the replacement string also contains metacharacters
# (the back references to the captured groups) so we use a raw
# string for that as well.
regex = r"([a-zA-Z]+) (\d+)"

# This will reorder the string and print:
#   24 of June, 9 of August, 12 of Dec
print(re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12"))

