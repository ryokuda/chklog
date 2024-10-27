f = open( './apache2.log', 'r')
lines = f.readlines()
all_accesses = [ line.split( ',' ) for line in lines ]

# Create a list of client's IP-address which caused 404 error
idx_ip = 0
idx_time = 3
idx_url = 4
idx_status = 5
clients404 = [ acc[idx_ip] for acc in all_accesses if acc[idx_status] == '404' ] 

# Create a dictionaly key :IP-address, value: its occurance
dict404 = {}
for client in clients404:
    if client in dict404:
        dict404[ client ] = dict404[ client ] + 1
    else:
        dict404[ client ] = 1

# Convert the dict to list and sort
list404 = [ [count, ip] for ip, count in dict404.items() ]
#list404.sort()

for count, ip in list404:
    print( count, ip )
