#！ /usr/local/bin/python3
import re
import streamlit as st
import pandas as pd

class RecordData:
    def __init__(self,text):
        self.text = text
        self.error_text = ''
        self.text_type = '1'
        self.sheet_name = '澳门'
        self.sheet = 0
        self.animals = ["兔", "虎", "牛", "鼠", "猪", "狗", "鸡", "猴", "羊", "马", "蛇", "龙"]
        self.result_a = [[] for _ in range(49)]
        self.result_b = [[] for _ in range(49)]
        self.result = [self.result_a,self.result_b]
    def animal_index(self,input_animal):    #将生肖转换成对应的号码
        numbers = list(range(1, 50))
        start_index = self.animals.index("兔")
        numbers = numbers[start_index:] + numbers[:start_index]
        for animal in input_animal:  
                animal_index = self.animals.index(animal)
                result = [numbers[i] for i in range(animal_index, len(numbers), 12)]
        return result
       
    def get_number(self, text):             # 获取数字和金额
        amount = 0
        rows = re.findall(r'\d+', text)
        rows = [int(row) for row in rows]
        amount = rows[-1]
        rows.pop()
        return rows, amount

    def get_animals(self, text):           # 获取生肖和金额
        key_words = self.animals
        animals = []
        for keyword in key_words:
            if keyword in text:
                animals.append(keyword)
        amounts = re.findall(r"\d+", text)
        amount = amounts[-1]
        return animals, amount

    def get_tail(self,text):             #获取尾数
        amounts = re.findall(r'\d+', text)
        amount = amounts[-1]
        pos = text.find('尾')
        if pos != -1:
            text = text[:pos]
        digits = re.findall(r'\d+',text)
        rows = []
        for digit in digits:
            rows += [int(i) for i in range(1, 50) if str(i)[-1] in digit[::-1]] 
        return rows, amount

    def get_head(self,text):                  #获取头数
        amounts = re.findall(r'\d+', text)
        amount = amounts[-1]
        pos = text.find('头')
        if pos != -1:
            text = text[:pos]
        digits = re.findall(r'\d+',text)
        rows = []
        for digit in digits:
            rows += [int(i) for i in [str(s).zfill(2) for s in range(1, 50)] if str(i)[0] in digit[::-1]]
        return rows, amount   

    def record(self, rows, amount):         # 写入数据到excel
        if len(rows) == 0:
            return "没有行数，无法录入！"
        for i in rows:
            if int(i) >= 50:
                return f'大于50行，无法录入！' 
        if int(amount) == 0:
            return f"金额为0，无法录入！"
        rows = [int(row) for row in rows]
        rows = [x for x in rows if x != 0]
        for row in rows:
            self.result [int(self.sheet)][row-1].append(amount)
        return "录入成功"
    
    def type_select (self):                #识别文本类型
        self.text_type = '1'             
        type2_str = self.animals 
        type3_str = ['包','肖']
        type4_str = ['红','蓝','绿']
        type5_str = ['大','小']
        type6_str = ['尾']
        type7_str = ['头']
        for x in type2_str:
            if x in self.text:
                self.text_type = '2'
                for x in type3_str:
                    if x in self.text:
                        self.text_type = '3'        
        for x in type4_str:
            if x in self.text:
                self.text_type = '4'
        for x in type5_str:
            if x in self.text:
                self.text_type = '5'
        for x in type6_str:
            if x in self.text:
                self.text_type = '6'
        for x in type7_str:
            if x in self.text:
                self.text_type = '7'   

    def sheet_select(self):                #选择sheet
        self.sheet = 0
        name2_str = ['香','港']
        for s in name2_str: 
            if s in self.text:
                self.sheet = 1

    def type_input(self):                 #按类型获取位置和金额并写入到excel
        if self.sheet == 1:
            self.sheet_name = '澳门'
        results = []
        match self.text_type:

            case "1":                       #数字特码
                rows, amount = self.get_number(text=self.text)
                state = self.record(rows,amount)
                results.append(f'录入文本：  {self.text}\n录入表格：  {self.sheet_name}\n录入状态：  {state}\n录入位置：  第{",".join(map(str, rows))}行\n录入金额：  ￥{amount} 元\n')
                return  "\n".join(results)

            case "2":                       #生肖特码
                rows = []
                animals, amount = self.get_animals(self.text)
                for animal in animals:
                 rows += self.animal_index(animal)
                state = self.record(rows,amount)
                results.append(f'录入文本：  {self.text}\n录入表格：  {self.sheet_name}\n录入状态：  {state}\n录入位置：  第{",".join(map(str, rows))}行\n录入金额：  ￥{amount} 元\n')
                return  "\n".join(results)

            case "3":                        #生肖包肖
                rows = []
                animals, amount = self.get_animals(self.text)
                for animal in animals:
                 rows = self.animal_index(animal)
                 if  animal == "兔" :
                    amount_1 = int(amount)/5
                    state = self.record(rows,amount_1)
                 else:
                    amount_1 = int(amount)/4
                    state = self.record(rows,amount_1)
                 results.append(f'录入文本：  {self.text}\n录入表格：  {self.sheet_name}\n录入状态：  {state}\n录入位置：  第{",".join(map(str, rows))}行\n录入金额：  ￥ {amount_1} 元\n')
                return  "\n".join(results)
                    
            case "4":               #红蓝绿波+单双
                rows = color(self.text).run()
                amounts = re.findall(r'\d+',self.text)
                amount = amounts[-1]
                state = self.record(rows,amount)
                results.append(f'录入文本：  {self.text}\n录入表格：  {self.sheet_name}\n录入状态：  {state}\n录入位置：  第{",".join(map(str, rows))}行\n录入金额：  ￥ {amount} 元\n')
                return  "\n".join(results)
                
            case "5":               #大小
                rows = num(self.text).run()
                amounts = re.findall(r'\d+',self.text)
                amount = amounts[-1]
                state = self.record(rows,amount)
                results.append(f'录入文本：  {self.text}\n录入表格：  {self.sheet_name}\n录入状态：  {state}\n录入位置：  第{",".join(map(str, rows))}行\n录入金额：  ￥ {amount} 元\n')
                return  "\n".join(results)
            
            case "6":               #尾
                rows,amount = self.get_tail(self.text)
                state = self.record(rows,amount)
                results.append(f'录入文本：  {self.text}\n录入表格：  {self.sheet_name}\n录入状态：  {state}\n录入位置：  第{",".join(map(str, rows))}行\n录入金额：  ￥ {amount} 元\n')
                return  "\n".join(results)

            case "7":               #头
                rows,amount = self.get_head(self.text)
                state = self.record(rows,amount)
                results.append(f'录入文本：  {self.text}\n录入表格：  {self.sheet_name}\n录入状态：  {state}\n录入位置：  第{",".join(map(str, rows))}行\n录入金额：  ￥ {amount} 元\n')
                return  "\n".join(results)
                
    def run(self):                         #运行程序  
        self.type_select()
        self.sheet_select()
        text = self.type_input()
        return text,self.result

