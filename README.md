
# Voting System using Flask, jQuery, and SQL


## Features

- Create polls, with any number of options.
- Vote on different polls.
- Display results with charts and graphs.

## Drawbacks
No kind of security system is implemented. This is a minimal project on which you can expand on later.
## Instructions
In order to run this project, follow the steps mentioned below

- Make sure you have python 3.8 or above.
- Create a virtual environment in your project folder with this command:
```bash
virtualenv flaskenv
```

- Activate the virtual environment:
```bash
.\flaskenv\Scripts\Activate.ps1
```

- After activating, install all the required packages.
```bash
pip install flask
```

- Create a database. In this project, SQLite is used. Execute the sql commands given in the "queries.txt" file.
- In the terminal run the command:
```bash
python main.py
```

- After the server starts, navigate to "localhost:5000".
