# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:28:01 2024

@author: tomas
"""

from flask import Flask, jsonify, request


app=Flask(__name__)

@app.route("/")
def root():
    return "root"


if __name__=="__main__":
    app.run(debug=True)