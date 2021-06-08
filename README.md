


# CodeForces CLI
Aimed at fetching information on CodeForces from the comfort of terminal.

A cli-tool made using python which is capable of setting reminder for the next CodeForces Round in your Google Calendar. Currently, I'm trying to add feature of fetching some publicly available information on CodeForces.


## Getting Started

### Installation

* Enable Google Calendar API by going here : https://developers.google.com/calendar/quickstart/python
This will generate a "credentials.json".
* Place your "credentials.json" inside "assets" of project directory.


```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```


### Run
```
git clone <this-repo>
cd CF-Contest_Reminder-master/
pip install -r requirements.txt
pip install --editable .
cf --help
```

### Screenshot
![enter image description here](https://github.com/satyap54/CF-Contest_Reminder/blob/master/assets/CF-Cli-v2.png?raw=true)
## To Do

 - contest_data method in cli.py
 - Better printing and formatting
