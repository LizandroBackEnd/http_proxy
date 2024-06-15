from flask import Flask, request, Response 
import requests 
import logging 

app = Flask(__name__) 

logging.basicConfig(level=logging.INFO) 

@app.route('/', defaults={'path': ''}) 
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE']) 
def proxy(path): 
    url = f'http://example.com/{path}' 
    logging.info(f'Proxying request: {request.method} {request.url}') 

    for header, value in request.headers.items(): 
        logging.info(f'Header request: {header}: {value}') 

    resp = requests.request( 
        method=request.method, 
        url=url, 
        headers={key: value for (key, value) in request.headers if key != 'Host'}, 
        data=request.get_data(), 
        cookies=request.cookies, 
        allow_redirects=False) 

    logging.info(f'Response: {resp.status_code} {resp.reason}') 
    for header, value in resp.headers.items(): 
        logging.info(f'Header response: {header}: {value}') 

    headers = [(name, value) for (name, value) in resp.raw.headers.items()] 
    response = Response(resp.content, resp.status_code, headers) 

    logging.info(f'Response content: {resp.text}')  
    return response 

if __name__ == '__main__':
    app.run(debug=True, port=8080)