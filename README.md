# Django Blog App

A simple blogging application built with Django, a popular Python web framework.

## Features

* Create, read, update, and delete blog posts
* User authentication and registration



## Requirements

* Python 3.6 or later
* Django 3.2 or later

## Installation

1. Clone the repository:

```bash
git clone [https://github.com/SamLinoFinnegan/MyBlog.git](https://github.com/SamLinoFinnegan/MyBlog.git)

cd Blog-App
python3 -m venv venv
```
# Windows
```
venv\Scripts\activate
```
# macOS/Linux
```
source venv/bin/activate

python manage.py migrate

python manage.py runserver

```
9. Open your web browser and go to `http://localhost:8000/` to access the blog app.

## Usage

1. Create a new user and log in.
2. Create, edit, and delete blog posts.
3. Customize the theme by modifying the `templates` directory.


## Contributing

If you would like to contribute to the Django Blog App, please fork the repository and submit a pull request.

## License

The Django Blog App is licensed under the MIT License.

## Acknowledgments

This project was inspired by the following resources:

* Django Tutorial: [https://docs.djangoproject.com/en/3.2/intro/](https://docs.djangoproject.com/en/3.2/intro/)
* Bootstrap CSS Framework: [https://getbootstrap.com/](https://getbootstrap.com/)

## Additional Notes

* The admin panel is accessible at `http://localhost:8000/admin`.
* The database is populated with sample data for development purposes. You can reset the database by running the following command:

bash
python manage.py reset-db


* To deploy the Django Blog App to production, you can use a service like Heroku or AWS Elastic Beanstalk.
