import time
from datetime import datetime

current_time = time.time()
formatted = f"{current_time:,.4f}"
scientific_notation = f"{current_time:.2e}"

current_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted} or {scientific_notation} in scientific notation")
print(current_date)