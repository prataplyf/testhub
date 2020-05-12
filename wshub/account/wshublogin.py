from wshub import module as ml
from wshub import app
bcrypt = ml.Bcrypt()

app.config['SECRET_KEY'] = ml.config.master_key

@app.route('/wshub/account/userlogin', methods=['POST','GET'])
@ml.cross_origin()
def wshublogin():
    if ml.request.method == 'POST':
        auth = ml.request.authorization
        if ml.request.is_json:
            data = ml.request.get_json()
            mail = data['useremail']  #login mailID
            userpassword = data['userpassword']  # login Password
        else:
            mail = ml.request.form.get('useremail')   #login mailID
            userpassword = ml.request.form.get('userpassword')  # login Password
        # print(mail)
        # if mail in [temp['Email'] for temp in ml.config.user.find({}, {"Email":1} )]:
        login_user = ml.config.user.find_one({'Email':mail})
        if login_user:
            logindata =  ml.config.user.find_one({"Email":mail},{'Password':1, 'userID':1, 'Name':1, 'Email':1})
            pwd = logindata['Password']
            uid = logindata['userID']
            uname = logindata['Name']
            umail = logindata['Email']
            if bcrypt.check_password_hash(pwd, userpassword) == True:
                data={'Name':uname, 'Email':umail}
                print(data)
                token = ml.jwt.encode({'Data':data, 'exp':ml.datetime.datetime.utcnow() + ml.datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
                print('Token:', token)
                    # return jsonify({'Token':token.decode('UTF-8'), 'Message':"Login Success", "User ID":uid, "Name": uname, "Email":umail})
                msg = "logged in"
                return ml.jsonify({ "data":{"name": uname,
                                    "userid": uid,
                                    "email": umail,
                                    "token":token.decode('UTF-8')},
                                    "message": msg,
                                    "status":"success"
                                    })
                    #return "Login Success"
            else:
                return ml.jsonify({'status': "success",'message': "invalid email or password"})
                                            # 401, {'WWW-Authenticate' : 'Basic realme="Login Required"'})
        else:
            return ml.jsonify({'status': "success",'message': "no such user"})
    return ml.render_template('account/wshublogin.html', title='Sign_In')
