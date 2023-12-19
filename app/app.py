from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import sentry_sdk
from flask import Flask, jsonify, request

sentry_sdk.init(
    dsn="https://127e735d2fff5cdf04c65db1d3bb20cd@o4506300835758080.ingest.sentry.io/4506408500199424",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

# Load environment variables from a .env file
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
## DB_PORT = int(os.getenv("DB_PORT", 3306))
## DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Creating a connection string
connect_args = {'ssl': {'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'

# Create the SQLAlchemy engine
engine = create_engine(
    connection_string,
    connect_args=connect_args
)

# Create a flask application

app = Flask(__name__)


@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/allergy_testing')
def allergy_testing():
    with engine.connect() as connection:
        query1 = text('SELECT * FROM allergy_tests')
        result1 = connection.execute(query1)
        db_data1 = result1.fetchall()
    return render_template('allergy_testing.html', data1=db_data1)

@app.route('/patients')
def patients():
    with engine.connect() as connection:
        query2 = text('SELECT * FROM patients')
        result2 = connection.execute(query2)
        db_data2 = result2.fetchall()
    return render_template('patients.html', data2=db_data2)

## create a route that throws an error
@app.route('/error')
def error():
    raise Exception('This is a test error for Sentry Testing')

patients_data = [
    {"id": "131313", "first_name": "Phillip", "last_name": "Duran", "date_of_birth": "1996-07-22", "gender": "Male"},
    {"id": "878787", "first_name": "Alan", "last_name": "Brown", "date_of_birth": "1967-08-06", "gender": "Male"},
    {"id": "101010", "first_name": "Mark", "last_name": "Dixon", "date_of_birth": "1980-12-22", "gender": "Male"},
    {"id": "181818", "first_name": "Renee", "last_name": "Garcia", "date_of_birth": "2021-03-28", "gender": "Female"},
    {"id": "636363", "first_name": "Joshua", "last_name": "Holmes", "date_of_birth": "1962-08-19", "gender": "Male"},
    {"id": "123456", "first_name": "Daniel", "last_name": "Rivera", "date_of_birth": "2016-10-26", "gender": "Male"},
    {"id": "127464", "first_name": "Rita", "last_name": "Perry", "date_of_birth": "1999-06-17", "gender": "Female"},
    {"id": "765434", "first_name": "Joanne", "last_name": "Washington", "date_of_birth": "1989-03-29", "gender": "Female"},
    {"id": "041408", "first_name": "Nathan", "last_name": "Howard", "date_of_birth": "2013-06-23", "gender": "Male"},
    {"id": "190814", "first_name": "Alexandra", "last_name": "Barnett", "date_of_birth": "1970-08-11", "gender": "Female"}
]

@app.route('/foodallergyapi/patients', methods=['GET'])
def get_patients():
    return jsonify({'patients': patients_data})

if __name__ == '__main__':
    app.run(debug=True)


#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000)

