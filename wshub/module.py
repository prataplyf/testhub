# @@@@@@@@@@@@@@@@@@@ Sendinblue module @@@@@@@@@@@@@@@@@@@@@@
import time
import time as t
# @@@@@@@@@@@@@@@@@@@ Sendinblue module End @@@@@@@@@@@@@@@@@@@@@@@@@
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# call database
from wshub import config
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from wshub import app
from flask import Flask, render_template, redirect, url_for, request, jsonify, request, make_response
# import jwt # @@@@@@@@@ PYJWT Token @@@@@@@@@@@
import datetime
import requests
# import pandas as pd
from functools import wraps
import pymongo
from flask import session
import string
import re
import jwt
from random import randint, choice
from socket import gaierror
# @@@@@@@@@@@@@@@@@@@ CROSS_ORIGIN ACCESS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from flask_cors import CORS, cross_origin

# @@@@@@@@@@@ STRIPE @@@@@@@@@@@@@@@@
# import stripe
# import razorpay


# Password Hashing
from flask_bcrypt import Bcrypt
