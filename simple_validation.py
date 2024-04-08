# -----------
# User Instructions
# 
# Modify the valid_day() function to verify 
# whether the string a user enters is a valid 
# day. The valid_day() function takes as 
# input a String, and returns either a valid 
# Int or None. If the passed in String is 
# not a valid day, return None. 
# If it is a valid day, then return 
# the day as an Int, not a String. Don't 
# worry about months of different length. 
# Assume a day is valid if it is a number 
# between 1 and 31.
# Be careful, the input can be any string 
# at all, you don't have any guarantees 
# that the user will input a sensible 
# day.
#
# Hint: The string function isdigit() might be helpful.

def valid_day(day):
    if day.isdigit():
        day = int(day)
        if day in range(1,32):
            return day


# print valid_day('0') 
# => None    
# print valid_day('1') 
# => 1
# print valid_day('15') 
# => 15
# print valid_day('500') 
# => None


# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    if str(month).capitalize() in months:
        return str(month).capitalize()


# print valid_month("january") 
# => "January"    
# print valid_month("January") 
# => "January"
# print valid_month("foo")
# => None
print valid_month("")
# => None


# -----------
# User Instructions
# 
# Modify the valid_year() function to verify 
# whether the string a user enters is a valid 
# year. If the passed in parameter 'year' 
# is not a valid year, return None. 
# If 'year' is a valid year, then return 
# the year as a number. Assume a year 
# is valid if it is a number between 1900 and 
# 2020.
#

def valid_year(year):
    if year.isdigit():
        year = int(year)
        if year in range(1900,2021):
            return year


#print valid_year('0') 
#=> None    
#print valid_year('-11') 
#=> None
#print valid_year('1950') 
#=> 1950
#print valid_year('2000') 
#=> 2000


