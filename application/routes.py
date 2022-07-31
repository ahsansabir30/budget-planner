from application import app, db
from flask import render_template, url_for, flash, redirect, request

@app.route('/')
def home():
    return 'Hello, World!'
