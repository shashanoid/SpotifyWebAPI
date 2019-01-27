## Spotify Web API 
This is a flask web API that generates song data (previewURL, coverimage etc)

### Install Required tools

```coffee
pip install -r requirements.txt
```

### Run the server
```coffee
cd src
python2 app.py
```

Visit the URLs in this order:

-- http://localhost:8000/new
-- http://localhost:8000/list
-- http://localhost:8000/tracks

The last link displays the required data