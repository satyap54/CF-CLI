

# CodeForces Contest Reminder
Aimed at fetching information on CodeForces from the comfort of terminal.

A cli-tool made using python which is capable of setting reminder for the next CodeForces Round in your Google Calendar. Currently, I'm trying to add feature of fetching some publicly available information on CodeForces.


## Getting Started

### Installing

* Enable Google Calendar API by going here : https://developers.google.com/calendar/quickstart/python
This will generate a "credentials.json".
* Place your "credentials.json" inside "assets" of project directory.


```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
```
pip install requests
```
```
pip install pickle
```
```
pip install json
```
```
pip install click
```


### Executing program
```
git clone <this-repo>
cd CF-Contest_Reminder-master/
pip install --editable
cf --reminder
```

## To Do

 - Converting this into a full-fledged CLI
 - Better printing and formatting
