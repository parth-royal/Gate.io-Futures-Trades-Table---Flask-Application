from datetime import datetime, timedelta

timestamp = "1677229044.775"
utc_time = datetime.utcfromtimestamp(float(timestamp))
ist_time = utc_time + timedelta(hours=5, minutes=30)

print("UTC time: ", utc_time)
print("IST time: ", ist_time)
