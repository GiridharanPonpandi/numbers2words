from eng_numbers_to_words_0_to_999 import *
decimal_number = ''
inp = "911"
inp = str(inp).replace(",","")
if inp.count(".") > 1:
    inp = inp.replace(".","")
elif inp.count(".") == 1:
    point_pos = inp.index(".")
    decimal_number = inp[point_pos+1:]
    inp = inp.replace(".","")
elif inp.count(".") > 1:
    inp.replace(".","")
rupee = eng_numbers_to_words_0_to_999(inp)
paise = '' or decimal_number
if paise:
    if len(paise) > 2:
        paise = paise[:2]
    paise = eng_numbers_to_words_0_to_999(paise)
    print("Rupees "+rupee+" and "+paise+" paise")
else:
    print(rupee)
