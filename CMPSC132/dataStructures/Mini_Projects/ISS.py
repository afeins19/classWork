#!/bin/python3
import json
import turtle
import urllib.request
import time

# loading data from API
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())  # loading data into json
print(result)

# accessing/manipulating data for presentation
spaceCount = result['number']
ppl = result['people']
print('\nPeople in space: ', str(spaceCount) + '\n')
for p in ppl:
    print(p['name'])

# space station location
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('\n' + str(result))
location = result['iss_position']
lon = location['longitude']
lat = location['latitude']
pos = lat + ', ' + lon
print('\n' + pos)

# using turtles to display map
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# overhead plot:

# plot space center location
lat = 29.5502
lon = -95.097
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

# calling web service to retrieve pass times
url = 'http://api.open-notify.org/iss-pass.json' + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
passOverTime = result['response'][1]['risetime']
location.write(time.ctime(passOverTime), font=('Arial', 5))








