#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    month = month.lower()
    if month == "january": return '01'
    elif month == "february": return '02'
    elif month == "march": return '03'
    elif month == "april": return '04'
    elif month == "may": return '05'
    elif month == "june": return '06'
    elif month == "july": return '07'
    elif month == "august": return '08'
    elif month == "september": return '09'
    elif month == "october": return '10'
    elif month == "november": return '11'
    elif month == "december": return '12'

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    list = []

    user_string = user_string.replace(",", "")

    for i in user_string.split(" "): list.append(i)

    parsed_month = parse_month(list[0])

    if int(list[1]) < 10:
        print(f'{parsed_month}/0{list[1]}/{list[2]}')

    else: print(f'{parsed_month}/{list[1]}/{list[2]}')
    

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    while input != "-1":
        parse_date(input())