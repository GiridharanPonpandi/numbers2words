# numbers2words 
Python package 
Convert numbers into words  English (Inter national format eg.million,billion).
num2wordsSI
#limitations is upto 17 digits for numbers before decimal point, the numbers after the decimal point gets stripped into 2 digit number and ouput is returned.
#giving a decimal pointer is optional
## Example

```python
from numbers2words.numbers2words import num2wordsSI

print(num2wordsSI(12345678))
ans:('twelve million three hundred and forty five thousand six hundred and seventy eight', '')
or
print(num2wordsSI(1234567.80))
ans:('one million two hundred and thirty four thousand five hundred and sixty seven', 'eighty')

or
print(num2wordsSI("12345678"))
ans:('twelve million three hundred and forty five thousand six hundred and seventy eight', '')
or
print(num2wordsSI("1234567.80"))
ans:('one million two hundred and thirty four thousand five hundred and sixty seven', 'eighty')

num2wordsIND
#limitations is upto 17 digits for numbers before decimal point, the numbers after the decimal point gets stripped into 2 digit number and ouput is returned.
#giving a decimal pointer is optional

## Example

#python
from numbers2words.numbers2words import num2wordsIND

print(num2wordsIND("12345678"))
ans:('one crore twenty three lakh forty five thousand six hundred and seventy eight', '')
or
print(num2wordsIND("1234567.80"))
ans:('twelve lakh thirty four thousand five hundred and sixty seven', 'eighty')
or
print(num2wordsIND(12345678))
ans:('one crore twenty three lakh forty five thousand six hundred and seventy eight', '')
or
print(num2wordsIND(1234567.80))
ans:('twelve lakh thirty four thousand five hundred and sixty seven', 'eighty')


num2wordsTA
#limitations is upto 18 digits for numbers before decimal point, the numbers after the decimal point gets stripped into 2 digit number and ouput is returned.
#giving a decimal pointer is optional
## Example

#python
from numbers2words.numbers2words import num2wordsTA
print(num2wordsTA(12345678))
ans:('ஒரு கோடியே இருபத்து மூன்று இலட்சத்து நாற்பத்து ஐந்து ஆயிரத்து அறுநூற்று எழுபத்து எட்டு', '')
or
print(num2wordsTA(1234567.80))
ans:('பன்னிரண்டு இலட்சத்து முப்பத்து நான்கு ஆயிரத்து ஐநூற்று அறுபத்து எழு', 'எண்பது')
or
print(num2wordsTA("12345678"))
ans:('ஒரு கோடியே இருபத்து மூன்று இலட்சத்து நாற்பத்து ஐந்து ஆயிரத்து அறுநூற்று எழுபத்து எட்டு', '')
or
print(num2wordsTA("1234567.80"))
ans:('பன்னிரண்டு இலட்சத்து முப்பத்து நான்கு ஆயிரத்து ஐநூற்று அறுபத்து எழு', 'எண்பது')



