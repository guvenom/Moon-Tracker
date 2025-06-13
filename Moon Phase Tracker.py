import ephem
import datetime


user_input = input("Enter the name of celestial body : ")
day = input("What day do you want to check? Format must be YYYY/MM/DD: ")

try:
    # Validate the date format before passing it to ephem
    datetime.datetime.strptime(day, "%Y/%m/%d")
except ValueError:
    print("Invalid date format. Please use YYYY/MM/DD.")
    exit(1)


try:
    celestial_body = getattr(ephem, user_input)()
except AttributeError:
    print(f"{user_input} is not a valid name of a celestial body")
    exit(1)


celestial_body.compute(day)

print('%s %s %s' % (celestial_body.ra, celestial_body.dec, celestial_body.mag))

print(ephem.constellation(celestial_body))



""" -Below other way of runnning the code with 3 different fucntions!-

import ephem

def main():
    user_input = input("Enter the name of celestial body: ")
    day = input("What day you want to check (format must be YYYY/MM/DD): ")
    
    celestial_body = get_celestial_body(user_input)
    if celestial_body:
        ra, dec, mag, constellation = compute_position(celestial_body, day)
        print('%s %s %s' % (ra, dec, mag))
        print(constellation)

        
def get_celestial_body(name):
    try:
        celestial_body = getattr(ephem, name)()
        return celestial_body
    except AttributeError:
        print(f"{name} is not a valid name of a celestial body")
        return None

def compute_position(celestial_body, date):
    celestial_body.compute(date)
    return celestial_body.ra, celestial_body.dec, celestial_body.mag, ephem.constellation(celestial_body)


if __name__ == "__main__":
    main()



"""