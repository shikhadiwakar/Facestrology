import requests
from bs4 import BeautifulSoup as bs

def horoscope(zodiac):
    zodiac_signs = [
    'Aries',
    'Taurus',
    'Gemini',
    'Cancer',
    'Leo',
    'Virgo',
    'Libra',
    'Scorpio',
    'Sagittarius',
    'Capricorn',
    'Aquarius',
    'Pisces']

    for i in range(len(zodiac_signs)):
        if zodiac==zodiac_signs[i]:
            num=i
            break
        else:
            i+=1

    day =['yesterday','today','tomorrow']
    hs="Here is your Horoscope: \n"
    for i in day:

        result = requests.get(f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{i}.aspx?sign={(num+1)}')
        soup = bs(result.content, 'html.parser')
        data = soup.find('div', attrs={'class': 'main-horoscope'})
        hs=hs+(data.p.text)+'\n'+'\n'
    return(hs)

