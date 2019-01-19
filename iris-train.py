from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

#붗꽃 csv 데이터 읽기
csv = pd.read_csv('iris.csv')

#필요한 열 추출하기
csv_data = csv[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
csv_label = csv['Name']

#학습전용 데이터와 테스트 전용 데이터로 나누기
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)

#데이터 학습시키고 예측
clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

#정답률 구하기
ac_score = metrics.accuracy_score(test_label, pre)
print('정답률:', ac_score)


'''
#csv 파일 100개로 학습, 50개로 테스트
from sklearn import svm, metrics
import random, re

#붗꽃의 CSV 데이터 읽기
csv =[]
with open('iris.csv', 'r', encoding='utf-8') as fp:
    #한줄씩 읽자
    for line in fp:
        line = line.strip() #줄바꿈 제거
        cols = line.split(',')
        #문자열 데이터를 숫자로 변환
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

#가장 앞 줄의 헤더 제거
del csv[0]

# 데이터 셔플
random.shuffle(csv)

#학습 전용 데이터와 테스트 전용 데이터 분할
total_len = len(csv)
train_len = int(total_len*2/3)
train_data=[]
train_label=[]
test_data=[]
test_label=[]

for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

#데이터를 학습시키고 예측한다.
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

#정답률 구하기
ac_score = metrics.accuracy_score(test_label, pre)
print('정답률 =', ac_score)
'''