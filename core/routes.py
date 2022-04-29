

from core import app, cache
from datetime import datetime
from random import choice
import string


from flask import render_template, request, flash, redirect, url_for

''' Initial index for the app '''
@app.route('/', methods=['GET', 'POST'])
def index():
    return "{'original':'...'}"

''' For decoding the given json body '''
@app.route('/decode', methods=['POST'])
@cache.cached(timeout=30)
def decode():
    content_type = request.headers.get('Content-Type')
    response = {}
    if (content_type == 'application/json'):
        json = request.json
        if request.method == 'POST':
            url = request.json['shortest']

            if not url:
                flash('The URL is required!')
                return 'URL is incorrect'
            short_id = url.rsplit('/', 1)[1]
            link = cache.get(short_id)

            if link:
                res_url = {"original": link, "status_code": 200}
                response = {**json, **res_url}
            else:
                err = {"status_code": 404, "msg":"link not found in memory"}
                response = { **err, **json,}
        return response
    else:
        return 'Content-Type not supported!'


''' For encoding the given json body '''
@app.route('/encode', methods=['POST'])
@cache.cached(timeout=30)
def encode():
    content_type = request.headers.get('Content-Type')
    response = {}
    if (content_type == 'application/json'):
        json = request.json
        if request.method == 'POST':
            url = request.json['original']
            if not url:
                flash('The URL is required!')
                return {'msg':'Invalid Url or Json Parameter', "status_code": 400}
            short_id = generate_short_id(8, url)
            cache.set(short_id, url)
            short_url = request.host_url + short_id
            res_url = {"id": short_id,"shortest": short_url, "status_code": 200}
            response = {**json, **res_url}
        return response
    else:
        return {'msg':'Content-Type not supported!', "status_code": 400}

''' For re-routing the clicked link to the original link from the cache memory '''
@app.route('/<short_id>')
def redirect_url(short_id):
    link = cache.get(short_id)
    if link:
        return redirect(link)
    else:
        flash('Invalid URL')
        return {"status_code": 404}


''' Function to generate short_id of specified number of characters '''
@cache.memoize(50)
def generate_short_id(num_of_chars, original):
    ''' 
        First check if the url already exists in our cache. 
        If it happens to be there, we don't generate a new ID.
    '''
    k_prefix = cache.cache.key_prefix
    keys = cache.cache._write_client.keys(k_prefix + '*')
    keys = [k.decode('utf8') for k in keys]
    keys = [k.replace(k_prefix, '') for k in keys]
    for k in keys:
        if(cache.get(k) == original):
            return k
        else:
            continue

    return  ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))
    
