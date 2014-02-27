'''
Problem 17
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
#In Java I wrote a much more robust answer to this question that was able to process numbers through a million.
#I started to rewrite that code but ultimately decided to just get an answer uploaded.
#Thus, this solution is overwritten in its current form for the task at hand despite having
#no additional functionality. It also resulted from a switch from arrays to dicts.

ones_dict =	{'0':'','1':'one','2':'two','3':'three','4':'four','5':'five',
				'6':'six','7':'seven','8':'eight','9':'nine'}
				
teens_dict = {'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
				'16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
tens_dict =	{'0':'','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty',
				'7':'seventy','8':'eighty','9':'ninety'}

hundred = "hundred"
thousand = "thousand"

sum_str_len = 0
for i in range(1,1001):
	i_english = ''
	i_str = str(i)
	
	if len(i_str)>2:
		if len(i_str)>3:
			i_english+=ones_dict[i_str[-4]]+thousand
		if i_str[-3]!='0':
			i_english+=ones_dict[i_str[-3]]+hundred
			if i_str[-2:]!='00':
				i_english+='and'
	
	if teens_dict.has_key(i_str[-2:]):	
		i_english+=teens_dict[i_str[-2:]]
	else:
		if i>9:
			i_english+=tens_dict[i_str[-2]]
		i_english+=ones_dict[i_str[-1]]
	print i_english
	sum_str_len += len(i_english)

print sum_str_len
