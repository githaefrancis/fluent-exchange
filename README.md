# Fluent Exchange

## Description
This is a Flask application that allows a user to view blogs posted. To create a blog, a user must create an account. A user is also able comment on blog posts.


## Author

Francis Githae

# Technologies

Python 3.8.10
Flask
Bootstrap
JQuery
Javascript

# Features
- Register for a account
- Login 
- Post a blog 
- View single blog
- Update profile picture
- View blogs you have posted
- Comment on a blog.
- Update a blog
- A writer can delete offensive comment.
- A user can subscribe to an alert service to be notified when a new blog is created.


## Setup and Installation

1. Clone the repository

```bash
git@github.com:githaefrancis/fluent-exchange.git
```

2. Navigate to project folder

```bash
cd fluent-exchange
```

3. Create a virtual environment
```
python3 -m venv <name>
```

4. Activate the virtual environment

source <name>/bin/activate

5. Install dependencies

```
pip intall -r requirements.txt
```

6. Create the .env variables in the root folder
```bash
touch .env
```
Create the environment  variables

export SECRET_KEY='<Your Secret Key>'
export MAIL_USERNAME=<email>
export MAIL_PASSWORD=<password>

**NB: The smtp service uses a gmail account.**

7. Load the environment variables

```bash
source .env
```
4. Grant the python executable permissions

```
chmod +x start.sh
```
5. Run the application

```
./start.sh
```

## Live Link

[Fluent Exchange](https://fluent.herokuapp.com/ )

## Contact
Email: mureithigithae@gmail.com

## License

This project is under the MIT License [click here for more information](LICENSE)

&copy; 2022 Francis Githae