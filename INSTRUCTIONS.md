Set up docker container:
    In the receipt folder containing manage.py:
        Create a file .env for four environment variables.
            DJANGO_SECRET_KEY={generate your own secret key here surrounded with single quotes}
            DEBUG=True
            DJANGO_LOGLEVEL=info
            DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
        Run "docker build -t django-docker ." OR "docker compose up --build"

Start webservice:
    Deploy docker container, port 8000 is open on localhost for image

Send HTTP requests to webserver
    Navigate to http://localhost:8000/challenge/receipts/95e8f5b8-992a-466b-8cf7-d235ddd055c4/points and you should see the message "No receipt found for that ID."
    From a Bash terminal session, you can run "curl -H "Content-Type: application/json" -d @./examples/morning-receipt.json http://localhost:8000/challenge/receipts/process"