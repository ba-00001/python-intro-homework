"""Warmup 4 - Use the datetime Module.

Prints today's date as "Today is April 24, 2026."
"""

# from ... import pulls one name out of the module, so I write datetime.now()
# rather than datetime.datetime.now(). The module and the class share a name,
# which is confusing until you've hit it once.
from datetime import datetime

today = datetime.now()

# strftime turns a datetime into text using format codes:
#   %B = full month name ("April"), %Y = four-digit year ("2026")
#
# The day is inserted with today.day rather than the %d code on purpose. %d
# zero-pads, so the 2nd of a month would come out "September 02, 2026". Using
# .day gives "September 2, 2026", which is how the date is actually written.
print(f"Today is {today.strftime(f'%B {today.day}, %Y')}.")
