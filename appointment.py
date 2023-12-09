from datetime import datetime, timedelta

class Appointment:
    '''Class for Appointments'''
    
    def __init__(self, day_of_week, start_time_hour, client_name="",client_phone="", appt_type=0):
        '''Initializes Appointment object properties and constructs an objects with the said attributes'''
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type
        self.__day_of_week = day_of_week.capitalize()
        self.__start_time_hour = datetime.strptime(str(start_time_hour), '%H')
    
    def get_client_name(self):
        '''Getter for client name'''
        return self.__client_name

    def get_client_phone(self):
        '''Getter for client phone number'''
        return self.__client_phone
    
    def get_appt_type(self):
        '''Getter for appointment type'''
        return self.__appt_type
    
    def get_day_of_week(self):
        '''Getter for appointment day'''
        return self.__day_of_week
    
    def get_start_time_hour(self):
        '''Getter for appointment start time (hour)'''
        return self.__start_time_hour.strftime('%H:%M')
    
    def get_hour(self):
        '''Getter for appointment hour (simple)'''
        return str(self.__start_time_hour.strftime('%H'))
    
    def get_appt_type_desc(self):
        '''Getter for appointment type by description'''
        if int(self.__appt_type) == 0:
            return "Available"
        elif int(self.__appt_type) == 1:
            return "Mens Cut"
        elif int(self.__appt_type) == 2:
            return "Ladies Cut"
        elif int(self.__appt_type) == 3:
            return "Mens Colouring"
        elif int(self.__appt_type) == 4:
            return "Ladies Colouring"
    
    def get_end_time_hour(self):
        '''Getter for appointment end time (1 hour after start)'''
        return (self.__start_time_hour + timedelta(hours=1)).strftime('%H:%M')
    
    def set_client_name(self, update_client_name):
        '''Setter for client name'''
        self.__client_name = update_client_name
    
    def set_client_phone(self, update_client_phone):
        '''Setter for client phone number'''
        self.__client_phone = update_client_phone
    
    def set_appt_type(self, update_appt_type):
        '''Setter for appointment type'''
        self.__appt_type = update_appt_type
    
    def schedule(self, schedule_client_name, schedule_client_phone, schedule_client_appt_type):
        '''Setter for scheduling for client appointment'''
        self.__client_name = schedule_client_name
        self.__client_phone = schedule_client_phone
        self.__appt_type = schedule_client_appt_type
    
    def cancel(self):
        '''Reset client details for scheduled appointment'''
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0
    
    def format_record(self):
        '''Return a string representation of an appointment object'''
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour.strftime('%H')}"
    
    def __str__(self):
        '''Return a string representation of an appointment object'''
        return f"{self.__client_name:20s}{self.__client_phone:15s}{self.__day_of_week:10s}{self.__start_time_hour.strftime('%H:%M'):7s}{'-':3s}{self.get_end_time_hour():<10s}{self.get_appt_type_desc():<20s}"
    