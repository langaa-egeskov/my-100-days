import urllib.request

battle_table_url = ('https://raw.githubusercontent.com/' +
                    'talkpython/100daysofcode-with-python-course/master/' +
                    'days/13-15-text-games/data/battle-table.csv')

sample_reader_url = ('https://raw.githubusercontent.com/' +
                     'talkpython/100daysofcode-with-python-course/master/' +
                     'days/13-15-text-games/data/sample_reader.py')


urllib.request.urlretrieve(battle_table_url, 'battle-table.csv')
urllib.request.urlretrieve(sample_reader_url, 'sample_reader.py')
