import csv
import math
import pandas as pd
import streamlit as st

def findMax(port):
    with open('titanic.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        max = 0
        for row in reader:
            if (str(row[11]) == port):
                if (float(max) < float(row[9])):
                    max = row[9]
        return max
def findMin(port):
    with open('titanic.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        min = 0
        for row in reader:
            if (str(row[11]) == port):
                if (float(min) > float(row[9])):
                    min = row[9]
        return min
def findAverage(port):
    with open('titanic.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        s = 0
        iterC = 0
        for row in reader:
            if str(row[11]) == port:
                s += float(row[9])
                iterC += 1
        average = s/iterC
        return math.ceil(average)

def countKids(port,age):
    with open('titanic.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        count = 0
        for row in reader:
            if str(row[11]) == port and row[5].isdigit():
                if int(row[5]) <= age:
                    count += 1
        return count

def aliveWomans(classobs, min, max):
    with open('titanic.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        count = 0
        for row in reader:
            if str(row[2]) == classobs and float(row[9]) > float(min) and float(max) > float(row[9]):
                count += 1
        return count

def suinPart():
    st.image('tit_image.webp')
    st.title('Данные пасажиров Титаника')
    st.write("Для выбора средней, максимальной или минимальной стоимости билета по портам нажмите ниже")
    selected_sex = st.selectbox("Выберите тип", ('Минимальный','Максимальный','Средний'))
    st.write(f'Selected option: {selected_sex!r}')
    qMax = findMax('Q')
    if selected_sex == "Максимальный":
        arr = {'Максимальное': {'Q': findMax("Q"), 'S': findMax('S'), 'C': findMax('C')}}
    if selected_sex == "Минимальный":
        arr = {'Минимальное':{'Q':findMin('Q'),'S':findMin('S'),'C':findMin('C')}}
    if selected_sex == "Средний":
        arr ={'Среднее':{'Q':findAverage('Q'),'S':findAverage('S'),'C':findAverage('C')}}
    #arr = {'max':{'Q':findMax("Q"),'S':findMax('S'),'C':findMax('C')},'min':{'Q':findMin('Q'),'S':findMax('S'),'C':findMin('C')},'average':{'Q':findAverage('Q'),'S':findAverage('S'),'C':findAverage('C')}}
    new_df = pd.DataFrame.from_dict(arr)
    st.table(new_df)

#Подсчитать количество погибших детей по каждому пункту посадки, указав максимальный возраст (число от 1 до 18).
def peplerPart():
    st.image('tit_image.webp')
    st.title('Данные пасажиров Титаника')
    selectedAge = st.text_input("Укажите максимальный возраст")
    if len(selectedAge) <=0:
        st.write("Вы не ввели число или ввели его неверно!")
    else:
        selectedAge = int(selectedAge)
        if int(selectedAge) > 0 and selectedAge < 19:
            arr = {'Q': [countKids("Q",selectedAge)],'S':[countKids("S",selectedAge)],
                   'C':[countKids("C",selectedAge)]}
            new_df = pd.DataFrame.from_dict(arr)
            st.table(new_df)
        else:
            st.write("Число не может быть меньше 1 и больше 18!")


#Подсчитать количество выживших женщин по каждому классу обслуживания, указав диапазон платы за проезд (от … и до …).
def vladPart():
    st.image('tit_image.webp')
    st.title('Данные пасажиров Титаника')
    minCost = st.text_input("Введите минимальное число")
    maxCost = st.text_input("Введите максимальное число")
    if len(minCost) <= 0 and len(maxCost) <= 0:
        st.write("Вы не ввели число или ввели его неверно!")
    else:
        minCost = int(minCost)
        maxCost = int(maxCost)
        if maxCost < 0 or minCost > maxCost:
            st.write("Число не может быть меньше 1 и больше 18!")
        else:
            arr = {'1': [aliveWomans("1", minCost, maxCost)], '2': [aliveWomans("2", minCost, maxCost)],
                   '3': [aliveWomans("3", minCost, maxCost)]}
            new_df = pd.DataFrame.from_dict(arr)
            st.table(new_df)

chose_member = st.selectbox("Выберите задание", ('Алексей С.','Алексей П.','Владислав'))
if chose_member == "Алексей С.":
    suinPart()
if chose_member == "Алексей П.":
    peplerPart()
if chose_member == "Владислав":
    vladPart()