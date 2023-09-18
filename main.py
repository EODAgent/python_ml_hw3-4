import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import linregress

NYCTemperature = pd.read_csv('temperature.csv')
NYCTemperatureComp = pd.read_csv('temperature-comp.csv')
NYCTemperature.columns = ['Date', 'Temperature', 'Anomaly']
NYCTemperatureComp.columns = ['Date', 'Temperature', 'Anomaly']
NYCTemperature.Date = NYCTemperature.Date.floordiv(100)
temps_df = pd.DataFrame(NYCTemperature)
x_train = NYCTemperature['Date']
y_train = NYCTemperature['Temperature']
years_to_forecast = [2019, 2020, 2021, 2022, 2023]
early_years_to_forecast = [1890, 1891, 1892, 1893, 1894]

print(NYCTemperature.head())

print(' ')
print('******************************************')
print('2. Бібліотеку Seaborn використати для графічного')
print('представлення даних DataFrame у вигляді регресійної прямої, що')
print('представляє графік зміни обраних показників за період 1895-2018 років.')
print('******************************************')
print(' ')

sns.regplot(x=x_train, y=y_train, data=NYCTemperature)
slope, intercept, r_value, p_value, std_err = linregress(x_train, y_train)
r_squared = r_value ** 2
plt.annotate(f"R-squared = {round(r_squared, 2)}", xy=(0.05, 0.95), xycoords='axes fraction')
plt.show()


print(' ')
print('******************************************')
print('3. Спрогнозуйте дані на 2019, 2020, 2021 та 2022 рік.')
print('******************************************')
print(' ')
def temp_forecast(years_to_forecast, data_file):
    x_train = data_file['Date']
    y_train = data_file['Temperature']
    slope, intercept, r_value, p_value, std_err = linregress(x_train, y_train)

    forecasts = {}
    for year in years_to_forecast:
        forecasted_temperature = slope * year + intercept
        forecasts[year] = forecasted_temperature

    return pd.Series(forecasts)


forecasts = temp_forecast(years_to_forecast, NYCTemperature)
print(forecasts)

print(' ')
print('******************************************')
print('#4. Оцініть за формулою, якою могли б бути показники до 1895')
print('року. Наприклад, оцінка середньої температури за січень 1890 року')
print('може бути отримана наступним чином:')
print('******************************************')
print(' ')
pre_forecasts = temp_forecast(early_years_to_forecast, NYCTemperature)
print(pre_forecasts)

print(' ')
print('******************************************')
print('5. Скористайтесь функцією regplot бібліотеки Seaborn для')
print('виведення всіх точок даних; дати представляються на осі x, а')
print('показники на осі y. Функція regplot будує діаграму розкиду даних, на')
print('якій точки представляють показники за заданий рік, а пряма лінія -')
print('регресійну пряму.')
print('6. Виконайте маштабування осі у від (приклад від 10 до 70 градусів):')
print('******************************************')
print(' ')
axes = sns.regplot(x=x_train, y=y_train)
axes.set_ylim(10, 70)
plt.show()

print(' ')
print('******************************************')
print('7. Порівняйте отриманий прогноз для 2019, 2020, 2021 та за 2022 роки з даними на NOAA «Climate at a Glance»:')
print ('https://www.ncdc.noaa.gov/cag/ і зробити висновок. ')
print('******************************************')
print(' ')
forecasts = temp_forecast(years_to_forecast, NYCTemperature)
fact_temp = pd.Series(NYCTemperatureComp['Temperature'])
print(forecasts)
print(fact_temp)