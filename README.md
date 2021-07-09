## TO RUN

brief : https://gist.github.com/louisdorard/2652fc3b53b90c8492b732b5717f49e1

```
python -m venv env
``` 

```
. ./env/Scripts/activate`
```

```
pip install -r requirements.txt`
``` 

```
export FLASK_APP=api.py` 
```

```
flask run
``` 

```
curl --request POST \
  --url 'http://localhost:5000/submit' \
  --header 'accept: multipart/form-data' \
  -F 'file=@test2-predictions.csv'
```