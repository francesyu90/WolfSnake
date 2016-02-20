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
    mv=['north','east','south','west']
    for wolf in data["snakes"]:
        if wolf["id"]=="afdccc0a-2f55-4092-b5b7-b65ab9a30b1e":
            self=wolf
    if self['coords'][0][0]==0:
        mv.remove('west')
    elif self['coords'][0][0]==data["width"]-1:
        mv.remove('east')
    elif self['coords'][0][1]==0:
        mv.remove('north')
    elif self['coords'][0][1]==data["height"]-1:
        mv.remove('south')
    
    if not data["food"]:
        return{
            'move': mv[r],
            'taunt':'AHHHHHHHHHH'
        }
    
    if data["food"][0][0]<self["coords"][0][0] and 'west' in mv:
        direction='west'
    elif data["food"][0][0]>self["coords"][0][0] and 'east' in mv:
        direction='east'
    else:
        if data["food"][0][1]>self["coords"][0][1] and 'south' in mv:
            direction='south'

    return {
        'move': direction,
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
