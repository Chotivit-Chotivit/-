#โปรเเกรมคำนวณภาษี บุคคลธรรมดา 
#เริ่มพัฒนา 21/3/2024 - 28/3/2024



#สูตรการคำนวณหาภาษีที่ต้องชำระ = [(เงินได้สุทธิของตนเอง - เงินได้สุทธิที่มากที่สุดของลำดับขั้นก่อนหน้า) X อัตราภาษี (%)] + ภาษีสะสมสูงสุดของลำดับขั้นก่อนหน้า
#รายได้ทั้งปี - ค่าใช้จ่าย - ค่าลดหย่อน = เงินได้สุทธิ


import xlsxwriter
import pandas as pd




hi = 'สวัสดี\nยินดีต้อนรับเข้าสู่\n----------------คำนวณภาษีสุดเเมว----------------------\n'
hi1 = hi.center(50)
print(hi1)


yearincome = int(input("รายได้ทั้งปี :"))
expenses = int(input("ค่าใช้จ่ายส่วนตัว :"))

                 
lst =[] #ค่าของค่าลดหย่อน
typetax = [] #ประเภทค่าลดหย่อน


Allowanceloop = int(input("จำนวณการลดหย่อนที่มี:"))

for k in range(0,Allowanceloop):
    k = k+1
    ele =int(input("ค่าลดหย่อน(บาท) :"))
    elty = str(input('ประเภทค่าลดหย่อน:'))

    lst.append(ele)  #ผนวกlstกับele
    typetax.append(elty) #ผนวกtypetaxกับelty

print(lst)
print(typetax)

dicttype = dict(zip(typetax,lst)) #เเปลงlistเป็นอยู่ในdict
print(dicttype)


print("---------------------------------------------\n")
print('ค่าลดหย่อนทั้งหมด:',sum(lst))
print("---------------------------------------------\n")

netincome =  yearincome-expenses-sum(lst)


print("เงินได้สุทธิ =",netincome,("บาท"))

print("---------------------------------------------\n")

if netincome <= 150000: 
    print("คุณไม่ต้องเสียภาษี")
    print("---------------------------------------------\n")
    exit()
    
    
       
elif netincome >= 150001 and netincome <= 300000:
    print("อัตราภาษีอยู่ที่ 5%")
    tax = 0.05      #อัตราภาษี
    Maxtax = 0    #Maxtax = ภาษีสะสมสูงสุดของลำดับขั้นก่อนหน้า
    incomebefore = 150000 #เงินได้สุทธิจำนวนสูงสุดของขั้นก่อนหน้า


elif netincome >= 300001 and netincome <= 500000:
    print("อัตราภาษีอยู่ที่ 10%")
    tax = 0.10
    Maxtax = 7500
    incomebefore = 300000

elif netincome >= 500001 and netincome <= 750000:
    print("อัตราภาษีอยู่ที่ 15%")
    tax = 0.15
    Maxtax = 27500
    incomebefore = 500000

elif netincome >= 750001 and netincome <= 1000000:
    print("อัตราภาษีอยู่ที่ 20%")
    tax = 0.20
    Maxtax = 65000
    incomebefore = 750000

elif netincome >= 1000001 and netincome <= 2000000:
    print("อัตราภาษีอยู่ที่ 25%")
    tax = 0.25
    Maxtax =  115000
    incomebefore = 1000000

elif netincome >= 2000001 and netincome <= 5000000:
    print("อัตราภาษีอยู่ที่ 30%")
    tax = 0.30
    Maxtax =  365000
    incomebefore = 2000000

elif netincome >= 5000001:
    print("อัตราภาษีอยู่ที่ 35%")
    tax = 0.35
    Maxtax = 1265000
    incomebefore = int(input("เงินได้สุทธิที่มากที่สุดของลำดับขั้นก่อนหน้า\nเนื่องจากไม่มีเพดานรายได้ ท่านต้องคำนวณเอง:) :"))

print("---------------------------------------------\n")
Taxpayable = ((netincome-incomebefore)*tax)+Maxtax 
print("ภาษีที่ต้องชำระ:",Taxpayable,"บาท")




saveexcel = str(input('คุณต้องการsaveข้อมูลของคุณเป็นExcelมั้ย?\nyes or no :'))


if saveexcel =='yes'or saveexcel =='ใช่' or saveexcel=='/':
    nameexcel = str(input("โปรดระบุบชื่อไฟล์ที่ต้องการsave :"))


elif saveexcel =='no' or saveexcel=='ไม่'or saveexcel=='x' or  saveexcel =='*': 
    print("----------------By Chotivit Busamongkol--------------------\n")
    exit()

# การนำข้อมูลที่คำนวณเเละไดก้มาทั้งหมดมาจัดอยู่ในรูปexcel
data = {
    "   ข้อมูลที่เกี่ยวกับการคำนวณฯภาษี": ['รายได้ทั้งปี', 'ค่าใช้จ่าย', 'ค่าลดหย่อนทั้งหมด', 'เงินได้สุทธิ', 'ภาษีสะสมสูงสุดของลำดับขั้นก่อนหน้า', 'เงินได้สุทธิจำนวนสูงสุดของขั้นก่อนหน้า', 'ภาษีที่ต้องชำระ(บาท)'],
    "จำนวณเงินเป็น(บาท)": [yearincome, expenses, sum(lst), netincome, Maxtax, incomebefore, Taxpayable],

}


df = pd.DataFrame(data) 

writer = pd.ExcelWriter(nameexcel+'.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='หน้าที่1')

writer.close()

print("----------------By Chotivit Busamongkol--------------------\n")