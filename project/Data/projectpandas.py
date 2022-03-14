import pandas as pd

# 엑셀 불러와서 데이터프레임으로 만들기
df1 = pd.read_excel("project_program.xlsx",sheet_name="program", skiprows = 0)
df2 = pd.read_excel("project_place.xlsx",sheet_name="place", skiprows = 0)

# 원하는 열을 index로 설정
# df1.set_index('ProgramName', inplace=True, drop=False)
# df2.set_index('PlaceName', inplace=True, drop=False)

# # 원하는 행 추출
# print(df1[df1.index=='뮤지컬 앨리스 스튜디오'])
#
# # 칼럼명만 보여줌
# print(df1.columns)
#
# ### 열만 가져와서 함수 적용
# # 중복제거 데이터 추출
# print(df1['PlaceName'].unique())
# # 중복제거 데이터 개수 출력
# print(df1['PlaceName'].nunique())
#
# # 칼럼 선택 추출; 여러개 추출 가능(대괄호 두 개 사용)
# print(df1['PlaceName'])
# print(df1[['PlaceName', 'Category']])
#
# # 열 이름 안쓰고도 칼럼 선택 추출 가능
# print(df1.columns) # 열 이름 목록
# print(df1.columns[3]) # 4번째 열의 이름
# print(df1[df1.columns[3]]) # print(df1['PlaceName'])과 같음
#
# # 슬라이싱
# print(df1['PlaceName'][0:5])
# print(df1[['ProgramName', 'PlaceName']][:3])

### 데이터 선택 (loc; location) ###
# # 이름을 이용하여 원하는 row에서 원하는 col을 선택
# print(df.loc[1])
# # index 1에 해당하는 전체 데이터
# print(df.loc[1, 'PlaceName'])
# # 1에 해당하는 데이터 중 PlaceName 데이터 추출
# print(df.loc[[1, 2], 'PlaceName'])
# print(df.loc[[1, 2], ['PlaceName', 'ProgramName']])
# print(df.loc[1:4, 'Category':'PlaceName'])
# # 슬라이싱을 이용해서 추출가능; 다른 슬라이싱과 다르게 양끝을 포함한다


### 데이터 선택 (iloc; integer location)
# 정수 위치를 이용해서 원하는 row에서 원하는 col 선택
# 1번째 row(행)의 데이터
# print(df1.iloc[0])
# 1번째 행의 2번째 열의 값
# print(df1.iloc[0, 1])
# 1,2 번째 행의 3~5번째 열의 값
# print(df1.iloc[[0,1], 2:5])
# 1,2 번째 행의 3,5번째 열의 값
# print(df1.iloc[[0,1], [2,4]])

### 데이터 선택 (조건) ###
# print(df1['ProgramNumber'] >= 50)
# filt = df1['ProgramNumber'] >= 50
# print(df1[filt])
# # PlaceName이 세종문화회관 데이터 중에서 장소랑 프로그램 이름 추출
# filt2 = df1['PlaceName']=='세종문화회관'
# print(df1[filt2][['PlaceName', 'ProgramName']])
# # 필터를 역으로 적용해서 세종문화회관 아닌 데이터중에서 장소랑 프로그램 이름 추출
# print(df1[~filt2][['PlaceName', 'ProgramName']])

# #df.loc[row조건, col조건]
# print(df1.loc[df1['PlaceName']=='세종문화회관', ['PlaceName', 'ProgramName', 'Category']])
# # & |
# print(df1.loc[(df1['PlaceName']=='세종문화회관') & (df1['Category']=='독주/독창회'), ['PlaceName', 'ProgramName']])

### str 함수 ###
# # 세 로 시작하는 데이터 추출
# filt = df1['PlaceName'].str.startswith('세')
# print(df1[filt])
# # 관 으로 끝나는 데이터 추출
# filt = df1['PlaceName'].str.endswith('관')
# print(df1[filt])
# # 가 를 포함하는 데이터
# .str.contains('가')
# # 세종문화회관이거나 예술의 전당인 데이터 추출
# name = ["세종문화회관", "예술의 전당"]
# df1['PlaceName'].isin(name)
# 소문자로 바꾸기
# .str.lower()
# 소문자로 바꾼 name이 있는지 확인
# df1[].str.lower().isin(name)
# na를 True나 False로 처리를 해야 contain을 사용할 수 있다.
# .str.contains('가', na=false)













