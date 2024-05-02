from flask import redirect, session, url_for
from functools import wraps


def session_required(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        if not session.get('user_id',''):
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return decorator