import pandas as pd
s = pd.Series(['banana', 42]) #시리즈 만들기
print(s)

s = pd.Series(['Wes Mc Kinney', 'Creator of Pandas']) #시리즈를 생성할때 문자열을 인덱스로 지정 가능
print(s)
s = pd.Series(['Wes Mc Kinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

scientists = pd.DataFrame({
    'Name' : ['Rosaline Fanklin', 'William gosset'],
    'Occupation' : ['Chemist', 'Statistician' ],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Died' : ['1958-04-16', '1937-10-16'],
    'Age' : [37,61]}
)

print(scientists) #데이터프레임 생성


scientists = pd.DataFrame(
    data = {'Occupation' : ['Chemist', 'Statistician' ],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Died' : ['1958-04-16', '1937-10-16'],
    'Age' : [37,61]},
    index = ['Rosaline Fanklin', 'William gosset'],
    columns =  ['Occupation', 'Born', 'Age', 'Died' ]
)

print(scientists) #index, column 직접설정하기

from collections import OrderedDict

scientists = pd.DataFrame(OrderedDict([
    ('Name', ['Rosaline Fanklin', 'William gosset']),
    ('Occupation', ['Chemist', 'Statistician']),
    ('Born', ['1920-07-25', '1876-06-13']),
    ('Died', ['1958-04-16', '1937-10-16']),
    ('Age', [37, 61])
])
)
print(scientists) #데이터 순서를 정하고 싶으면 OrderedDict 사용

scientists = pd.DataFrame(
    data = {'Occupation' : ['Chemist', 'Statistician' ],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Died' : ['1958-04-16', '1937-10-16'],
    'Age' : [37,61]},
    index = ['Rosaline Fanklin', 'William gosset'],
    columns =  ['Occupation', 'Born', 'Age', 'Died' ]
)

first_row = scientists.loc['William gosset']
print(type(first_row))
print(first_row) #시리즈 출력하기

print(first_row.index) #시리즈의 인덱스 출력
print(first_row.values) #시리즈의 데이터 출력

print(first_row.index[0]) #인덱스 첫번째 추출
print(first_row.keys()[0]) #keys를 이용한 동일한 출력

ages = scientists['Age']
print(ages) # Age 열 출력
# mean, max, min, std 매서드 사용하기
print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())

#시리즈 다루기 - 응용

scientists = pd.read_csv('C:/Users/yun47/Downloads/scientists.csv')
ages = scientists['Age']
print(ages.max())

print(ages.mean())

print(ages[ages > ages.mean()]) #평균보다 나이많은 사람 데이터 출력하기

print(ages > ages.mean()) # 조건에 따른 True False 출력

print(type(ages > ages.mean()))

manual_bool_values = [True, True, False, False, True, True, False, True]
print(ages[manual_bool_values])

#시리즈와 브로드캐스팅

print(ages+ages)
print(ages*ages)
print(ages+100)
print(ages*2)

print(pd.Series([1,100]))
print(ages+pd.Series([1,100])) #길이가 다른 시리즈 더하기 , 해당 부분만 계산

rev_ages = ages.sort_index(ascending=False)
print(rev_ages) #인덱스 역순으로 출력하기

print(ages*2)
print(ages+rev_ages) #벡터 계산은 인덱스에 맞춰서함


print(scientists[scientists['Age'] > scientists['Age'].mean()]) # 불린추출하기

#print(scientists.loc[[True, True, False, True]]) # bool 벡터길이만큼만 계산

print(scientists*2) #브로드캐스팅하기

#시리즈와 데이터프레임의 데이터 처리하기

print(scientists['Born'].dtype)
print(scientists['Died'].dtype)

born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)

died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(died_datetime)

scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print(scientists.head())

print(scientists.shape)

scientists['ages_day_dy'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists)

print(scientists['Age'])

import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age']) #시리즈, 데이터프레임 데이터 섞기

print(scientists.columns)
scientists_dropped = scientists.drop(['Age'], axis=1)
print(scientists_dropped.columns) #데이터프레임 열 삭제하기

## 데이터 저장 불러오기

names = scientists['Name']
names.to_pickle('../scientists_names_series.pickle') #피클로 저장하기
scientists.to_pickle('../scientists_df.pickle')
scientists_names_from_pickle = pd.read_pickle('../scientists_names_series.pickle')
print(scientists_names_from_pickle)

scientists_from_pickle = pd.read_pickle('../scientists_df.pickle')
print(scientists_from_pickle)

names.to_csv('../scientists_names_series.csv') #csv tsv로 저장하기
scientists.to_csv('../scientists_df.tsv', sep='\t')
