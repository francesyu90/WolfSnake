import bottle
import os
import random

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#980000',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    

    # TODO: Do things with data
    direction = 'north'
    r=random.randint(0,3)
    mv=0
    if r==0:
        mv='north'
    if r==1:
        mv='east'
    if r==2:
        mv='south'
    if r==3:
        mv='west'
    
    if not data["food"]:
        return{
            'move': mv,
            'taunt':'AHHHHHHHHHH'
        }
    for wolf in data["snakes"]:
        if wolf["id"]=="afdccc0a-2f55-4092-b5b7-b65ab9a30b1e":
#            if data["food"][0][0]<wolf["coords"][0][0]:
                direction='west'
#            elif data["food"][0][0]>wolf["coords"][0][0]:
#                direction='east'
#            else:
#                if data["food"][0][1]>wolf["coords"][0][1]:
#                    direction='south'

    return {
        'move': test,
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
