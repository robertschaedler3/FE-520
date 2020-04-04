class Time:
    def __init__(self, hours, minutes, seconds):
        if minutes > 60 or seconds > 60:
            raise ValueError(
                f'{"minutes" if minutes > 60 else "seconds"} must be less than 60')
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def addTime(self, time):
        ''' Adds a given amount of time to the current object. '''
        self.__seconds += time.seconds
        if self.seconds > 60:
            self.__seconds, self.__minutes = self.seconds % 60, self.minutes + self.seconds // 60

        self.__minutes += time.minutes
        if self.minutes > 60:
            self.__minutes, self.__hours = self.minutes % 60, self.hours + self.minutes // 60

        self.__hours += time.hours

    def displayTime(self):
        print(f'{self.hours} hrs and {self.minutes} mins and {self.seconds} sec')

    def displayMinute(self):
        print(f'{(self.hours*60*60) + (self.minutes * 60) + self.minutes}')


if __name__ == '__main__':
    t1 = Time(12, 45, 17)
    t1.displayTime()
    # 12 hrs and 45 mins and 17 sec

    t2 = Time(1, 24, 10)
    t2.displayTime()
    # 1 hrs and 24 mins and 10 sec

    t1.addTime(t2)

    t1.displayTime()
    # 14 hrs and 9 mins and 27 sec

    t1.displayMinute()
    # 50949
