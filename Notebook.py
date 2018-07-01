# -*- coding: utf-8 -*-
import pandas as pd
from datetime import date

import sys

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)


months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
               'Nov': 11, 'Dec': 12, 'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
               'September': 9, 'October': 10, 'November': 11, 'December': 12}


def date_sorter():
    all_formatted_dates = []

    # datetime.date(year, month, day)
    my_strings = df.str.extractall(r'(((\d{1,2})[/-](\d{1,2})[/-](\d{4}|\d{2}))|((\d{1,2})[/-](\d{4})))')

    for string in my_strings[0]:

        if (str(string) != 'nan'):
            # Only Month and Year provided
            slashes = string.count('/')
            dashes = string.count('-')

            print(string)
            print(slashes)
            print(dashes)

            if (slashes > 0):
                if (slashes == 1):
                    i = string.find('/')
                    formatted = (int(string[i+1:]), months_dict[string[:i]], 1)
                else:
                    if (int(string[string.find('/') + 1:string.rfind('/')]) < 32):
                        #print (string[:string.find('/')])
                        #print (string[string.find('/') + 1:string.rfind('/')])
                        #print (string[string.rfind('/') + 1:])

                        if (len(string) - (string.rfind('/') + 1) < 3):
                            formatted = date(int('19'+string[string.rfind('/') + 1:]), int(string[:string.find('/')]),
                                         int(string[string.find('/') + 1:string.rfind('/')]))
                        else:
                            formatted = date(int(string[string.rfind('/') + 1:]), int(string[:string.find('/')]),
                                             int(string[string.find('/') + 1:string.rfind('/')]))
            elif (dashes > 0):
                if (dashes == 1):
                    i = string.find('-')
                    formatted = (int(string[i + 1:]), months_dict[string[:i]], 1)
                else:
                    if (int(string[string.find('-') + 1:string.rfind('-')]) < 32):
                        #print (string[:string.find('-')])
                        #print (string[string.find('-') + 1:string.rfind('-')])
                        #print (string[string.rfind('-') + 1:])

                        if (len(string) - (string.rfind('-') + 1) < 3):
                            formatted = date(int('19'+string[string.rfind('-') + 1:]), int(string[:string.find('-')]),
                                         int(string[string.find('-') + 1:string.rfind('-')]))
                        else:
                            formatted = date(int(string[string.rfind('-') + 1:]), int(string[:string.find('-')]),
                                             int(string[string.find('-') + 1:string.rfind('-')]))
            else:
                print('Something is wrong')
                formatted = None

            if (formatted != None) and not (formatted in all_formatted_dates):
                all_formatted_dates.append(formatted)
                del formatted

    sys.exit(all_formatted_dates)
    my_strings = df.str.extract(r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(st|nd|rd|th)? (\d{4}|\d{2}))')
    for string in my_strings[0]:
        if (str(string) != 'nan'):

            start = string.find(' ')
            end = string.rfind(' ')

            if (len(string) - end <= 3):
                if (end-start >= 4):
                    formatted = date(int('19' + string[end + 1:]), months_dict[string[:start]],
                                     int(string[start + 1:end-2]))
                else:
                    formatted = date(int('19'+string[end + 1:]), months_dict[string[:start]], int(string[start + 1:end]))
            else:
                if (end-start >= 4):
                    formatted = date(int(string[end + 1:]), months_dict[string[:start]],
                                     int(string[start + 1:end-2]))
                else:
                    formatted = date(int(string[end + 1:]), months_dict[string[:start]],
                                     int(string[start + 1:end]))
            if (not (formatted in all_formatted_dates)):
                all_formatted_dates.append(formatted)


    my_strings = df.str.extract(
        r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December).? \d{1,2}(st|nd|rd|th)?,? (\d{4}|\d{2}))')

    for string in my_strings[0]:
        if (str(string) != 'nan'):
            # Assume space after . and , always --> Validated to be true

            start = string.find(' ')
            end = string.rfind(' ')

            # datetime.date(year, month, day)

            # year has 2 digits
            if (len(string) - end <= 3):

                if (string[start-1] is '.') and (string[end-1] is ','):
                    if (end - start >= 5):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[:start-1]],
                                         int(string[start + 1:end - 3]))
                    else:
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[:start-1]],
                                         int(string[start + 1:end - 1]))

                elif (string[start-1] is '.') and not(string[end-1] is ','):
                    if (end - start >= 4):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[:start-1]],
                                         int(string[start + 1:end - 2]))
                    else:
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[:start-1]],
                                         int(string[start + 1:end]))

                elif not(string[start - 1] is '.') and (string[end - 1] is ','):
                    if (end - start >= 5):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[:start]],
                                         int(string[start + 1:end - 3]))
                    else:
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[:start]],
                                         int(string[start + 1:end - 1]))

                else:
                    if (end - start >= 4):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[:start]],
                                         int(string[start + 1:end - 2]))
                    else:
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[:start]],
                                         int(string[start + 1:end]))

            # Year has 4 digits
            else:
                if (string[start-1] is '.') and (string[end-1] is ','):
                    if (end - start >= 5):
                        formatted = date(int(string[end + 1:]), months_dict[string[:start-1]],
                                         int(string[start + 1:end - 3]))
                    else:
                        formatted = date(int(string[end + 1:]), months_dict[string[:start-1]],
                                         int(string[start + 1:end - 1]))

                elif (string[start-1] is '.') and not(string[end-1] is ','):
                    if (end - start >= 4):
                        formatted = date(int(string[end + 1:]), months_dict[string[:start-1]],
                                         int(string[start + 1:end - 2]))
                    else:
                        formatted = date(int(string[end + 1:]), months_dict[string[:start-1]],
                                         int(string[start + 1:end]))

                elif not(string[start - 1] is '.') and (string[end - 1] is ','):
                    if (end - start >= 5):
                        formatted = date(int(string[end + 1:]), months_dict[string[:start]],
                                         int(string[start + 1:end - 3]))
                    else:
                        formatted = date(int(string[end + 1:]), months_dict[string[:start]],
                                         int(string[start + 1:end - 1]))

                else:
                    if (end - start >= 4):
                        formatted = date(int(string[end + 1:]), months_dict[string[:start]],
                                         int(string[start + 1:end - 2]))
                    else:
                        formatted = date(int(string[end + 1:]), months_dict[string[:start]],
                                         int(string[start + 1:end]))

            if (not (formatted in all_formatted_dates)):
                all_formatted_dates.append(formatted)

    my_strings = df.str.extract(
        r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)-\d{1,2}(st|nd|rd|th)?-(\d{4}|\d{2}))')

    for string in my_strings[0]:
        if (str(string) != 'nan'):
            start = string.find('-')
            end = string.rfind('-')

            # datetime.date(year, month, day)

            # 4-digit year
            if (len(string) - end > 3):
                # with th, rd, nd
                if (end - start >= 4):
                    formatted = date(int(string[end+1:]), months_dict[string[:start]], int(string[start+1:end-2]))
                else:
                    formatted = date(int(string[end + 1:]), months_dict[string[:start]], int(string[start + 1:end]))
            else:
                if (end - start >= 4):
                    formatted = date(int('19'+string[end+1:]), months_dict[string[:start]], int(string[start+1:end-2]))
                else:
                    formatted = date(int('19'+string[end + 1:]), months_dict[string[:start]], int(string[start + 1:end]))

            if (not (formatted in all_formatted_dates)):
                all_formatted_dates.append(formatted)

    my_strings = df.str.extract(
        r'(((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December) (\d{4}))|((\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)[,.]? (\d{4}|\d{2})))')


    for string in my_strings[0]:
        if (str(string) != 'nan'):

            # datetime.date(year, month, day)
            start = string.find(' ')
            end = string.rfind(' ')

            if (start == end):
                formatted = date(int(string[end+1:]), months_dict[string[:start]], 1)

                if (not (formatted in all_formatted_dates)):
                    all_formatted_dates.append(formatted)
                continue

            # 2-digit year
            if (len(string) - end <= 3):
                # with th, nd
                if (start > 2):
                    if (('.' in string) and ((',') in string)):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[start+1:end-2]],
                                         int(string[:start-2]))
                    elif (('.' in string) and not((',') in string)):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[start+1:end-1]],
                                         int(string[:start-2]))
                    elif (not('.' in string) and ((',') in string)):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[start + 1:end-1]],
                                         int(string[:start - 2]))
                    else:
                        #print(string[end + 1:])
                        #print(months_dict[string[start + 1:end]])
                        #print(string[:start - 2])
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[start + 1:end]],
                                         int(string[:start - 2]))
                else:
                    if (('.' in string) and ((',') in string)):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[start+1:end-2]],
                                         int(string[:start]))
                    elif (('.' in string) and not((',') in string)):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[start+1:end-1]],
                                         int(string[:start]))
                    elif (not('.' in string) and ((',') in string)):
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[start + 1:end-1]],
                                         int(string[:start]))
                    else:
                        formatted = date(int('19' + string[end + 1:]), months_dict[string[start + 1:end]],
                                         int(string[:start]))
            else:
                # with th, nd
                if (start > 2):
                    if (('.' in string) and ((',') in string)):
                        formatted = date(int(string[end + 1:]), months_dict[string[start + 1:end - 2]],
                                         int(string[:start - 2]))
                    elif (('.' in string) and not ((',') in string)):
                        formatted = date(int(string[end + 1:]), months_dict[string[start + 1:end - 1]],
                                         int(string[:start - 2]))
                    elif (not ('.' in string) and ((',') in string)):
                        formatted = date(int(string[end + 1:]), months_dict[string[start + 1:end - 1]],
                                         int(string[:start - 2]))
                    else:
                        formatted = date(int(string[end + 1:]), months_dict[string[start + 1:end]],
                                         int(string[:start - 2]))
                else:
                    if (('.' in string) and ((',') in string)):
                        formatted = date(int(string[end + 1:]), months_dict[string[start + 1:end - 2]],
                                         int(string[:start]))
                    elif (('.' in string) and not ((',') in string)):
                        formatted = date(int(string[end + 1:]), months_dict[string[start + 1:end - 1]],
                                         int(string[:start]))
                    elif (not ('.' in string) and ((',') in string)):
                        formatted = date(int(string[end + 1:]), months_dict[string[start + 1:end - 1]],
                                         int(string[:start]))
                    else:
                        formatted = date(int(string[end + 1:]), months_dict[string[start + 1:end]],
                                         int(string[:start]))

            if (not (formatted in all_formatted_dates)):
                all_formatted_dates.append(formatted)

    my_strings = df.str.extract(
        r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December) (\d{4}))')


    sys.exit(all_formatted_dates)


    print(all_dates)
    print(len(all_dates))

    return  # Your answer here

date_sorter()