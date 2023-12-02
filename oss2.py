import pandas as pd


df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

year_2015 = df[df['year'] == 2015]
year_2016 = df[df['year'] == 2016]
year_2017 = df[df['year'] == 2017]
year_2018 = df[df['year'] == 2018]

#2-1.1번

#2015년
print('---------------------------------------------------------------------------------------------')
print('2015 Top 10 player in hits')
H_top_2015 = year_2015.nlargest(10, 'H')
print(H_top_2015)

print('2015 Top 10 player in average')
AVG_top_2015 = year_2015.nlargest(10, 'avg')
print(AVG_top_2015)

print('2015 Top 10 player in homeruns')
HR_top_2015 = year_2015.nlargest(10, 'HR')
print(HR_top_2015)

print('2015 Top 10 player in OBP')
OBP_top_2015 = year_2015.nlargest(10, 'OBP')
print(OBP_top_2015)
print('---------------------------------------------------------------------------------------------')


#2016년
print('---------------------------------------------------------------------------------------------')
print('2016 Top 10 player in hits')
H_top_2016 = year_2016.nlargest(10, 'H')
print(H_top_2016)

print('2016 Top 10 player in average')
AVG_top_2016 = year_2016.nlargest(10, 'avg')
print(AVG_top_2016)

print('2016 Top 10 player in homeruns')
HR_top_2016 = year_2016.nlargest(10, 'HR')
print(HR_top_2016)

print('2016 Top 10 player in OBP')
OBP_top_2016 = year_2016.nlargest(10, 'OBP')
print(OBP_top_2016)
print('---------------------------------------------------------------------------------------------')


#2017년
print('---------------------------------------------------------------------------------------------')
print('2017 Top 10 player in hits')
H_top_2017 = year_2017.nlargest(10, 'H')
print(H_top_2017)

print('2017 Top 10 player in average')
AVG_top_2017 = year_2017.nlargest(10, 'avg')
print(AVG_top_2017)

print('2017 Top 10 player in homeruns')
HR_top_2017 = year_2017.nlargest(10, 'HR')
print(HR_top_2017)

print('2017 Top 10 player in OBP')
OBP_top_2017 = year_2017.nlargest(10, 'OBP')
print(OBP_top_2017)
print('---------------------------------------------------------------------------------------------')


#2018년
print('---------------------------------------------------------------------------------------------')
print('2018 Top 10 player in hits')
H_top_2018 = year_2018.nlargest(10, 'H')
print(H_top_2018)

print('2018 Top 10 player in average')
AVG_top_2018 = year_2018.nlargest(10, 'avg')
print(AVG_top_2018)

print('2018 Top 10 player in homeruns')
HR_top_2018 = year_2018.nlargest(10, 'HR')
print(HR_top_2018)

print('2018 Top 10 player in OBP')
OBP_top_2018 = year_2018.nlargest(10, 'OBP')
print(OBP_top_2018)
print('---------------------------------------------------------------------------------------------')

#2-1.2번
print('---------------------------------------------------------------------------------------------')
catcher = year_2018[year_2018['cp'] == '포수']
war_top_c = catcher.nlargest(1, 'war')
print("2018 Top war in Catcher")
print(war_top_c)

base1 = year_2018[year_2018['cp'] == '1루수']
war_top_b1 = base1.nlargest(1, 'war')
print("2018 Top war in 1base")
print(war_top_b1)

base2 = year_2018[year_2018['cp'] == '2루수']
war_top_b2 = base2.nlargest(1, 'war')
print("2018 Top war in 2base")
print(war_top_b2)

base3 = year_2018[year_2018['cp'] == '3루수']
war_top_b3 = base3.nlargest(1, 'war')
print("2018 Top war in 3base")
print(war_top_b3)

ss = year_2018[year_2018['cp'] == '유격수']
war_top_ss = ss.nlargest(1, 'war')
print("2018 Top war in ss")
print(war_top_ss)

lf = year_2018[year_2018['cp'] == '좌익수']
war_top_lf = lf.nlargest(1, 'war')
print("2018 Top war in Left fly")
print(war_top_lf)

cf = year_2018[year_2018['cp'] == '중견수']
war_top_cf = cf.nlargest(1, 'war')
print("2018 Top war in Center fly")
print(war_top_cf)

rf = year_2018[year_2018['cp'] == '우익수']
war_top_rf = rf.nlargest(1, 'war')
print("2018 Top war in Right fly")
print(war_top_rf)
print('---------------------------------------------------------------------------------------------')

#2-1.3번
print('---------------------------------------------------------------------------------------------')
data_set = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG', 'salary']
data = df[data_set]
correlation = data.corr()
salary_correlation = correlation['salary']
max_corr = salary_correlation.drop('salary').idxmax()
print(f"One of the data with the highest correlation with 'salary' is: {max_corr}")
print('---------------------------------------------------------------------------------------------')