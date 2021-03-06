import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    citys = ['chicago','new york city','washington'] 
    city = input("choose a city from (chicago, new york city, washington) : ").lower()
    while(city not in citys):
        city = input("please type the correct city name from (chicago, new york city, washington) : ")
        
    # get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june','july','august','september','october','november','december']
    month = input("please choose all or a specific month : ").lower()
    while(month not in months):
        month = input("please type a correct month or all : ")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    day = input("please choose all or a specific day : ").lower()
    while(day not in days):
        day = input("please type a correct day or all : ")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months =['january','february','march','april','may','june']
    popular_month = months[df["month"].mode()[0]-1]
    print("the most common month is : {}".format(popular_month))

    # display the most common day of week
    print("the most common day of the week is : {}".format(df["day_of_week"].mode()[0]))

    # display the most common start hour
    popular_hour =  df['Start Time'].dt.hour.mode()[0]
    print("the most common hour is : {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

start_end = df[['Start Station', 'End Station']].mode().loc[0]

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()