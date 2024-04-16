
def predict(dob):

	day=int(dob[0:2])
	month=dob[2:4]
    
	if month == '12':
		astro_sign = 'Sagitarius' if (day < 22) else 'Capricorn'

	elif month == '01':
		astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
		
	elif month == '02':
		astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
		
	elif month == '03':
		astro_sign = 'Pisces' if (day < 21) else 'Aries'
		
	elif month == '04':
		astro_sign = 'Aries' if (day < 20) else 'Taurus'
		
	elif month == '05':
		astro_sign = 'Taurus' if (day < 21) else 'Gemini'
		
	elif month == '06':
		astro_sign = 'Gemini' if (day < 21) else 'Cancer'
		
	elif month == '07':
		astro_sign = 'Cancer' if (day < 23) else 'Leo'
		
	elif month == '08':
		astro_sign = 'Leo' if (day < 23) else 'Virgo'
		
	elif month == '09':
		astro_sign = 'Virgo' if (day < 23) else 'Libra'
		
	elif month == '10':
		astro_sign = 'Libra' if (day < 23) else 'Scorpio'
		
	elif month == '11':
		astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
	
	else:
		astro_sign='error'
		
	return(astro_sign)
