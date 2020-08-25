#Rob Rush refactoring of Udacity Course "Programming for Data Science with Python"
#Added file to GitHub for sharing
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = 'Unknown'
    while city not in ('chicago', 'new york city', 'washington'):
        print('Which city do you want Chicago, New York City, or Washington? \n[Please chose one of 3 cities or you will be asked again]')
        city = input().lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'Unknown'
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'June'):
        print('Which month do you want (All, January, February, March, April, May, June \n[Please chose one of 6 months or All or you will be asked again]')
        month = input().lower()
        
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'Unknown'
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print('Which day do you want All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n[Please chose one of 7 days or All or you will be asked again]')
        day = input().lower()
        

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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns #add hours for statistics
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    #print(df)#test code
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most popular month: ",popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most popular day: ",popular_day)

    # TO DO: display the most common start hour
    popular_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("Most popular Start Hour: ",popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most popular Start Station: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most popular End Station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combo_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print("Most popular Start and End Station Combo: ", popular_combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time: ", df['Trip Duration'].sum()/60/60/24, " days") #divide by 60/60/24 for days

    # TO DO: display mean travel time
    print("Mean Travel Time: ", df['Trip Duration'].mean()/60, " minutes") #divide by 60 for minutes

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    # TO DO: Display earliest, most recent, and most common year of birth
        early_by = df['Birth Year'].min()
        recent_by = df['Birth Year'].max()
        common_by = df['Birth Year'].mode()[0]
        print('\nEarliest Birth Year: {} \nMost Recent Birth Year: {} \nMost Common Birth Year: {} '.format(early_by, recent_by, common_by))
    else:    
        print('City does not collect gender or birth year info')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        print('Would you like to see 5 rows of raw data as a sample')
        raw_data_show = input()
        
        row_count = 0
        while raw_data_show in('yes','y','Yes','YEs','YES'):           
            #for i in range(row_count, row_count+5):
            print(df[row_count:row_count+5])
            row_count = row_count + 5
            print('Do you want 5 more rows Yes/No?')
            raw_data_show = input()
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
