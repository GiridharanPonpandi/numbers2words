from numbers_list import *

def eng_numbers_to_words_0_to_999(number):

    length = len(str(number))
    temp_number = ''
    if length == 1:
        return eng_0_to_9[str(number)]
    elif length == 2:
        if number < 20:
            return eng_11_to_19[str(number)]
        if number > 19:
            temp_number = str(number)[0] + '0'
            if int(str(number)[1]) > 0:
                result = eng_10_to_90[temp_number] + ' ' + eng_0_to_9[str(number)[1]]
            else:
                result = eng_10_to_90[temp_number]
            return result
    elif length == 3:
        if int(str(number)[1]) == 0 and int(str(number)[2]) == 0:
            return eng_100_to_900[str(number)]

        elif int(str(number)[1]) == 0 and int(str(number)[2]) != 0:
            result = eng_100_to_900[str(number)[0] + "00"] + " " + "and" + " " + eng_0_to_9[str(number)[2]]
            return result

        elif int(str(number)[1]) != 0 and int(str(number)[2]) == 0:


            result = eng_100_to_900[str(number)[0] + "00"] + ' ' + "and" + " " + eng_10_to_90[str(number)[1] + "0"]
            return result
        else:
            if int(str(number)[1]) == 1:
                result = eng_100_to_900[str(number)[0] + "00"] + ' ' + "and" + " " + eng_11_to_19[str(number)[1] + str(number)[1]]
                return result
            else:
                result = eng_100_to_900[str(number)[0] + "00"] + ' '+ "and" + " " + eng_10_to_90[str(number)[1] + "0"] + " " + eng_0_to_9[str(number)[2]]
            return result
