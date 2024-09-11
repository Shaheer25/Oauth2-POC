import pytz

def generate_timezones_enum():
    # Retrieve all timezones from pytz
    timezones = pytz.all_timezones
    
    # Open a file to write the enum
    with open('timezones_enum.txt', 'w') as file:
        file.write('from enum import Enum\n\n')
        file.write('class TimeZone(Enum):\n')
        
        for tz in timezones:
            # Convert timezone string to a valid Python enum member name
            enum_name = tz.replace('/', '_').replace('-', '_').replace(' ', '_').replace('.', '_')
            file.write(f'    {enum_name} = "{tz}"\n')

if __name__ == "__main__":
    generate_timezones_enum()
    print("Timezones enum has been written to 'timezones_enum.txt'")
