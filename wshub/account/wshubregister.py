from wshub import module as ml
from wshub import app
from wshub import mail

# @app.route('/register',methods = ['POST', 'GET'])
@app.route("/wshub/account/registration", methods=['POST','GET'])
@ml.cross_origin()
def wshubregister():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            email = data['email']
            password = data['password']
        else:
            email = ml.request.form.get('email')
            password = ml.request.form.get('password')
        count = 0
        usercount = ml.config.user.find().count()
        totalcount = usercount + 1
        predata = "wshub-"
        uid = predata + "%07d"%totalcount
        print('WS-HUB userID',uid)
        if email in [temp['Email'] for temp in ml.config.user.find({}, {"Email":1} )]:
            return ml.jsonify({"status":"success","message":"Email ID Registered in Academy Database!"})
        else:
            temp_id = 20
            mail.sendinbluemail.wshubregistermail(uid, email, password, temp_id).wshub_registration_mail()
            return ml.jsonify({"status":"Success","message":"WS-HUB Register Successfully", "data":{"userID": uid, "email":email, "password": password }})
    return ml.render_template('account/wshubregister.html', title='WS-HUB Registration')
