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
    months = ['all','january','february','march','april','may','june']
    month = input("Enter any month of the first 6 months or enter All to select all 6 months. : ").lower()
    while(month not in months):
        month = input("Please enter Only one of the first 6 months or enter All to select all 6 months. : ")
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
        months =['january','february','march','april','may','june']
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
    months =['january','february','march','april','may','june','july']
    popular_month = months[df["month"].mode()[0]-1]
    print("the most common month is : {}".format(popular_month))

    # display the most common day of week
    print("the most common day of the week is : {}".format(df["day_of_week"].mode()[0]))

    # display the most common start hour
    popular_hour =  df['Start Time'].dt.hour.mode()[0]
    print("the most common hour is : {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("the most common Start Station is : {}".format(df["Start Station"].mode()[0]))

    # display most commonly used end station
    print("the most common End Station is : {}".format(df["End Station"].mode()[0]))

    # display most frequent combination of start station and end station trip
    start_end = df.groupby(["Start Station", "End Station"]).size().sort_values(ascending=False).index[0]

    print("the most common Start & End Station is : {} ".format(start_end))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_ravel_time = round(df['Trip Duration'].sum())
    print("the total travel time is : {} sec ".format(total_ravel_time))

    # display mean travel time
    mean_ravel_time = round(df['Trip Duration'].mean())
    print("the mean travel time is : {} sec ".format(mean_ravel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("the counts of user types :\n{}\n".format(df['User Type'].value_counts().to_frame()))

    # Display counts of gender unless its Washington city
    try:
        print("the counts of gender types :\n{}\n".format(df['Gender'].value_counts().to_frame()))
        # Display earliest, most recent, and most common year of birth
        print("earliest year of birth is : {} ".format(int(df['Birth Year'].min())))
        print("most recent year of birth is : {} ".format(int(df['Birth Year'].max())))
        print("most common year of birth is : {} ".format(int(df['Birth Year'].mode()[0])))
        
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except KeyError:
        print("Washington city doesnt have gender  or birth year data\n")


def display_data(df):
    """asking the user if he want to see 5 rows of raw data"""
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    #making sure the user input is only  yes/no 
    while(view_data  not in['yes','no']):
        view_data = input('please enter only yes or no\n').lower()
    #keep asking the user if he wants to see the next 5 rows of data     
    start_loc = 0
    while (view_data == "yes"):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input(" Do you want to see the next 5 rows of data? : ").lower()
                                 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
