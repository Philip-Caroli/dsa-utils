from bottle import Bottle, route, run, debug, template, static_file, request, error
import simple_db

app = Bottle()

@app.get('/')
def main():
    return template('tpl/pflanzen_uebersicht.tpl', plants=simple_db.plants)

@app.get('/pflanzen')
def pflanzen_ubersicht():
    return template('tpl/pflanzen_uebersicht.tpl', plants=simple_db.plants)

@app.get('/pflanze/<name>')
def pflanze(name):
    for plant in simple_db.plants:
        if name == plant['Name']:
            return template('tpl/pflanze.tpl', plant=plant)
    return "Pflanze " + name + " nicht gefunden!"


@app.route('/static/<filename>')
def serve_css(type, filename):
    return static_file(filename, root='/static/')

run(app, host='0.0.0.0', port=8081)