from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import sentry_sdk

sentry_sdk.init(
    dsn="https://127e735d2fff5cdf04c65db1d3bb20cd@o4506300835758080.ingest.sentry.io/4506408500199424",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
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
    
if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )