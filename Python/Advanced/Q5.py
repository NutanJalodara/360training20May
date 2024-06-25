class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        total_hours = self.hours + other.hours + extra_hours
        return Time(total_hours, remaining_minutes)
    
    def displayMinute(self):
        return f"{self.minutes + (self.hours * 60)} minute(s)"

    def displayTime(self):
        return f"{self.hours} hour(s) and {self.minutes} minute(s)"

time1 = Time(2, 50)
time2 = Time(1, 20)
result = time1.addTime(time2)

print(f"Time 1: {time1.displayTime()}")
print(f"Time 2: {time2.displayTime()}")
print(f"Result: {result.displayTime()}")
print(f"{result.displayMinute()}")
