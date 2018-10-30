import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    while True:
        try:
            city = input("\nEnter the name of the city that you want to see the data for \n the available options are (\'chicago,new york,washington\'): \n").lower()
            if city not in ['chicago','washington','new york']:
                print("\nKindly Enter correct city name")
                time.sleep(1)
                continue
            else:
                break
        except:
            print(" ")
    while True:
        try:
            filter = str(input("\nWould you like to filter the data \nby \'months\' or by \'days\' or by \'both\' months and days or \'none\' for no filter: \n")).lower()
            if filter not in ['months','days','both','none']:
                continue
            else:
                break
        except:
            print(" ")


    if filter == 'both':
        # get user input for month (all, january, february, ... , june)
        while True:
            try:
                month = input("\nEnter \'all\' or the name of the month by which you would like to filter : \noptions : all, january,february,march,april,may,june\n").lower()
                if month not in ['all','january','february','march','april','may','june']:
                    print("\nCAUTION !")
                    print("Enter the month from the above given list\n")
                    time.sleep(1)
                    continue
                else:
                    break
            except:
                print(" ")

        while True:
            try:
                day = input("\nEnter \'all\' or the name of the day by which you would like to filter: \n").lower()
                if day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                    print("\nThe entered day is incorrect so kindly retry !")
                    time.sleep(1)
                    continue
                else:
                    break
            except:
                print(" ")


    elif filter == 'months':
        while True:
            try:
                month = input("\nEnter \'all\' or the name of the month by which you would like to filter : \noptions : all, january,february,march,april,may,june\n").lower()
                day = 'all'
                if month not in ['all','january','february','march','april','may','june']:
                    print("\nCAUTION !")
                    print("Enter the month from the above given list\n")
                    continue
                else:
                    break
            except:
                print(" ")


    elif filter == 'days':
        while True:
            try:
                day = input("Enter \'all\' or the name of the day by which you would like to filter: \n").lower()
                month = 'all'
                if day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                    print("\nThe entered day is incorrect so kindly retry !")
                    time.sleep(1)
                    continue
                else:
                    break
            except:
                print(" ")
    elif filter == 'none':
        month = 'all'
        day = 'all'


    print('-'*40)
    return city,month,day

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months_list = ['january','february','march','april','may','june']
        month = months_list.index(month) + 1 # one is added to month so that it gives the correct number of the month

        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    time.sleep(1)
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    # display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    common_day = df['day'].mode()[0]
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common MONTH is ",common_month)
    print("Most common Day of the Week is ",common_day)
    print("Most common START HOUR is ",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return common_month,common_day,common_hour

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    time.sleep(1)
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    common = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print("\nMost commonly used start station : ",common_start_station)
    print("\nMost commonly used end station : ",common_end_station)
    print("\nCombination of Most frequently used both Start and End stations : ")
    print(common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    time.sleep(1)
    start_time = time.time()

    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    # display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()

    print("Total Trip Duration : {} seconds\n".format(total_trip_duration))
    print("Mean Trip Duration : {} seconds\n".format(mean_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats #1...\n')
    time.sleep(1)
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()

    print("Number of User Types : ")
    print(user_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_2(df):

    print('\nCalculating User Stats #2...\n')
    time.sleep(1)
    start_time = time.time()

    # Display counts of gender
    gender_count = df['Gender'].value_counts()

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    recent_birth_year   = df['Birth Year'].max()
    common_birth_year   = df['Birth Year'].mode()[0]

    print("Number of Genders : ")
    print(gender_count)

    print("\nEarlist or oldest Birth Year : ",int(earliest_birth_year))
    print("\nRecent or Youngest Birth Year : ",int(recent_birth_year))
    print("\nMost Common Birth Year : ",int(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    ask = str(input("\nWould you like to see the raw data ? - 5 lines  will displayed at a time: \noptions: yes or no\n")).lower()
    if ask.lower() == 'yes':
        for i in range(5,len(df.index),5):
            print(df.head(i))
            a = str(input("Would you like to continue to see more data ? \noptions: yes or no\n")).lower()
            if a.lower() == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if city.lower() != 'washington':
            user_stats_2(df)
        raw_data(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()