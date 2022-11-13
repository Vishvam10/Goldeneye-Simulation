import sys

from flask_restful import Resource
from flask import current_app as app
from flask import jsonify

from cli_color import COLORS

total_hits = 0
GET_hits = 0
POST_hits = 0
PUT_hits = 0
DELETE_hits = 0

# Prints HTTP method hit every LOG_FREQUENCY times
LOG_FREQUENCY = 100


class HitCountAPI(Resource):

    def get(self):
        global total_hits
        global GET_hits
        total_hits += 1
        GET_hits += 1
        if(total_hits % LOG_FREQUENCY == 0):
            msg = "\n{} GET Method Hit : {}".format(
                total_hits, GET_hits)
            print(COLORS.BOLD, COLORS.GREEN, msg, COLORS.END)
            sys.stdout.flush()
        data = {
            "No. of GET Hits": GET_hits,
            "No. of POST Hits": POST_hits,
            "No. of PUT Hits": PUT_hits,
            "No. of DELETE Hits": DELETE_hits,
            "No. of Total Hits": total_hits
        }
        return jsonify(data)

    def post(self):
        global total_hits
        global POST_hits
        total_hits += 1
        POST_hits += 1
        if(total_hits % LOG_FREQUENCY == 0):
            msg = "\n{} POST Method Hit : {}".format(
                total_hits, POST_hits)
            print(COLORS.BOLD, COLORS.CYAN, msg, COLORS.END)
            sys.stdout.flush()
        data = {
            "No. of GET Hits": GET_hits,
            "No. of POST Hits": POST_hits,
            "No. of PUT Hits": PUT_hits,
            "No. of DELETE Hits": DELETE_hits,
            "No. of Total Hits": total_hits
        }
        return jsonify(data)

    def put(self):
        global total_hits
        global PUT_hits
        total_hits += 1
        PUT_hits += 1
        if(total_hits % LOG_FREQUENCY == 0):
            msg = "\n{} PUT Method Hit : {}".format(
                total_hits, PUT_hits)
            print(COLORS.BOLD, COLORS.BLUE, msg, COLORS.END)
            sys.stdout.flush()
        data = {
            "No. of GET Hits": GET_hits,
            "No. of POST Hits": POST_hits,
            "No. of PUT Hits": PUT_hits,
            "No. of DELETE Hits": DELETE_hits,
            "No. of Total Hits": total_hits
        }
        return jsonify(data)

    def delete(self):
        global total_hits
        global DELETE_hits
        total_hits += 1
        DELETE_hits += 1
        if(total_hits % LOG_FREQUENCY == 0):
            msg = "\n{} DELETE Method Hit : {}".format(
                total_hits, DELETE_hits)
            print(COLORS.BOLD, COLORS.PINK, msg, COLORS.END)
            sys.stdout.flush()
        data = {
            "No. of GET Hits": GET_hits,
            "No. of POST Hits": POST_hits,
            "No. of PUT Hits": PUT_hits,
            "No. of DELETE Hits": DELETE_hits,
            "No. of Total Hits": total_hits
        }
        return jsonify(data)
