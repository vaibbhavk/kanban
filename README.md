**_NOTE:_** This app is in development.

# Kanban Board

A [kanban board](https://en.wikipedia.org/wiki/Kanban_board) is one of the tools that can be used to implement kanban to manage work at a personal or organizational level.

## Authors

- [@vaibbhavk](https://github.com/vaibbhavk)

## Demo

The app is live: [https://k-for-kanban.herokuapp.com/](https://k-for-kanban.herokuapp.com/)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_URL`

## Features

- User authentication and authorization
- Lists and Cards for project management.
- User can see the summary of their performance, on the summary page. (coming soon!)

## Tech Stack

- Flask
- SQLAlchemy
- Jinja2

## Run Locally

Clone the project

```bash
  git clone https://github.com/vaibbhavk/kanban.git
```

Go to the project directory

```bash
  cd kanban
```

Create a virtual environment

```bash
  virtualenv venv
```

Activate virtual environment

```bash
  venv\Scripts\activate
```

Install dependencies through pip

```bash
  pip install -r requirements.txt
```

Start the app

```bash
  python main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
