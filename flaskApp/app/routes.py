from app import app

@app.route('/weatherforecast')
def countries():
    return {"weatherdata":[{"date":"2022-05-28T21:50:29.9137137+05:30","temperatureC":-1,"temperatureF":31,"summary":"Mild"},{"date":"2022-05-29T21:50:29.9351683+05:30","temperatureC":11,"temperatureF":51,"summary":"Chilly"},{"date":"2022-05-30T21:50:29.9351783+05:30","temperatureC":51,"temperatureF":123,"summary":"Balmy"},{"date":"2022-05-31T21:50:29.9351787+05:30","temperatureC":11,"temperatureF":51,"summary":"Freezing"},{"date":"2022-06-01T21:50:29.9351788+05:30","temperatureC":32,"temperatureF":89,"summary":"Warm"}]}
