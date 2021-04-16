# Run With Docker

## Open terminal 1
## Run all the commands line by line
- docker build -t name .
- docker run -itd name bash commands.sh
- cd server
- python app.py
## Open terminal 2
## Run all the commands line by line
- docker run -itd name bash commands1.sh
- npm install --save
- npm run serve
## Open browser with http://localhost:8080/


# Run Without Docker

## Open terminal 1
## Run all the commands line by line
- pip install -r requirements.txt
- cd server
- python app.py
## Open terminal 2
## Run all the commands line by line
- cd wiki_view
- npm install --save
- npm run serve
## Open browser with http://localhost:8080/