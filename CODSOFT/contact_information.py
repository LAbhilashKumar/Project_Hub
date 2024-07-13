phone_dict={}

while True:
    userinput=int(input("""1. Add new contact
    2. View contact
    3. Search contact
    4. Update contact
    5. Delete contact\n"""))

    if userinput == 1:
        name=input("Enter name:")
        limit=int(input("How many phone numbers do you want to save?"))
        phone_number=[]
        while limit>0:
            number=input("enter phone number ")
            if number.isdigit() and len(number) == 10:
                phone_number.append(number)
            else:
                print("enter valid number")
                continue
            limit-=1
        email_Id=input("enter email ID")
        address=input("enter address")
        phone_dict[name]={
            "Phone number": phone_number,
            "email_ID": email_Id,
            "address": address
        }
    if phone_dict!={}:
        if userinput == 2:
            for name , others in phone_dict.items():
                print(f"Name :{name} Phone number :{others['Phone number']} email_ID :{others['email_ID']}")

        elif userinput == 3:
            search=input("enter name to search ")
            if search in phone_dict:
                a=phone_dict[search]
                print(f"contact found\n Name: {search}\n phone number: {a['Phone number']}\n email_ID: {a['email_ID']}")
            else:
                print("contact not found ")

        elif userinput == 4:  # update contact

            name=input("enter name")
            if name in phone_dict:
                a=phone_dict[name]
                update=input("enter new phone number ")
                if update.isdigit() and len(update) == 10:
                        a['Phone number'][0]=update
                        print("phone number updated successfully ")
            else:
                print("No contact found ")

        elif userinput == 5:
            name=input("enter name to delete contact")
            if name in phone_dict:
                del phone_dict[name]
                print("deleted successfully ")
            else:
                print("contact not found")





    else:
        print("dict is empty"); continue




