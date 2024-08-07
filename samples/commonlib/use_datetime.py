from datetime import datetime, timezone

now = datetime.now()
print(f"now = {now}")
print(type(now))

dt = datetime(2024, 7, 25, 18, 12, 33)
print(dt)
print(dt.timestamp())

t = 1429417200.0
print(f"timestamp: {datetime.fromtimestamp(t)}")
print(f"utc timestamp: {datetime.fromtimestamp(t, timezone.utc)}")