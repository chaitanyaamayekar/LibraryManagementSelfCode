import json
import random
import string
from pathlib import Path

class MemberManagement():
    database = 'member.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exist")
    except Exception as err:
        print(f"Exception:{err}")

    @classmethod
    def idgenerate(cls):
        alpha = random.choices(string.ascii_uppercase, k=3)
        digit = random.choices(string.digits, k=2)

        id_no = alpha + digit
        random.shuffle(id_no)

        return "M" + "".join(id_no)

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data,indent= 4))
    
    def addMember(self):
        info = {
            'name': input("Name: "),
            'age': int(input("Age: ")),
            'phone': input("Phone Number: "),
            'email':input("Email: "),
            'id': MemberManagement.idgenerate()
        }
        phone_valid =  len(str(info['phone'])) == 10 and info['phone'].isdigit()
        email_valid = "@" in info['email'] and "." in info['email'].split("@")[-1]
        if phone_valid and email_valid:
            print("Id:",info['id'])
            print(f"Account Created Successfully!, Welcome {info['name']}.")
            MemberManagement.data.append(info)
            MemberManagement.__update()
        else:
            print("Invalid Phone Number Or Email! Redo Both")

    def showDetails(self):
        try:
            name = input("Name: ")
            id = input("Member Id: ")
            mem_info = [i for i in MemberManagement.data if i['name'] == name and i['id'] == id]
        
            if mem_info:
                 print("=" * 30)
                 for i in mem_info[0]:
                     print(f"{i}:{mem_info[0][i]}")
                 print("=" * 30)

            else:
                print("No Such User Found!")
        except Exception as err:
            print(f"Error Occured As: {err}")
  
    def search(self):
        name = input('Enter Name: ')
        id = input('Enter Member id:')
        mem_info = [ i for i in MemberManagement.data if i['name'] == name and i['id'] == id]

        print("Member Details :-")
        
        if mem_info:
            for i in mem_info[0]:
                print(f"{i} :{mem_info[0][i]}")
        else:
            print("no such user found!")

    def updateDetails(self):
        name = input("Member Name: ")
        id = input("Member id: ")
        mem_info = [i  for i in MemberManagement.data if i['name'] == name and i['id'] == id ]

        print("Note You can only update :\n Name | Phone no. | Email ")

        if mem_info == False:
            print("No such user found!")
        else:
            print("[Fill the details to change else leave Empty and press ENTER]")

            new_data = {
                "name" :input("Name: "),
                "phone" : input("Phone no: "),
                "email" : input("Email: ")
            }
            if new_data['name'] == "":
                new_data['name'] = mem_info[0]['name']
            if new_data['phone'] == "":
                new_data['phone'] = mem_info[0]['phone']
            if new_data['email'] == "":
                new_data['email'] = mem_info[0]['email']
            new_data['age'] = mem_info[0]['age']
            new_data['id'] = mem_info[0]['id']

            for i in new_data:
                if new_data[i] == mem_info[0][i]:
                    continue
                else:
                    mem_info[0][i] = new_data[i]
            MemberManagement.__update()

            for i in new_data:
                print(f"{i}:{new_data[i]}")
                print("Member Details Updated Successfully!")

    def deleteMem(self):
        name = input("Member Name: ")
        id = input("Member id: ")
        mem_info = [i  for i in MemberManagement.data if i['name'] == name and i['id'] == id ]

        if mem_info == False:
            print("no user found!")
        else:
            check = input("Press 'Y' to delete \nPress 'N' to cancel deletion")
            if check == 'N' or check == 'n':
                pass
            else:
                index = MemberManagement.data.index(mem_info[0])
                MemberManagement.data.pop(index)   
                print("Account Deleted Successfully!")
                MemberManagement.__update()    

member = MemberManagement()

print("Press 1 To Add New Member")
print("Press 2 To View Member Details")
print("Press 3 To Search a Member")
print("Press 4 To Update Member Details")
print("Press 5 To Delete Member")

opt = int(input("Press Your Response:"))
if opt == 1:
    member.addMember()
if opt == 2:
    member.showDetails()
if opt == 3:
    member.search()
if opt == 4:
    member.updateDetails()
if opt == 5:
    member.deleteMem()