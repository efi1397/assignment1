import logging
import os
import json
import datetime

import requests
import pandas as pd

# --- Environment Variables
JSON_RESULT_PATH = os.getenv('JSON_RESULT_PATH', 'result.json')


def get_holidays() -> list:
    """
    This function returns holidays items from https://www.hebcal.com website
    :return: list of holidays
    """
    request = "https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year=now&month=x&ss=on&mf=on&c" \
              "=on&geo=geoname&geonameid=3448439&M=on&s=on "

    try:
        logging.info("Try to fetch holidays from https://www.hebcal.com")
        holidays = requests.get(request).json()["items"]
        logging.info("Holidays fetched successfully")

    except Exception as error:
        message = "Failed to fetch holidays from https://www.hebcal.com website,"
        f"error: {error}"

        logging.error(message)
        raise Exception(message)

    return holidays


def extract_holidays_according_to_quarter(holidays: list, quarter: int) -> list:
    """
    Extract the relevant hebrew holidays from holidays list
    :param holidays: All holidays
    :param quarter: The relevant quarter
    :return: holidays
    """
    relevant_holidays = []
    for holiday in holidays:
        if holiday['category'] == 'holiday' and get_quarter_from_date(holiday['date']) == quarter:
            holiday_result = {
                'holiday_hebrew_name': holiday['hebrew'],
                'date': holiday['date']
            }

            relevant_holidays.append(holiday_result)

    return relevant_holidays


def get_quarter_from_date(date: str) -> int:
    """
    Extract the period quarter number form date.
    :return: period quarter number
    """
    date_quarter = None

    try:
        pd_timestamp = pd.to_datetime(date)
        date_quarter = pd_timestamp.to_period('Q').quarter

    except Exception as error:
        logging.warning(f"Failed to parse {date}, error: {error}")

    return date_quarter


def execute():
    # Get all holidays
    holidays = get_holidays()

    # Get the relevant quarter
    current_date = datetime.date.today()
    next_quarter = get_quarter_from_date(pd.Timestamp(current_date) + pd.tseries.offsets.QuarterEnd() * 2)

    json_result = {
        'holidays': extract_holidays_according_to_quarter(holidays, next_quarter)
    }

    # Write result to json file
    try:
        logging.info(f"Try to write {JSON_RESULT_PATH}")
        with open(JSON_RESULT_PATH, 'w') as f:
            json.dump(json_result, f, ensure_ascii=False)

        logging.info(f"The {JSON_RESULT_PATH} file was written successfully")

    except Exception as error:
        logging.warning(f"Failed to publish {JSON_RESULT_PATH}, error: {error}")
