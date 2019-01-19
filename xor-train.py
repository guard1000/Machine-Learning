from sklearn import svm, metrics
import pandas as pd

xor_input =[
    #P, Q, result
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

#입력을 학습 전용 데이터와 테스트 전용 데이터로 분류
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:,0:1] #data
xor_label = xor_df.ix[:,2] #label

#데이터 학습과 예측하기
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

#정답률 구하기
ac_score = metrics.accuracy_score(xor_label, pre)
print('정답률:', ac_score)


'''
#XOR 계산 결과 데이터
xor_data =[
    #P, Q, result
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

#학습을 위한 데이터와 레이블 분리
data =[]
label =[]
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    label.append(r)

#데이터 학습시키기
clf = svm.SVC()
clf.fit(data, label)

#데이터 예측하기
pre = clf.predict(data)
print('예측결과:', pre)

#결과확인
ok =0; total =0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer: ok+=1
    total += 1
print('정답률:', ok, "/", total, '=', ok/total)
'''