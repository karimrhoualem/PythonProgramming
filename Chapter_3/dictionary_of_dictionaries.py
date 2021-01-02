import pprint

people = {}

people['Ford'] = {
    'Occupation': 'Researcher',
    'Gender':'Male',
    'Home Planet':'Betelgeuse Seven',
    'Name':'Ford Prefect'
    }

people['Arthur'] = {
    'Occupation': 'Sandwich-Maker',
    'Gender':'Male',
    'Home Planet':'Earth',
    'Name':'Arthur Dent'
    }

people['Trillian'] = {
    'Occupation': 'Mathematician',
    'Gender':'Female',
    'Home Planet':'Earth',
    'Name':'Tricia McMillan'
    }

people['Robot'] = {
    'Occupation': 'Paranoid Android',
    'Gender':'Unknown',
    'Home Planet':'Unknown',
    'Name':'Marvin'
    }

pprint.pprint(people)