class num:      #大小
    def __init__(self,text):
        self.text = text
    
    def add(self):
        rows = []
        if "小" in self.text:
            rows = range(1,25)
        if "大" in self.text:
            rows = range(25,50)

        return rows
    
    def sub(self,rows):
        if "单" in self.text:
            rows = [x for x in rows if x % 2 != 0]
        elif "双" in self.text:
            rows = [x for x in rows if x % 2 == 0]
        elif "偶" in self.text:
            rows = [x for x in rows if x % 2 == 0]
        else:
            rows = rows
        return rows

    def run(self):
        rows = self.add()
        return self.sub(rows)

class color:  #红蓝绿波
    
    def __init__(self,text):
        self.text = text
    
    def add(self):
        red = [1, 2, 7, 8, 12, 13, 18, 19, 23, 24, 29, 30, 34, 35, 40, 45, 46]
        blue = [3, 4, 9, 10, 14, 15, 20, 25, 26, 31, 37, 42, 36, 41, 47, 48]
        green = [5, 6, 11, 16, 17, 21, 22, 27, 28, 32, 33, 38, 39 ,43, 44, 49]
        rows = []

        if "红" in self.text:
            rows += red
        if "蓝" in self.text:
            rows += blue
        if "绿" in self.text:
            rows += green
        return rows
    
    def sub(self,rows):
        if "单" in self.text:
            rows = [x for x in rows if x % 2 != 0]
        elif "双" in self.text:
            rows = [x for x in rows if x % 2 == 0]
        elif "偶" in self.text:
            rows = [x for x in rows if x % 2 == 0]
        else:
            rows = rows
        return rows

    def run(self):
        rows = self.add()
        return self.sub(rows)


if __name__ == '__main__':
    index_list = ["兔", "虎", "牛", "鼠", "猪", "狗", "鸡", "猴", "羊", "马", "蛇", "龙"]*4+['兔']
    tab2, tab3 = st.tabs([ "Aomen","Hongkong"])
    with st.sidebar:
        st.markdown('''
        # 测试页面
                ''')
    prompt = st.chat_input("Enter here !")
    if prompt:
        message ,result= RecordData(prompt).run()
        with st.chat_message("Liaco"):
            st.write(message)
            with tab2:
                st.dataframe(pd.DataFrame(result[0],index=index_list))
            with tab3:
                st.dataframe(pd.DataFrame(result[1],index=index_list))          
