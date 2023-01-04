import os

site = 'google.com'
ping = os.system(f'ping {site}')
print(ping)
