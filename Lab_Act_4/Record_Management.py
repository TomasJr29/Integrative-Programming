check = 0

while check != 7:
    
    print("")
    
    print("[1] Open File")
    print("[2] Show All Students Record")
    print("[3] Show Student Record")
    print("[4] Add Record")
    print("[5] Edit Record")
    print("[6] Delete Record")
    print("[7] Exit")

    print("")

    check = int(input("Enter your choice: "))
    
    if check == 1:
        print("")
        print("Open File")
        print("")
        filename = str(input("Enter file name: "))
        file_name = filename + ".txt"
            
        choice = 0
        
        while choice != 3:
            print("")
            print("[1] Save")
            print("[2] Save As")
            print("[3] Cancel")
            
            print("")
            
            choice = int(input("Enter your choice: "))
                
            if choice == 1:
                file = open(file_name, "a")
                file.close()
                print("")
                print("File opened successfully")
                
                choice = 3
                
            elif choice == 2:
                print("")
                temp_file_path = str(input("input file path: "))
                file_path = temp_file_path.replace("\"", "/")
                files = file_path + "/" + file_name 
                save_file = open(files, "a")
                save_file.close()
                print("")
                print("File opened successfully")
                
                choice = 3
        
    elif check == 2:
        checkfile = 0
        while checkfile != 1:
            print("")
            check_record = str(input("Enter file name (If file was saved using the SAVE AS option please provide the full file path): "))
            filename1 = check_record + ".txt"
            try:
                check_file1 = open(filename1, "r")
                check_file1.close()
                checkfile = 1
            except FileNotFoundError:
                print("")
                print("File not found")
                print("")
                checkfile = 0
        
        check_2 = 0
        
        while check_2 != 3:
            print("")
            print("[1] Order by last name")
            print("[2] Order by grade")
            print("[3] Cancel")
            
            print("")
            
            check_2 = int(input("Please enter your choice: "))
            
            print("")
             
            if check_2 == 1:
                
                with open(filename1, "r") as data:
                    records = data.read().strip().split("\n\n")
                    student_data =  records
                    result = []
                    for row in student_data:
                        result.append(row[10]) 
                    sorted_records = sorted(result, key = lambda x: x[2], reverse = True) 
                    for record in sorted_records:
                        print(str(record).strip() + "\n --------------------------------")
                    
            elif check_2 == 2:
                with open(filename1, "r") as data:
                    records = data.read().strip().split("\n\n")
                    student_data =  records
                    result = []
                    for row in student_data:
                        result.append(row[-5:-3]) 
                    sorted_records = sorted(result, key = lambda x: x[1], reverse = True) 
                    for record in sorted_records:
                        print(str(record).strip() + "\n --------------------------------")
        
        
    elif check == 3:
        print("Show Student Record")
    elif check == 4:
        check_4 = 0
        
        while check_4!= 1:
        
            opening_file = 0
            while opening_file != 1:
                print("")
                add_record = str(input("Enter file name (If file was saved using the SAVE AS option please provide the full file path): "))
                filename = add_record + ".txt"
                try:
                    check_file = open(filename, "r")
                    check_file.close()
                    opening_file = 1
                except FileNotFoundError:
                    print("")
                    print("File not found")
                    print("")
                    
                    opening_file = 0
            
            check_id = 0
            
            while check_id != 1:
                print("")
            
                student_id = int(input("Enter Student ID (6 digits): "))
                
                if len(str(student_id)) == 6:
                    check_id = 1
                else:
                    print("")
            
                    print("Enter a valid ID")
                    
            check_fname = 0
            
            while check_fname != 1:
                print("")
            
                student_fname = str(input("Enter Student First Name: "))
                
                if student_fname.isalpha():
                    check_fname = 1
                else:
                    print("")
            
                    print("Enter a valid name (no speacial characters and numbers)")
            
            check_lname = 0
            
            while check_lname != 1:
                print("")
            
                student_lname = str(input("Enter Student Last Name: "))
                
                if student_lname.isalpha():
                    check_lname = 1
                else:
                    print("")
            
                    print("Enter a valid name (no speacial characters and numbers)")  
                    
            full_name = student_lname[0].upper() + student_lname[1:].lower() + ", " + student_fname[0].upper() + student_fname[1:].lower()
            
            check_class_standings = 0
            
            while check_class_standings != 1:
                print("")
            
                class_standings = int(input("Enter Class Standings: "))
                
                if class_standings >= 0 and class_standings <= 100:
                    check_class_standings = 1
                else:
                    print("")
            
                    print("Enter a valid grade (0-100)")
            
            check_midterm = 0
            
            while check_midterm != 1:
                print("")
            
                midterm = int(input("Enter Midterm grade: "))
                
                if midterm >= 0 and midterm <= 100:
                    check_midterm = 1
                else:
                    print("")
            
                    print("Enter a valid grade (0-100)")
            
            check_final = 0
            
            while check_final != 1:
                print("")
            
                final = int(input("Enter Final grade: "))
                
                if final >= 0 and final <= 100:
                    check_final = 1
                else:
                    print("")
            
                    print("Enter a valid grade (0-100)")
                    
            temp_grade = ((final * 0.2) + (midterm *.2)) + (class_standings * 0.6)
            grade = temp_grade
            
            saving_check = 0
            
            student_record = [student_id, full_name, grade]
            
            while saving_check!= 3:
                print("")
                print("[1] Save record")
                print("[2] Cancel")
                
                print("")
                
                saving_check = int(input("Enter your choice: "))
                
                if saving_check == 1:
                    check_file = open(filename, "a+")
                    check_file.write("\n \n" + str(student_record))
                    check_file.close()
                    print("")
                    print("Record has been saved")
                    print("")
                    saving_check = 3
                
                elif saving_check == 2:
                    print("")
                    saving_check = 3
                    
            check_4 = 1
            
    elif check == 5:
        print("Edit Record")
    elif check == 6:
        print("Delete Record")
    elif check == 7:
        print("Exit")
    else:
        print("Wrong Choice")
    
    
