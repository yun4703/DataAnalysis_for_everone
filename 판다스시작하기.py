import pandas
import matplotlib.pyplot as plt
from gapminder import gapminder
df = gapminder

#1 데이터 집합 불러오기

print(df.head()) #데이터 집합 살펴보기

print(type(df)) #데이터프레임 자료형 출력

print(df.shape) #데이터프레임 행열

print(df.columns) #데이터 프레임 열 조회

print(df.dtypes) #데이터프레임 구성하는 값 자료형 출력

print(df.info()) # 좀더 상세히

#2 데이터 추출하기

#열

country_df = df['country'] #열 단위 데이터 추출
print(type(country_df))
print(country_df.head())
print(country_df.tail())

subset = df[['country', 'continent', 'year']] #여러 열 출력, 형태는 데이터프레임
print(type(subset))
print(subset.head())
print(subset.tail())

#행, loc

print(df.loc[0]) # loc속성으로 행 데이터 추출하기, loc 은 인덱스 기준
print(df.loc[99]) # -1은 오류 발생, 인덱스가 아니기때문에

number_of_rows = df.shape[0] # 마지막 행 출력
last_row_index = number_of_rows -1
print(df.loc[last_row_index])
print(df.tail(n=1)) # 좀 더 효율적인 방법

print(df.loc[[0, 99, 999]]) # 특정 인덱스(0, 99, 999번째) 행 출력하기

subset_loc = df.loc[0]
subset_tail = df.tail(n=1)

print(type(subset_loc)) # 둘의 반환 자료형은 다르다 loc은 series , tail은 dataframe
print(type(subset_tail))

#행, iloc

print(df.iloc[1]) # iloc은 데이터 순서를 의미하는 행번호 사용
print(df.iloc[99])
print(df.iloc[-1]) # iloc은 -1 가능, 행이기때문에, 다만 존재하지 않는 행은 오류

print(df.iloc[[0, 99, 999]]) # 여러 데이터 출력하기

# 데이터 추출하기 - 슬라이싱 구문, range메서드

subset = df.loc[:, ['year','pop']] # df.loc[[행],[열]], df.iloc[[행],[열]] 방식 기억하기
print(subset.head())

subset = df.iloc[:, [2, 4, -1]]
print(subset.head())

small_range = list(range(5))
print(range)
print(type(small_range))
subset = df.iloc[:, small_range]
print(subset.head())

small_range = list(range(3, 6))
print(small_range)

subset = df.iloc[:, small_range]
print(subset)

small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset.head())

subset = df.iloc[:, :3] # range 보다는 슬라이싱이 낫지
print(subset.head())

subset = df.iloc[:, 0:6:2]
print(subset.head())

print(df.iloc[[0, 99, 999], [0, 3, 5]]) # 0,99,99번째 행 0,3,5번째 열 출력

print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']]) #iloc이 python기준 편해보이나 loc을 통한 직접지정이 좋다

print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']]) #응용하기

#3 기초 통계 계산

print(df.head(n=10))

print(df.groupby('year')['lifeExp'].mean()) #lifeExp열을 연도별로 그룹화하여 평균계산하기

grouped_year_df = df.groupby('year') #연도별로 그룹화한 country, continent, gdpPercap 열 데이터프레임
print(type(grouped_year_df))
print(grouped_year_df) #메모리주소 출력

grouped_year_df_lifeExp = grouped_year_df['lifeExp'] #연도별로 그룹화한 lifeExp 열 (시리즈) 출력
print(type(grouped_year_df_lifeExp))

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year) #연도별로 그룹화한 lifeExp 평균값

multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean() # year와 continent 그룹화한열 lifeExp, gdpPercap 열 평균 추출

print(df.groupby('continent')['country'].nunique()) #continent 기준 df 생성, country 열 추출 , 빈도수 계산

#그래프 그리기

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)
global_yearly_life_expectancy.plot()
plt.show()