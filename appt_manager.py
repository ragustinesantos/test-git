import os
from appointment import Appointment

def show_appointments_by_name(appointment_list, name):
    '''Function for showing appointments based on input name'''
    print_appointment_header()
    appointment_exists = False
    for appointment in appointment_list:
        if name.lower() in appointment.get_client_name().lower():
            appointment_exists = True
            print(appointment)
    if not appointment_exists:
        print("No appointments found.")

def show_appointments_by_day(appointment_list, day):
    '''Function for showing appointments based on input day'''
    print_appointment_header()
    for appointment in appointment_list:
        if day.lower() == appointment.get_day_of_week().lower():
            print(appointment)

def print_appointment_header():
    '''Function for printing table_header'''
    print(f"{'Client Name':20s}{'Phone':15s}{'Day':10s}{'Start':7s}{'':3s}{'End':<10s}{'Type':<20s}")
    print("-"*80)

def create_weekly_schedule(appointment_list, open_days):
    '''Function for populating the appointment list with appointment objects'''
    for day in open_days:
        for time in range(9,17):
            time_slot = Appointment(day, time)
            appointment_list.append(time_slot)

def save_scheduled_appointments(appointment_list):
    '''Function for saving scheduled appointments to a file'''
    appointment_count = 0
    filename = input("Enter appointment filename: \033[1m\033[4m")
    print('\033[0m', end='')
    if os.path.exists(filename):
        overwrite = input("File already exists. Do you want to overwrite it (Y/N)? \033[1m\033[4m")
        print('\033[0m', end='')
        if overwrite.upper() == "Y":
            file_obj = open(filename, "w")
        elif overwrite.upper() =="N":
            new_file = input("Enter appointment filename: \033[1m\033[4m")
            print('\033[0m', end='')
            file_obj = open(new_file, "w")
    else:
        file_obj = open(filename, "w")
    for scheduled_appointment in appointment_list:
        if (scheduled_appointment.get_appt_type() != 0):
            file_obj.write(scheduled_appointment.format_record()+"\n")
            appointment_count += 1
    file_obj.close()
    return print(f"{appointment_count} scheduled appointments have been successfully saved")

def find_appointment_by_time(day, hour, appointment_list):
    '''Function for retrieving appointment based on day and start hour input'''
    for appointment in appointment_list:
        if appointment.get_day_of_week().lower() == day.lower():
            if int(appointment.get_hour()) == int(hour):
                return appointment
    return

def load_scheduled_appointments(appointment_list):
    '''Function for loading appointments from a file'''
    num_appts = 0
    filename = input("Enter appointment filename: \033[1m\033[4m")
    print('\033[0m', end='')
    while not os.path.exists(filename):
        filename = input("File not found. Re-enter appointment filename: \033[1m\033[4m")
    print('\033[0m', end='')
    file_reader = open(filename, "r")
    for line in file_reader:
        values = line.split(",")
        hour = values.pop().strip()
        day = values.pop()
        appoint : Appointment = find_appointment_by_time(day, hour, appointment_list)
        appoint.set_appt_type(int(values.pop()))
        appoint.set_client_phone(values.pop())
        appoint.set_client_name(values.pop())
        num_appts += 1
    file_reader.close()
    return print(f"{num_appts} previously scheduled appointments have been loaded")

def print_menu():
    '''Function for printing menu'''
    selection = 0
    valid = [1, 2, 3, 4, 9]
    while selection not in valid:
        print("\n\nJojo's Hair Salon Appointment Manager")
        print("=====================================")
        print(" 1) Schedule an appointment")
        print(" 2) Find appointment by name")
        print(" 3) Print calendar for a specific day")
        print(" 4) Cancel an appointment")
        print(" 9) Exit the system")
        selection = int(input("Enter your selection: \033[1m\033[4m"))
        print('\033[0m', end='')
        if selection not in valid:
            print("Enter valid selection.")
    return selection

def main():
    '''Function for running the Application'''
    appointment_list : Appointment = []
    open_days_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print("Starting the Appointment Manager System")
    create_weekly_schedule(appointment_list, open_days_array)
    print("Weekly calendar created")
    load = input("Would you like to load previously scheduled appointments from a file (Y/N)? \033[1m\033[4m")
    print('\033[0m', end='')
    if load.lower() == "y":
        load_scheduled_appointments(appointment_list)
    selection = 0
    while selection != 9:
        selection = print_menu()
        if(selection == 1):
            print("\n** Schedule an appointment **")
            day = input("What day: \033[1m\033[4m")
            print('\033[0m', end='')
            hour = input("Enter start hour (24 hour clock): \033[1m\033[4m")
            print('\033[0m', end='')
            if (day.capitalize() not in open_days_array) or (int(hour) < 9) or (int(hour) > 16):
                print("Sorry that time slot is not in the weekly calendar!")
            else:
                appoint : Appointment = find_appointment_by_time(day, hour, appointment_list)
                if (appoint.get_appt_type() != 0):
                    print("Sorry that time slot is booked already!")
                else:
                    client_name = input("Client Name: \033[1m\033[4m")
                    print('\033[0m', end='')
                    client_phone = input("Client Phone: \033[1m\033[4m")
                    print('\033[0m', end='')
                    print("Appointment types")
                    print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
                    appointment_type = int(input("Type of Appointment: \033[1m\033[4m"))
                    print('\033[0m', end='')
                    if (appointment_type not in range (1,5)):
                        print("Sorry that is not a valid appointment type!")
                    else:
                        appoint.set_client_name(client_name)
                        appoint.set_client_phone(client_phone)
                        appoint.set_appt_type(appointment_type)
                        print("OK, " + appoint.get_client_name() + "'s appointment is scheduled!")
        elif(selection == 2):
            print("\n** Find appointment by name **")
            name = input("Enter Client Name: \033[1m\033[4m")
            print('\033[0m', end='')
            print("Appointments for " + name + "\n")
            show_appointments_by_name(appointment_list, name)
        elif(selection == 3):
            print("\n** Print calendar for a specific day **")
            day = input("Enter day of week: \033[1m\033[4m")
            print('\033[0m', end='')
            print("Appointments for " + day.capitalize() + "\n")
            show_appointments_by_day(appointment_list, day)
        elif(selection == 4):
            print("\n** Cancel an appointment **")
            day = input("What day: \033[1m\033[4m")
            print('\033[0m', end='')
            hour = input("Enter start hour (24 hour clock): \033[1m\033[4m")
            print('\033[0m', end='')
            if (day.capitalize() not in open_days_array) or (int(hour) < 9) or (int(hour) > 16):
                print("Sorry that time slot is not in the weekly calendar!")
            else:
                appoint : Appointment = find_appointment_by_time(day, hour, appointment_list)
                if (appoint.get_appt_type() == 0):
                    print("That time slot isn't booked and doesn't need to be cancelled")
                else:
                    print("Appointment: " + day.capitalize() + " " + appoint.get_start_time_hour() + " - " + appoint.get_end_time_hour() +
                        " for " + appoint.get_client_name() + " has been cancelled!")
                    appoint.cancel()
        elif(selection == 9):
            print("\n** Exit the system **")
            save = input("Would you like to save all scheduled appointments to a file (Y/N)? \033[1m\033[4m")
            print('\033[0m', end='')
            if save.upper() == "Y":
                save_scheduled_appointments(appointment_list)
            print("Good Bye!")

# Application
main()
