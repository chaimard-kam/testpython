import datetime

def calculate_parking_fee(entry_datetime, exit_datetime):
  """
  คำนวณค่าจอดรถ

  Args:
    entry_datetime: datetime object, วันที่และเวลาเข้าจอด
    exit_datetime: datetime object, วันที่และเวลาออกจากที่จอด

  Returns:
    int, ค่าจอดรถ
  """

  # คำนวณจำนวนชั่วโมงที่จอด
  total_hours = (exit_datetime - entry_datetime).total_seconds() / 3600

  # ตรวจสอบว่าจอดเกิน 24 ชั่วโมงหรือไม่
  if total_hours > 24:
    return 100

  # แยกจำนวนชั่วโมงออกเป็นช่วง
  free_hours = min(total_hours, 2)
  hour_3_5 = min(max(total_hours - 2, 0), 3)
  hour_6_up = max(total_hours - 5, 0)

  # คำนวณค่าจอดรถ
  parking_fee = 0
  parking_fee += hour_3_5 * 10
  parking_fee += hour_6_up * 5

  return parking_fee

def print1(entry_datetime, exit_datetime):
    # คำนวณจำนวนชั่วโมงที่จอด
  total_hours = (exit_datetime - entry_datetime).total_seconds() / 3600

  # แยกจำนวนชั่วโมงออกเป็นช่วง
  free_hours = min(total_hours, 2)
  hour_3_5 = min(max(total_hours - 2, 0), 3)
  hour_6_up = max(total_hours - 5, 0)

  print("ฟรี",free_hours)
  print("จำนวน ชม. 10 บาท : ",hour_3_5)
  print("จำนวน ชม. 5 บาท : ",hour_6_up)



# ตัวอย่างการใช้งาน
print("-------ป้อนข้อมูลเวลาเข้าจอด-------")
year1 = int(input("Year:"))
month1 = int(input("Month:"))
day1 = int(input("Day:"))
Hour1 = int(input("Hour:"))
Minute1 = int(input("Minute:"))

print("-------ป้อนข้อมูลเวลาออก-------")
year2 = int(input("Year:"))
month2 = int(input("Month:"))
day2 = int(input("Day:"))
Hour2 = int(input("Hour:"))
Minute2 = int(input("Minute:"))

entry_datetime = datetime.datetime(year1, month1, day1, Hour1, Minute1)
exit_datetime = datetime.datetime(year2, month2, day2, Hour2, Minute2)

parking_fee = calculate_parking_fee(entry_datetime, exit_datetime)

print("-------สรุปค่าจอด-------")
print1(entry_datetime, exit_datetime)
print("--------------")
print(f"ค่าจอดรถ: {parking_fee} บาท")
