# CONTRIBUTING

## How to run the Dockerfile locally
 '''
    docker run -dp 5000:5000 -w //app -v "//c/xampp/htdocs/python-flask-restapi://app" flask-smorest-api sh -c "flask run --host 0.0.0.0"
'''