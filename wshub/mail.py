# This module used to send mail:
# At
# 1. Time of user registration
# 2. Time of forget password/ re-activate account
# 3. Time of slotBooking

from wshub import module as ml

class sendinbluemail():
    #
    # Academy Registration Mail
    class wshubregistermail():
        def __init__(self, uid, email, password, temp_id):
            self.uid = uid
            self.email = email
            self.password = password
            self.temp_id = temp_id
        #
        def wshub_registration_mail(self):
            configuration = ml.sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = ml.config.academy_mail_key
            api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
            send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                    to=[{"email": self.email ,"name": self.email}],
                                    template_id=self.temp_id,
                                    params={"name": self.email, "email": self.email, "pwd": self.uid},
                                    headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
            try:
                # Send a transactional email
                api_response = api_instance.send_transac_email(send_smtp_email)
                bcrypt = ml.Bcrypt()  # password Hashing
                pass_decode = bcrypt.generate_password_hash(self.password).decode('utf-8')
                if self.email not in [temp['Email'] for temp in ml.config.user.find({}, {"Email":1} )]:
                    ml.config.user.insert_one({"userID": self.uid, "Name": self.email, "Email":self.email, "Password":pass_decode })
                ml.pprint(api_response)
            except ml.ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    #
    #
    #
