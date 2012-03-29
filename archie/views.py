from archie import app, models, db
from flask import request, make_response, redirect, url_for, render_template, jsonify

# routes
@app.route('/')
def index():
    """ Just redirect to /pois """
    return redirect(url_for('pois'))
    
@app.route('/pois')
def pois():
    """ Show all pois """
    resp = make_response(render_template('pois.xml', pois=models.Poi.query.all()))
    resp.headers['Content-type'] = 'text/xml'
    return resp

@app.route('/target_add')
def target_add():
    """ Record a target on user interaction in the Wikitude map or AR display """
    attrs=request.args.to_dict()
    t = models.Target(**request.args.to_dict())
    db.session.add(t)
    db.session.commit()
    return make_response(t.__repr__())

@app.route('/target_report')
def target_report():
    """ Get a repost, in JSON format, on all currently recorded targets """
    targets_list=[]
    targets=models.Target.query.all()
    for t in targets:
        targets_list.append({"poi_id": t.poi_id, "action": t.action, "ip": t.ip, "user_agent": t.user_agent,
            "device": t.device, "action_time": t.action_time, "latitude": t.latitude, "longitude": t.longitude})
    return jsonify(targets=targets_list)
