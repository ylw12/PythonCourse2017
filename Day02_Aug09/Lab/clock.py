class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
        if len(str(self.hour)) == 1:
            self.hour = '0%s' %(self.hour)
        else: pass
        if len(str(self.minutes)) == 1:
            self.minutes = '0%s' %(self.minutes)
        else: pass
        return '%s:%s' %(self.hour, self.minutes)
    
    def __add__(self, minutes):
        new_minutes = int(self.minutes) + int(minutes)
        if new_minutes >= 60:
            while new_minutes >= 60:
                new_minutes -= 60
                self.minutes = new_minutes
                self.hour = int(self.hour) + 1
        else: self.minutes = new_minutes
        if self.hour >= 24:
            while self.hour >= 24:
                self.hour -= 24
        else:pass
        return Clock(self.hour, self.minutes)

    def __sub__(self, minutes):
        new_minutes = int(self.minutes) - int(minutes)
        if new_minutes < 0:
            while new_minutes < 0:
                new_minutes += 60
                self.minutes = new_minutes
                self.hour = int(self.hour) - 1
        else: self.minutes = new_minutes
        if self.hour < 0:
            while self.hour < 0:
                self.hour += 24
        else: pass
        return Clock(self.hour, self.minutes)
    
    def __eq__(self, other):
        if self.hour == other.hour and self.minutes == other.minutes:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.hour == other.hour and self.minutes == other.minutes:
            return False
        else:
            return True
