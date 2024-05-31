from functools import wraps
from flask import session, redirect, url_for, flash



def auth(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'user' in session:
                user_roles = session['user'].get('roles', [])
                for role in roles:
                    if role in user_roles:
                        return func(*args, **kwargs)
                return {'message':'unauthorized'}, 401
            else:
                flash("Vous devez vous connecter pour accéder à cette page", 'error')
                return {'message':'Pleade connect'}, 401
        return wrapper
    return decorator


def andrana():
    print("me")

def liantso():
    print("liantsa aa")