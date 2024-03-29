import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="canteenmanagement"
)

mycursor = mydb.cursor()
    

class Employee:

    def __init__(self,EmpID,EmpLName,EmpFName,Birthday,Address,DateofEmplymnt,JobID):
        self.EmpID = EmpID
        self.EmpLName = EmpLName
        self.EmpFName = EmpFName
        self.Birthday = Birthday
        self.Address = Address
        self.DateofEmplymnt = DateofEmplymnt
        self.JobID = JobID

    def create(self):
        mycursor.execute("INSERT INTO employeetbl (EmpID, EmpLName, EmpFName, Birthday, Address, DateofEmplymnt, JobID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                 (self.EmpID, self.EmpLName, self.EmpFName, self.Birthday, self.Address, self.DateofEmplymnt, self.JobID))
        mydb.commit()

        messagebox.showinfo("Success", "Employee Added Successfully")

    def fetch_employee():
        mycursor.execute('SELECT EmpID,EmpLName,EmpFName,Birthday,Address,JobDescription,TypeOfEmplymnt,DateOfEmplymnt FROM employeetree')
        Employee = mycursor.fetchall()
        mydb.commit()
        return Employee

    def fetch_ID():
        mycursor.execute('SELECT EmpID FROM employeetbl')
        Employee = mycursor.fetchall()
        mydb.commit()
        return Employee

    def update_employee(self):
        mycursor.execute("UPDATE employeetbl SET EmpLName = %s, EmpFName = %s, Birthday = %s, Address = %s, DateofEmplymnt = %s, JobID = %s WHERE EmpID = %s",
                 (self.EmpLName, self.EmpFName, self.Birthday, self.Address, self.DateofEmplymnt, self.JobID, self.EmpID))
        mydb.commit()
        messagebox.showinfo("Success", "Employee Updated Successfully")
        

    def delete_employee(self):
        response = messagebox.askyesno("Delete", "Are you sure you want to delete this employee?")
        if response == 1:
            mycursor.execute("DELETE FROM employeetbl WHERE EmpID = %s", (self.EmpID,))
            mydb.commit()
            messagebox.showinfo("Success", "Employee Deleted Successfully")
        else:
            pass
    
class Login:
    def __init__(self,LoginID,LoginCredentials,EmpID,Username,Password):
        self.LoginID = LoginID
        self.LoginCredentials = LoginCredentials
        self.EmpID = EmpID
        self.Username = Username
        self.Password = Password


    def create_admin(self):
        mycursor.execute("INSERT INTO logintbl (LoginCredentials, EmpID, Username, Password) VALUES (%s, %s, %s, %s)",
        (self.LoginCredentials, self.EmpID, self.Username, self.Password))
        mydb.commit()
        messagebox.showinfo("Success", "Account Created Successfully")

    def update_admin(self):
        mycursor.execute("UPDATE logintbl SET LoginCredentials = %s WHERE EmpID = %s",
        (self.LoginCredentials, self.EmpID))
        mydb.commit()
        messagebox.showinfo("Success", "Account Updated Successfully")

    


    def change_pass(self):
        mycursor.execute("UPDATE logintbl SET Password = %s WHERE EmpID = %s",
        (self.Password, self.EmpID))
        mydb.commit()
        messagebox.showinfo("Success", "Password Changed Successfully")

class OrderLine:
    def __init__(self,OrderID,ProductID,Quantity):
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.Quantity = Quantity


class LoggedIn:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def get_login(self):
        mycursor.execute('INSERT INTO loggedin (username, password) VALUES (%s, %s)', (self.username, self.password))
        mydb.commit()
    


    def change_pass(self):
        mycursor.execute("UPDATE logintbl SET Password = %s WHERE username = %s",
        (self.password, self.username))
        mycursor.execute('UPDATE loggedin SET password = %s WHERE username = %s', (self.password, self.username))
        mydb.commit()
        messagebox.showinfo("Success", "Password Changed Successfully")

    def log_out(self):
        mycursor.execute('DELETE FROM loggedin where username = %s', (self.username,))
        mydb.commit()




    


