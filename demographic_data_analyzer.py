import pandas as pd

# Load dataset
# df = pd.read_csv("your_data.csv")  # replace with your file path

# Here is a sample of what the data looks like:

#|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
#|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
#|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
#|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
#|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
#|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
#|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |


# 1. How many people of each race are represented in this dataset?
race_count = df['race'].value_counts()
print("Number of people of each race:\n", race_count)

# 2. What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print("\nAverage age of men:", round(average_age_men, 1))

# 3. What is the percentage of people who have a Bachelor's degree?
total_people = len(df)
bachelors_count = len(df[df['education'] == 'Bachelors'])
percentage_bachelors = (bachelors_count / total_people) * 100
print("\nPercentage with Bachelor's degrees:", round(percentage_bachelors, 1))

# 4. What percentage of people with advanced education make more than 50K?
advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
adv_edu_df = df[df['education'].isin(advanced_edu)]
high_income_adv = len(adv_edu_df[adv_edu_df['salary'] == '>50K'])
percentage_high_income_adv = (high_income_adv / len(adv_edu_df)) * 100
print("\nPercentage with advanced education earning >50K:", round(percentage_high_income_adv, 1))

# 5. What percentage of people without advanced education make more than 50K?
non_adv_edu_df = df[~df['education'].isin(advanced_edu)]
high_income_non_adv = len(non_adv_edu_df[non_adv_edu_df['salary'] == '>50K'])
percentage_high_income_non_adv = (high_income_non_adv / len(non_adv_edu_df)) * 100
print("\nPercentage without advanced education earning >50K:", round(percentage_high_income_non_adv, 1))

# 6. What is the minimum number of hours a person works per week?
min_hours = df['hours-per-week'].min()
print("\nMinimum hours per week:", min_hours)

# 7. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
min_workers = df[df['hours-per-week'] == min_hours]
rich_min_workers = len(min_workers[min_workers['salary'] == '>50K'])
percentage_rich_min_workers = (rich_min_workers / len(min_workers)) * 100
print("\nPercentage of rich among those who work minimum hours:", round(percentage_rich_min_workers, 1))

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
country_groups = df.groupby('native-country')
rich_percent_by_country = (country_groups.apply(lambda x: (x['salary'] == '>50K').sum() / len(x)) * 100)
highest_country = rich_percent_by_country.idxmax()
highest_percentage = rich_percent_by_country.max()
print("\nCountry with highest percentage of rich:", highest_country)
print("Highest percentage of rich:", round(highest_percentage, 1))

# 9. Identify the most popular occupation for those who earn >50K in India.
rich_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_common_occupation_india = rich_india['occupation'].value_counts().idxmax()
print("\nMost popular occupation for rich in India:", most_common_occupation_india)
