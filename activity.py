import pymysql

connection = pymysql.connect(
    host        = 'localhost',      
    user        = 'root',
    password    = 'password',
    db          = 'Output',
)




def add_activity(activity,score):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `activity` (`id`, `activity`, `score`) VALUES (NULL, %s, %s);"
        try:
            cursor.execute(sql, (activity,score))
            print("New Activity Added!")
        except:
            print("Sorry Something wrong!")

    connection.commit()

def view_activity(add_activity):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `activity`"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
 
            print("id\t\t activity\t\t score\t\t\t")
            print("---------------------------------------------------")
            for row in result:
                print(str(row[0]) + "\t\t" + row[1] + "\t\t\t" + row[2])
 
        except:
            print("Oops! Something wrong")
 
    connection.commit()

def update_activity(id):
    with connection.cursor() as cursor:
             cursor.execute("SELECT * FROM activity WHERE `id` = %s",id)
             cursor.fetchall()
             if cursor.rowcount > 0 :
                new_activity = raw_input("Enter New Activity: ")
                new_score    = raw_input("Enter New Score: ")
                cursor.execute("UPDATE activity SET `activity`=%s, `score`=%s WHERE `id` = %s", (new_activity,new_score,id))
                print("Successfully Updated")
             else:
                print("ID '"+id+"' does'nt match")
 
    connection.commit()

def delete_activity(id):
    with connection.cursor() as cursor:
        sql =  "SELECT *  FROM `activity` WHERE `id` = %s"
        try:
            cursor.execute(sql, id)
            if cursor.rowcount > 0 :
                del_activity = "DELETE FROM `activity` WHERE `id` = %s"
                cursor.execute(del_activity, id)
                print "Activity Successfully Deleted"
            else:
                print "ID '" + id + "' is not Exist!"
        except:
            print("Oops! Something wrong!!")

    connection.commit() 

loop = 1
while loop:

    print"----CHOICES---"
    print"[C] Create Activity"
    print"[R] Read/View Activity"
    print"[U] Update Activity"
    print"[D] Delete Activity"
    print"[E] Exit Program\n"



    choice = raw_input("Enter your choice: ")

    if choice == 'C':
        activity            = raw_input('Enter What activity? : ')
        score               = raw_input('Enter score: ')
        add_activity(activity,score)

    if choice == 'c':
        activity            = raw_input('Enter What activity? : ')
        score               = raw_input('Enter score: ')
        add_activity(activity,score)
    
    elif choice == 'R':
        view_activity(add_activity)
        print("---------------------------------------------------")
    elif choice == 'r':
        view_activity(add_activity)
        print("---------------------------------------------------")
    elif choice == 'U':
        id = raw_input("Enter ID to update Data : ")
        update_activity(id)

    elif choice == 'u':
        id = raw_input("Enter ID to update Data : ")
        update_activity(id)

    elif choice == 'D':
        id = raw_input("Enter ID to Delete Data: ")
        delete_activity(id)

    elif choice == 'd':
        id = raw_input("Enter ID to Delete Data: ")
        delete_activity(id)
    elif choice == 'E':
        print "Program Closed!!!"

    elif choice == 'e':
        print "Program Closed!!!"

        break 
    else:
        print "Invalid Choice"
    
    
    loop_2 = 1
    while loop_2:
        cont = raw_input("\nDo you wish to continue ? [Y/N]: ").strip()
        if cont in 'Yy':
            loop_2 = 0
            loop = 1
        elif cont in 'Nn':
            print "Program Closed!!!"
            loop_2 = 0
            loop = 0
        else:
            print 'Invalid Choice'
            loop_2 = 1
