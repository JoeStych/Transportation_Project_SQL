import psycopg2 as psyc
import xml.etree.ElementTree as ET


#Connect to the database
try:
    connection = psyc.connect(
        host="localhost",
        database="tevents2",
        user="postgres",
        password="password"
    )
    
    cursor = connection.cursor()
    
    print("Connection successful.\n")


except (Exception, psyc.Error) as error:
    print("Error while connecting to PostgreSQL.")
    quit()

print("Connected to the PostgreSQL database.")

#reading network XML file
print("Filling nodes...")
tree = ET.parse("D:\\Desktop\\Projects\\Code\\SQL\\CSCI 411 Final Project\\network.xml")
root = tree.getroot()

n = 0

#filling nodes
for node in root.find('nodes'):
    id = node.get('id')
    x = node.get('x')
    y = node.get('y')
    
    insert_query = f"INSERT INTO nodes VALUES ('{id}', {x}, {y});"
    
    cursor.execute(insert_query)
    n += 1
    if n % 10000 == 0:
        print("Node", n, "has been added.")

print("Nodes have been filled.", n, "nodes in total.\n")
print("Filling links...")
n = 0

#filling links
for link in root.find('links'):
    linkID = link.get('id')
    fromN = link.get('from')
    toN = link.get('to')
    length = link.get('length')
    capacity = link.get('capacity')
    freespeed = link.get('freespeed')
    permlanes = link.get('permlanes')
    modes = link.get('modes')
    
    insert_query = f"INSERT INTO links VALUES ('{linkID}', '{fromN}', '{toN}', {length}, {capacity}, {freespeed}, {permlanes}, '{modes}');"
    
    cursor.execute(insert_query)
    n += 1
    if n % 10000 == 0:
        print("Link", n, "has been added.")

print(n, "links were added to the DB.\n")
print("Adding events...")

#reading events XML file
tree = ET.parse("D:\\Desktop\\Projects\\Code\\SQL\\CSCI 411 Final Project\\output_events.xml")
root = tree.getroot()
eventID = 0

for event in root.findall('event'):
    eventID += 1
    time = event.get('time')
    type = event.get('type')
    
    link = event.get('link') if event.get('link') is not None else 'NULL'
    vehicle = event.get('vehicle') if event.get('vehicle') is not None else 'NULL'
    actType = event.get('actType') if event.get('actType') is not None else 'NULL'
    person = event.get('person') if event.get('person') is not None else 'NULL'
    distance = event.get('distance') if event.get('distance') is not None else 'NULL'
    mode = event.get('mode') if event.get('mode') is not None else 'NULL'
    amount = event.get('amount') if event.get('amount') is not None else 'NULL'
    purpose = event.get('purpose') if event.get('purpose') is not None else 'NULL'
    transPartner = event.get('transactionPartner') if event.get('transactionPartner') is not None else 'NULL'
    dvrpVehicle = event.get('dvrpVehicle') if event.get('dvrpVehicle') is not None else 'NULL'
    taskType = event.get('taskType') if event.get('taskType') is not None else 'NULL'
    taskIndex = event.get('taskIndex') if event.get('taskIndex') is not None else 'NULL'
    dvrpMode = event.get('dvrpMode') if event.get('dvrpMode') is not None else 'NULL'
    legMode = event.get('legMode') if event.get('legMode') is not None else 'NULL'
    networkMode = event.get('networkMode') if event.get('networkMode') is not None else 'NULL'
    relPos = event.get('relativePosition') if event.get('relativePosition') is not None else 'NULL'
    request = event.get('request') if event.get('request') is not None else 'NULL'
    facility = event.get('facility') if event.get('facility') is not None else 'NULL'
    delay = event.get('delay') if event.get('delay') is not None else 'NULL'
    driverID = event.get('driverId') if event.get('driverId') is not None else 'NULL'
    vehicleID = event.get('vehicleId') if event.get('vehicleId') is not None else 'NULL'
    transitLineID = event.get('transitLineId') if event.get('transitLineId') is not None else 'NULL'
    transitRouteID = event.get('transitRouteId') if event.get('transitRouteId') is not None else 'NULL'
    departureID = event.get('departureId') if event.get('departureId') is not None else 'NULL'
    agent = event.get('agent') if event.get('agent') is not None else 'NULL'
    atStop = event.get('atStop') if event.get('atStop') is not None else 'NULL'
    destinationStop = event.get('destinationStop') if event.get('destinationStop') is not None else 'NULL'
    x = event.get('x') if event.get('x') is not None else 'NULL'
    y = event.get('y') if event.get('y') is not None else 'NULL'
    
    
    if link == 'NULL':
        insert_query = f'''
        INSERT INTO events
        VALUES ({time}, '{type}', NULL, '{vehicle}', '{actType}', '{person}', {distance}, '{mode}', {amount}, '{purpose}', '{transPartner}', '{dvrpVehicle}',
        '{taskType}', '{taskIndex}', '{dvrpMode}', '{legMode}', '{networkMode}', {relPos}, '{request}', '{facility}', {delay}, '{driverID}', '{vehicleID}',
        '{transitLineID}', '{transitRouteID}', '{departureID}', '{agent}', '{atStop}', '{destinationStop}' 
        );
        '''
    else:
        insert_query = f'''
        INSERT INTO events
        VALUES ({time}, '{type}', '{link}', '{vehicle}', '{actType}', '{person}', {distance}, '{mode}', {amount}, '{purpose}', '{transPartner}', '{dvrpVehicle}',
        '{taskType}', '{taskIndex}', '{dvrpMode}', '{legMode}', '{networkMode}', {relPos}, '{request}', '{facility}', {delay}, '{driverID}', '{vehicleID}',
        '{transitLineID}', '{transitRouteID}', '{departureID}', '{agent}', '{atStop}', '{destinationStop}' 
        );
        '''
    
    cursor.execute(insert_query)
    
    if eventID % 10000 == 0:
        print("Event", eventID, "was just added.")


print("Finished adding data.")

connection.commit()
cursor.close()
connection.close()
