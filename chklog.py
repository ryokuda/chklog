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

# Pickup ips which made hundred status 404 accesses
#list404 = [ [count, ip] for ip, count in dict404.items() ]
IPs = [ ip for ip, count in dict404.items() if count >= 100 ]

# Count status 200 accesses
for ip in IPs:
    count = 0
    for acc in all_accesses:
        if acc[idx_ip] == ip and acc[idx_status] == 200:
            count += 1
    print( ip, count )
