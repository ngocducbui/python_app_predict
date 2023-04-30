import pathlib
import xlsxwriter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, \
    ConfusionMatrixDisplay, mean_absolute_error, mean_squared_error, mean_squared_error, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn.metrics import r2_score


def percentage_of_student_target(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    student_target = data['Target'].value_counts()
    plt.pie(student_target, labels=student_target.index, autopct='%1.1f%%')
    plt.title('Percentage of Student Target')
    if type == 'export':
        plt.savefig('graph1')
    else:
        plt.show()


def number_of_student_target_by_genders(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    sns.countplot(data=data, x='Gender', hue='Target', hue_order=['Dropout', 'Enrolled', 'Graduate'])
    plt.xticks(ticks=[0, 1], labels=['Female', 'Male'])
    plt.ylabel('Number of Students')
    if type == 'export':
        plt.savefig('graph2')
    else:
        plt.show()


def number_of_student_target_by_arital_status(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    plt.figure(figsize=(9, 4))
    sns.countplot(data=data, x='Marital status', hue='Target', hue_order=['Dropout', 'Enrolled', 'Graduate'])
    plt.xticks(ticks=[0, 1, 2, 3, 4, 5],
               labels=['Single', 'Married', 'Widower', 'Divorced', 'Facto Union', 'Legally Seperated'])
    plt.xlabel('Marital Status')
    plt.ylabel('Number of Students')
    if type == 'export':
        plt.savefig('graph3')
    else:
        plt.show()


def number_of_student_enrolled_by_ages(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    sns.displot(data=data, x='Age at enrollment', kde=True)
    data['Age at enrollment'].describe()
    plt.xlabel('Age at Enrolment')
    plt.ylabel('Number of Students')
    if type == 'export':
        plt.savefig('graph4')
    else:
        plt.show()


def dropout_percentage_by_ges(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])

    # lấy những bản ghi có giá trị "Dropout" trong cột "Target"
    # nhóm chúng theo từng độ tuổi bằng hàm "groupby" và đếm số lượng bản ghi -> lưu vào list: `dropout_by_age`
    dropout_by_age = data.loc[data.Target == 'Dropout'].groupby('Age at enrollment').Target.agg(['count']).to_dict()
    # nhóm các bản ghi theo từng độ tuổi và đếm số lượng bản ghi -> `total_by_age`
    total_by_age = data.groupby('Age at enrollment').Target.agg(['count']).to_dict()

    # Kiểm tra độ tuổi nào không có trong dictionary "dropout_by_age",
    # nếu không có thì thêm độ tuổi đó vào với giá trị bằng 0.
    for age in list(total_by_age['count'].keys()):
        if age not in list(dropout_by_age['count'].keys()):
            dropout_by_age['count'][age] = 0

    # Sắp xếp dictionary "dropout_by_age" theo độ tuổi và lưu trữ kết quả vào dictionary temp
    temp = list(dropout_by_age['count'].keys())
    temp.sort()
    temp = {key: dropout_by_age['count'][key] for key in temp}
    # Tính tỷ lệ bỏ học theo độ tuổi
    # bằng cách lấy số lượng bỏ học ở từng độ tuổi trong dictionary "temp" chia cho tổng số lượng ở từng độ tuổi
    # trong dictionary "total_by_age" và nhân với 100.
    # Kết quả được lưu trữ trong list "dropout_rate_by_age".
    dropout_rate_by_age = [list(temp.values())[i] / list(total_by_age['count'].values())[i] * 100 for i in
                           range(len(list(total_by_age['count'].keys())))]

    fig, ax = plt.subplots()
    # Vẽ biểu đồ cột thể hiện kết quả với trục x là độ tuổi và trục y là tỷ lệ bỏ học được tính toán ở bước trước.
    ax.bar(list(total_by_age['count'].keys()), dropout_rate_by_age)
    ax.set(title="Age Dropout", xlabel="Age", ylabel="Percen")
    if type == 'export':
        plt.savefig('graph5')
    else:
        plt.show()


def number_of_student_with_educational_special_needs(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    sns.countplot(data=data, x='Educational special needs', hue='Target', hue_order=['Dropout', 'Enrolled', 'Graduate'])

    plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
    plt.xlabel('Educational Special Needs')
    plt.ylabel('Number of Students')
    if type == 'export':
        plt.savefig('graph6')
    else:
        plt.show()


def statistics_comparison_in_number_of_studen_target_by_debt(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    sns.countplot(data=data, x="Debtor", hue='Target', hue_order=['Dropout', 'Enrolled', 'Graduate'])

    plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
    plt.xlabel('Debtor')
    plt.ylabel('Number of Students')
    if type == 'export':
        plt.savefig('graph7')
    else:
        plt.show()


def rate_of_unemployment_student(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    X = student_data.drop(columns=['Target'], axis=1)
    Y = student_data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    clf = RandomForestClassifier(max_depth=10, random_state=0)
    clf.fit(X_train, y_train)

    sns.displot(data=data, x="Unemployment rate", kde=True)
    data['Unemployment rate'].describe()

    plt.xlabel('Unemployment Rate')
    plt.ylabel('Number of Students')
    if type == 'export':
        plt.savefig('graph8')
    else:
        plt.show()


def correlation_heatmap_between_variables(path, type):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    plt.figure(figsize=(15, 10))
    sns.heatmap(data.corr(), cmap='coolwarm')
    plt.title('Correlation Heatmap between Variables')
    if type == 'export':
        plt.savefig('graph9')
    else:
        plt.show()


def shape(path, extension):
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    return str(data.shape)


def corr_col(path, list_col):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    list_reuslt = []
    for i in list_col:
        result = student_data[i].corr(student_data['Target'])
        list_reuslt.append(result)
    plt.bar(list_col, list_reuslt)
    plt.xlabel("Columns")
    plt.ylabel("Correlation with the target column")
    plt.title("The table shows the correlation of the columns")
    plt.show()


def random_forest(path, data_test, max_depth, number):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    data = data.drop(['International', 'Nacionality'], axis=1)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    X = student_data.drop(columns=['Target'], axis=1)
    Y = student_data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=number)
    clf = RandomForestClassifier(max_depth=max_depth, random_state=0)
    clf.fit(X_train, y_train)
    if data_test == ' ':
        y_pred = clf.predict(X_test)
        rs = f1_score(y_test, y_pred, average='macro')
        return rs

    elif data_test == 'error':
        y_pred = clf.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        score = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return mae, mse, rmse, score, report
    elif data_test == 'matrix':
        y_pred = clf.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        TN, FP, FN, TP = cm.ravel()
        print("TN={0}, FP={1}, FN={2}, TP={3}".format(TN, FP, FN, TP))
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.show()
    else:
        rs = clf.predict([data_test])
        return rs


def liner(path, data_test, number):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    data = data.drop(['International', 'Nacionality'], axis=1)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    X = student_data.drop(columns=['Target'], axis=1)
    Y = student_data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=number)
    clf = linear_model.LinearRegression()
    clf.fit(X_train, y_train)
    if data_test == ' ':
        y_pred = clf.predict(X_test)
        rs = r2_score(y_test, y_pred)
        return rs
    elif data_test == 'error':
        y_pred = clf.predict(X_test)
        coef = clf.coef_
        intercept = clf.intercept_
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = mse ** 0.5
        r2 = r2_score(y_test, y_pred)
        return coef, intercept, mae, mse, rmse, r2
    else:
        rs = clf.predict([data_test])
        return rs


def logic_regression(path, data_test, number):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    data = data.drop(['International', 'Nacionality'], axis=1)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    X = student_data.drop(columns=['Target'], axis=1)
    Y = student_data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=number)
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    if data_test == ' ':
        y_pred = clf.predict(X_test)
        rs = f1_score(y_test, y_pred, average='macro')
        return rs
    elif data_test == 'error':
        y_pred = clf.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        score = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return mae, mse, rmse, score, report
    elif data_test == 'matrix':
        y_pred = clf.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        TN, FP, FN, TP = cm.ravel()
        print("TN={0}, FP={1}, FN={2}, TP={3}".format(TN, FP, FN, TP))
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.show()
    else:
        rs = clf.predict([data_test])
        return rs


# test=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1.0,1]
# a=['1', '8', '5', '2', '1', '1', '13', '10', '6', '10', '1', '0', '0', '1', '1', '0', '20', '0', '0', '0', '0', '0.0', '0', '0', '0', '0', '0', '0.0', '0', '10.8', '1.4', '1.74']
# print(logic_regression('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv', test,0.1))


def decision_tree(path, data_test, number,max_depth):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    data = data.drop(['International', 'Nacionality'], axis=1)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    X = student_data.drop(columns=['Target'], axis=1)
    Y = student_data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=number)
    clf = DecisionTreeClassifier(max_depth=max_depth)
    clf.fit(X_train, y_train)
    if data_test == ' ':
        y_pred = clf.predict(X_test)
        rs = f1_score(y_test, y_pred, average='macro')
        return rs
    elif data_test == 'error':
        y_pred = clf.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        score = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return mae, mse, rmse, score, report
    elif data_test == 'matrix':
        y_pred = clf.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        TN, FP, FN, TP = cm.ravel()
        print("TN={0}, FP={1}, FN={2}, TP={3}".format(TN, FP, FN, TP))
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.show()
    else:
        rs = clf.predict([data_test])
        return rs


def knn(path, data_test, number, n_neigh):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    data = data.drop(['International', 'Nacionality'], axis=1)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    X = student_data.drop(columns=['Target'], axis=1)
    Y = student_data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=number)
    clf = KNeighborsClassifier(n_neighbors=n_neigh)
    clf.fit(X_train, y_train)
    if data_test == ' ':
        y_pred = clf.predict(X_test)
        rs = f1_score(y_test, y_pred, average='macro')
        return rs

    elif data_test == 'error':
        y_pred = clf.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        score = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return mae, mse, rmse, score, report
    elif data_test == 'matrix':
        y_pred = clf.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        TN, FP, FN, TP = cm.ravel()
        print("TN={0}, FP={1}, FN={2}, TP={3}".format(TN, FP, FN, TP))
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.show()
    else:
        rs = clf.predict([data_test])
        return rs


# a=[1.0, 8.0, 5.0, 2.0, 1.0, 1.0, 13.0, 10.0, 6.0, 10.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 20.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.8, 1.4, 1.74]
# test=[1, 1, 1.0, 1, 1, 1.2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1.0,1]
# # a=['1', '8', '5', '2', '1', '1', '13', '10', '6', '10', '1', '0', '0', '1', '1', '0', '20', '0', '0', '0', '0', '0.0', '0', '0', '0', '0', '0', '0.0', '0', '10.8', '1.4', '1.74']
def size_split(path, size):
    extension = pathlib.Path(path).suffix
    if extension == '.csv':
        data = pd.read_csv(path)
    else:
        data = pd.read_excel(path)
    data = data.drop(['International', 'Nacionality'], axis=1)
    student_data = data.drop(data[data['Target'] == 'Enrolled'].index)
    encoder = LabelEncoder()
    student_data['Target'] = encoder.fit_transform(student_data['Target'])
    X = student_data.drop(columns=['Target'], axis=1)
    Y = student_data['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=size)
    return X_train.shape, X_test.shape
# a=size_split('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv',0.1)
# print(a,type(a))
# test=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1]
# print(type(size_split('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv',0.1)))
# print(random_forest('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv',' '))
# print(liner('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv',' '))
# print(logic_regression('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv',' '))
# print(decision_tree('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv', ' '))
# print(knn('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv',' '))
# C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv
# a=random_forest('C:/Users/ADMIN/Downloads/Study/FPT Software/Project/final/Dataset/student.csv',test)
# print(a)
