import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many people of each race are represented in this dataset? 
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # What percentage of people with advanced education make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_high_earners = (advanced_education[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0]) * 100

    # What percentage of people without advanced education make more than 50K?
    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_high_earners_no_adv_edu = (no_advanced_education[no_advanced_education['salary'] == '>50K'].shape[0] / no_advanced_education.shape[0]) * 100

    # What is the minimum number of hours a person works per week?
    min_hours_per_week = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
    percentage_high_earners_min_hours = (min_hours_workers[min_hours_workers['salary'] == '>50K'].shape[0] / min_hours_workers.shape[0]) * 100
    # testing country money

    # test = df[df['salary'=='>50K']]['native-country'].value_counts().idxmax()
    testing = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True)
    all_in_country = df['native-country'].value_counts(normalize=True)
    high_earners_country = (testing / all_in_country * 100).idxmax()
    # print(high_earners_country)

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    # high_earners_country = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True).idxmax()
    percentage_high_earners_country = df[df['native-country'] == high_earners_country]['salary'].value_counts(normalize=True)['>50K'] * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_occupation_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Display the results
    # print("Number of people of each race:")
    # print(race_count)
    # print("\nAverage age of men:", average_age_men)
    # print("\nPercentage of people with a Bachelor's degree:", percentage_bachelors)
    # print("\nPercentage of high earners with advanced education:", percentage_high_earners)
    # print("\nPercentage of high earners without advanced education:", percentage_high_earners_no_adv_edu)
    # print("\nMinimum number of hours worked per week:", min_hours_per_week)
    # print("\nPercentage of high earners among minimum hours workers:", percentage_high_earners_min_hours)
    # print("\nCountry with the highest percentage of high earners and their percentage:", high_earners_country, percentage_high_earners_country)
    # print("\nMost popular occupation for high earners in India:", top_occupation_india)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = round(race_count)

    # What is the average age of men?
    average_age_men = round(average_age_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(percentage_bachelors,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = round(percentage_high_earners,1)
    lower_education_rich = round(percentage_high_earners_no_adv_edu,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min_hours_per_week

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = round(percentage_high_earners_min_hours,1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = high_earners_country
    highest_earning_country_percentage = round(percentage_high_earners_country,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = top_occupation_india

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
