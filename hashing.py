import requests
from cs50 import SQL
from flask import redirect, render_template, session, url_for
from functools import wraps
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

password = 1

print(generate_password_hash(string(password))
