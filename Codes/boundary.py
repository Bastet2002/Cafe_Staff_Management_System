import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import StringVar
import controller
import entity

class LoginPg:
    def __init__(self, root):
        self.loginController = controller.LoginController()

        self.root = root
        self.root.title("Cafe Staff Management System")
        self.root.geometry("1400x750")

        # Create and place widgets by calling the display() function.
        self.displayLoginPg()

    def displayLoginPg(self):
        
        #making a main log in frame
        self.loginFrame = tk.Frame(self.root, bg="#D3D3D3")
        self.loginFrame.pack(fill="both", expand=True)
        # Header
        self.header_frame = tk.Frame(self.loginFrame, bg="#DA7635")
        self.header_frame.pack(fill="x")

        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.header_frame, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(side="left", padx=20, pady=10)

        self.nav_frame = tk.Frame(self.header_frame, bg="#DA7635")
        self.nav_frame.pack(side="right")

        
        self.lgnbutton = tk.Button(self.nav_frame, text="LOG IN")
        self.lgnbutton.pack(side="left", padx=20)
        self.lgnbutton.configure(bg = "blue", activebackground="blue")
        
    
        self.containerFrame = tk.Frame(self.loginFrame, bg="#D3D3D3")
        self.containerFrame.pack()
        # Username label and entry
        self.title_label = tk.Label(self.containerFrame, text="Welcome", font=("Paprika", 70), bg = "#D3D3D3", fg="#DA7635")
        self.title_label.pack(pady=80)

        self.form_frame = tk.Frame(self.loginFrame, bg="#D3D3D3")
        self.form_frame.pack()

        self.username_label = tk.Label(self.form_frame, text="Your Username", font=("Josefin Sans", 18),bg="#D3D3D3", fg="#DA7635")
        self.username_label.pack(pady=20)

        self.username_entry = tk.Entry(self.form_frame, font=("Josefin Sans", 14))
        self.username_entry.pack()

        self.password_label = tk.Label(self.form_frame, text="Password", font=("Josefin Sans", 18), bg="#D3D3D3", fg="#DA7635")
        self.password_label.pack(pady=20)

        self.password_entry = tk.Entry(self.form_frame, show="*", font=("Josefin Sans", 14))
        self.password_entry.pack()

        self.forgot_password_button = tk.Button(self.form_frame, text="Change Password", command = self.openChangePwPg, font=("Josefin Sans", 18), cursor="hand2", fg="#DA7635", bg="#D3D3D3")
        self.forgot_password_button.pack(pady=20)

        self.login_button = tk.Button(self.form_frame, text="LOG IN", command=self.login)
        self.login_button.pack()


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        user = self.loginController.userLogin(username, password)
        if (user):
            if (user.userProfile.profileName == "system_admin"):
                messagebox.showinfo("Login Successful", "You have successfully logged in!")
                self.openAdminPg(user)
            elif (user.userProfile.profileName == "cafe_owner"):
                messagebox.showinfo("Login Successful", "You have successfully logged in!")
                self.openOwnerPg(user)
            elif (user.userProfile.profileName == "cafe_manager"):
                messagebox.showinfo("Login Successful", "You have successfully logged in!")
                self.openManagerPg(user)
            elif (user.userProfile.profileName == "cafe_staff"):
                messagebox.showinfo("Login Successful", "You have successfully logged in!")
                self.openStaffPg(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")
        
    def openChangePwPg(self):
        #self.backgroundLabel.place_forget()
        self.loginFrame.pack_forget()
        ChangePwPg(self.root)

    def openAdminPg(self, user):
        #self.backgroundLabel.place_forget()
        self.loginFrame.pack_forget()
        AdminPg(self.root, user)
        
    def openOwnerPg(self, user):
        #self.backgroundLabel.place_forget()
        self.loginFrame.pack_forget()
        OwnerPg(self.root, user)
    
    def openManagerPg(self, user):
        #self.backgroundLabel.place_forget()
        self.loginFrame.pack_forget()
        ManagerPg(self.root, user)
        
    def openStaffPg(self, user):
        #self.backgroundLabel.place_forget()
        self.loginFrame.pack_forget()
        StaffPg(self.root, user)
    

class ChangePwPg():
    def __init__(self, root):
        self.changePwController = controller.ChangePwController()
        self.root = root

        self.displayChangePwPg()

    def displayChangePwPg(self):
        
        self.changePwFrame = tk.Frame(self.root, bg="#D3D3D3")
        # Header
        self.header_frame = tk.Frame(self.changePwFrame, bg="#DA7635")
        self.header_frame.pack(fill="x")

        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.header_frame, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(side="left", padx=20, pady=10)

        self.nav_frame = tk.Frame(self.header_frame, bg="#DA7635")
        self.nav_frame.pack(side="right")
        
        self.lgnbutton = tk.Button(self.nav_frame, text="LOG IN" , command = self.openLoginPg)
        self.lgnbutton.pack(side="left", padx=20)
        self.lgnbutton.configure(bg = "blue", activebackground="blue")
        
        # Content
        self.container_frame = tk.Frame(self.changePwFrame, bg="#D3D3D3")
        self.container_frame.pack(pady=100)

        title_label = tk.Label(self.container_frame, text="CHANGE PASSWORD", font=("Paprika", 35), bg="#D3D3D3", fg="#DA7635")
        title_label.pack(pady=30)

        self.form_frame = tk.Frame(self.container_frame, bg="#D3D3D3")
        self.form_frame.pack()

        # Username
        self.username_label = tk.Label(self.form_frame, text="Username", font=("Josefin Sans", 14),bg="#D3D3D3", fg="#DA7635")
        self.username_label.grid(row=1, column=0, padx=5, sticky="w")

        self.username_entry = tk.Entry(self.form_frame, font=("Josefin Sans", 14))
        self.username_entry.grid(row=1, column=1, padx=5)

        # Old Password
        self.old_password_label = tk.Label(self.form_frame, text="Old Password", font=("Josefin Sans", 14), bg="#D3D3D3", fg="#DA7635")
        self.old_password_label.grid(row=3, column=0, padx=5, sticky="w")

        self.old_password_entry = tk.Entry(self.form_frame, font=("Josefin Sans", 14, 'bold'))
        self.old_password_entry.grid(row=3, column=1, padx=5)

        # New Password
        self.new_password_label = tk.Label(self.form_frame, text="New Password", font=("Josefin Sans", 14),bg="#D3D3D3", fg="#DA7635")
        self.new_password_label.grid(row=4, column=0, padx=5, sticky="w")

        self.new_password_entry = tk.Entry(self.form_frame, font=("Josefin Sans", 14, 'bold'))
        self.new_password_entry.grid(row=4, column=1, padx=5)

        # Confirm Password
        self.confirm_password_label = tk.Label(self.form_frame, text="Re-enter Password", font=("Josefin Sans", 14),bg="#D3D3D3", fg="#DA7635")
        self.confirm_password_label.grid(row=6, column=0, padx=5, sticky="w")

        self.confirm_password_entry = tk.Entry(self.form_frame, font=("Josefin Sans", 14, 'bold'))
        self.confirm_password_entry.grid(row=6, column=1, padx=5)

        # Change Password Button
        self.change_password_button = tk.Button(self.form_frame, text="CHANGE PASSWORD", font=("Josefin Sans", 14, 'bold'), command=self.changePw, bg="#33373D", fg="Black", bd=3)
        self.change_password_button.grid(row=10, column=0, columnspan=2, pady=20)
        
        self.changePwFrame.pack(fill="both", expand=True)

    def changePw(self):
        username = self.username_entry.get()
        oldPw = self.old_password_entry.get()
        newPw1 = self.new_password_entry.get()
        newPw2 = self.confirm_password_entry.get()
       
        if (newPw1 != newPw2):
            messagebox.showerror("Notice", "New Password and Confirm Password are not the same. Please try again")
        else:
            result = self.changePwController.changePassword(username, oldPw, newPw1)
            if (result):
                messagebox.showinfo("Successful!", "Changed Password Successfully! Proceed to Log In page")
                self.openLoginPg()
            else:
                messagebox.showerror("Failed!", "Please check username and old password are entered correctly")

    def openLoginPg(self):
        self.changePwFrame.pack_forget()
        LoginPg(self.root)
        

class AdminPg():
    def __init__(self, root, user):
        self.loginController = controller.LoginController()
        self.root = root
        self.user = user

        self.displayAdminPg()

    def displayAdminPg(self):
        # Display welcome label
        self.mainLabel = tk.Label(self.root, text="Welcome to the Admin Page")
        self.mainLabel.pack(fill="both", expand=True)

        
        #creating admin main frame
        self.adminFrame = tk.Frame(self.root, bg="#EBDFD3")
        self.adminFrame.pack(fill="both", expand=True)
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.adminFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)
        

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        self.logoutButton = tk.Button(self.sidebar, text="Logout", command=self.logout)
        self.logoutButton.pack(pady=(520, 0))

        # Create the main content area
        self.main_content = tk.Frame(self.adminFrame, width=1400, height=800, bg="#EBDFD3")
        self.main_content.grid(row=0, column=1)

        # Add a welcome message
        self.welcome_label = tk.Label(self.main_content, text="Welcome Admin!", font=("Josefin Sans", 30), bg="#EBDFD3", fg = "black")
        self.welcome_label.pack(pady=55)

        # Create function buttons
        self.function_buttons = tk.Frame(self.main_content, bg="#EBDFD3")
        self.function_buttons.pack()
        
        self.function_buttons = tk.Frame(self.main_content, bg="#EBDFD3")
        self.function_buttons.pack()
        
        self.button_frame = tk.Frame(self.function_buttons, bg="#EBDFD3")
        self.button_frame.pack(side="left", padx=40, pady=40)


        # Add buttons
        self.button1 = tk.Button(self.button_frame, text="View Own Account", command=self.openOwnAccountInfoPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button1.grid(row= 0, column = 0)

        self.button2 = tk.Button(self.button_frame, text="Create User Account", command=self.openCreateAccountPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button2.grid(row= 0, column = 1)

        self.button3 = tk.Button(self.button_frame, text="Manage User Account", command= self.openViewAllAccPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button3.grid(row= 1, column = 0)

        self.button4 = tk.Button(self.button_frame, text="Create User Profile", command = self.openCreateProfilePg, font=("Josefin Sans", 18), width=15, height=4)
        self.button4.grid(row= 1, column = 1)
        
        self.button5 = tk.Button(self.button_frame, text="Manage user profile", command = self.openViewAllAProfilePg, font=("Josefin Sans", 18), width=15, height=4)
        self.button5.grid(row= 0, column = 2)

        
    def openOwnAccountInfoPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        OwnAccountInfoPg(self.root, self.user)

    def openCreateAccountPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        CreateAccountPg(self.root, self.user)
        
    def openViewAllAccPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllAccPg(self.root, self.user)
        
    def openCreateProfilePg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        CreateUserProfilePg(self.root, self.user)
    
    def openViewAllAProfilePg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllProfilePg(self.root, self.user)
        
    def logout(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        LoginPg(self.root)

        
class OwnAccountInfoPg:
    def __init__(self, root, user):
        self.root = root
        self.user = user

        self.displayOwnAccountInfoPg()
    
    def displayOwnAccountInfoPg(self):
        self.ownAccountFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.ownAccountFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #making container frame
        self.container_frame = tk.Frame(self.ownAccountFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Account Information", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        # Display the account information in labels
        rowNum = 0
        for i, (attribute, value) in enumerate(vars(self.user).items()):
            if (attribute == "password"):
                continue
            elif (attribute == "userProfile"):
                value = value.profileName
            elif (attribute == "cafeRole"):
                value = value.roleName
        
            label_text = f"{attribute}: {value}"
            label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
            label.grid(row=i+1, column=0, padx=20, pady=10, sticky="w")
            rowNum += 1
        
        # Show account information frame
        self.ownAccountFrame.pack(fill="both", expand=True)

    def back(self):
        if(self.user.userProfile.profileName == "system_admin"):
            self.ownAccountFrame.pack_forget()
            AdminPg(self.root, self.user)
        elif(self.user.userProfile.profileName == "cafe_owner"):
            self.ownAccountFrame.pack_forget()
            OwnerPg(self.root, self.user)
        elif(self.user.userProfile.profileName == "cafe_manager"):
            self.ownAccountFrame.pack_forget()
            ManagerPg(self.root, self.user)
        elif(self.user.userProfile.profileName == "cafe_staff"):
            self.ownAccountFrame.pack_forget()
            StaffPg(self.root, self.user)
        

    def logout(self):
        self.ownAccountFrame.pack_forget()
        LoginPg(self.root)

#user account starts user account starts user account starts user account starts user account starts
class CreateAccountPg:
    def __init__(self, root, user):
        self.root = root
        self.user = user

        self.createAccountController = controller.CreateUserAccController()
        self.viewAllUserProfileController = controller.ViewAllUserProfileController()

        self.displayCreateAccountPg()

    def displayCreateAccountPg(self):
        self.createAccountFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.createAccountFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #creating continer page
        self.container_frame = tk.Frame(self.createAccountFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Creating Account", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Username label and entry
        self.usernameLabel = tk.Label(self.container_frame, text="Username:", bg="#D3D3D3", fg = "black")
        self.usernameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.usernameEntry = tk.Entry(self.container_frame)
        self.usernameEntry.grid(row=1, column=1, padx=5, pady=5)
    
        # password label and entry
        self.passwordLabel = tk.Label(self.container_frame, text="Password:",bg="#D3D3D3", fg = "black")
        self.passwordLabel.grid(row=2, column=0, padx=5, pady=5)
        self.passwordEntry = tk.Entry(self.container_frame)
        self.passwordEntry.grid(row=2, column=1, padx=5, pady=5)
        
        # full name label and entry
        self.fullNameLabel = tk.Label(self.container_frame, text="Full Name:",bg="#D3D3D3", fg = "black")
        self.fullNameLabel.grid(row=3, column=0, padx=5, pady=5)
        self.fullNameEntry = tk.Entry(self.container_frame)
        self.fullNameEntry.grid(row=3, column=1, padx=5, pady=5)

        # Email label and entry
        self.emailLabel = tk.Label(self.container_frame, text="Email:",bg="#D3D3D3", fg = "black")
        self.emailLabel.grid(row=4, column=0, padx=5, pady=5)
        self.emailEntry = tk.Entry(self.container_frame)
        self.emailEntry.grid(row=4, column=1, padx=5, pady=5)

        # Phone Number label and entry
        self.phoneNumLabel = tk.Label(self.container_frame, text="Phone Number:",bg="#D3D3D3", fg = "black")
        self.phoneNumLabel.grid(row=5, column=0, padx=5, pady=5)
        self.phoneNumEntry = tk.Entry(self.container_frame)
        self.phoneNumEntry.grid(row=5, column=1, padx=5, pady=5)
        
        # Address label and entry
        self.addressLabel = tk.Label(self.container_frame, text="Address:",bg="#D3D3D3", fg = "black")
        self.addressLabel.grid(row=6, column=0, padx=5, pady=5)
        self.addressEntry = tk.Entry(self.container_frame)
        self.addressEntry.grid(row=6, column=1, padx=5, pady=5)

        # Date of Birth label and entry
        self.dobLabel = tk.Label(self.container_frame, text="Date of Birth:",bg="#D3D3D3", fg = "black")
        self.dobLabel.grid(row=7, column=0, padx=5, pady=5)
        self.dobEntry = tk.Entry(self.container_frame)
        self.dobEntry.grid(row=7, column=1, padx=5, pady=5)

         #user profile lable and option
        self.userProfileLabel = tk.Label(self.container_frame, text="User Profile:", bg="#D3D3D3", fg ="black")
        self.userProfileLabel.grid(row=8, column=0, padx=5, pady=5)
        
        options = []
        
        profiles = self.viewAllUserProfileController.viewAllUserProfile()
        
        for profile in profiles:
            if (profile.isSuspended == False):
                options.append(profile.profileName)

        # Create a variable to store the selected value
        self.selected_var = StringVar(root)
        self.selected_var.set(options[0])  # Set the default value

        # Create a dropdown list
        self.dropdown = tk.OptionMenu(self.container_frame, self.selected_var, *options)
        self.dropdown.grid(row=8, column=1, padx=5, pady=5)


        # Create Account button
        self.createAccButton = tk.Button(self.container_frame, text="Create Account", command=self.createAccount)
        self.createAccButton.grid(row=9, column=1, padx=5, pady=5)
        
        self.createAccountFrame.pack(fill = "both", expand = True)
        
    def createAccount(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        fullname = self.fullNameEntry.get()
        email = self.emailEntry.get()
        phoneNum = self.phoneNumEntry.get()
        address = self.addressEntry.get()
        dateOfBirth = self.dobEntry.get()
        profileName = self.selected_var.get()
        
        userAcc = entity.UserAccount(username, password, fullname, email, phoneNum, address, dateOfBirth, entity.UserProfile(profileName))
        result = self.createAccountController.createUserAccount(userAcc)
        if (result):
            messagebox.showinfo("Successful!", "Account Created Successfully!")
        else:
            messagebox.showerror("Failed!", "User Account already existed")
        
    def back(self):
        self.createAccountFrame.pack_forget()
        AdminPg(self.root, self.user)

    def logout(self):
        self.createAccountFrame.pack_forget()
        LoginPg(self.root)
        
class ViewAllAccPg:
    def __init__(self, root, user):
        self.root = root

        self.user = user
        
        self.viewAllUserAccController = controller.ViewAllUserAccController()
        self.updateUserAccController = controller.UpdateUserAccController()
        self.suspendUserAccController = controller.SuspendUserAccController()
        self.searchUserAccController = controller.SearchUserAccController()

        self.displayViewAllAccPg() 

    def displayViewAllAccPg(self):
        self.newFrame = tk.Frame(self.root, bg="#EBDFD3")
        # Creating a header frame
        self.headerFrame = tk.Frame(self.root, bg="#EBDFD3")
        self.headerFrame.pack(side=tk.TOP, fill=tk.X)

        # Adding a search bar to the header frame
        self.searchLabel = tk.Label(self.headerFrame, text="Search Username: ", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
        self.searchLabel.pack(side=tk.LEFT, padx=10, pady=10)

        self.searchEntry = tk.Entry(self.headerFrame, font=("Josefin Sans", 14))
        self.searchEntry.pack(side=tk.LEFT, padx=10, pady=10)

        self.searchButton = tk.Button(self.headerFrame, text="Search", command=self.displaySearchAcc, font=("Josefin Sans", 14))
        self.searchButton.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Calling controller to get a list of users
        accounts = self.viewAllUserAccController.viewAllUserAcc()
        
        self.viewAllAccCanvas = tk.Canvas(self.root,bg="#EBDFD3")
        self.viewAllAccCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.viewAllAccScrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.viewAllAccCanvas.yview)
        self.viewAllAccScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.viewAllAccCanvas.configure(yscrollcommand=self.viewAllAccScrollbar.set)
        
        self.viewAllAccFrame = tk.Frame(self.viewAllAccCanvas, bg="#EBDFD3")
        self.viewAllAccCanvas.create_window((0, 0), window=self.viewAllAccFrame, anchor="nw")

        rowNum = 0
        for account in accounts:
            # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)
            username_label = tk.Label(self.viewAllAccFrame, text=f"Username: {account.username}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            username_label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")

            profile_label = tk.Label(self.viewAllAccFrame, text=f"Profile Name: {account.userProfile.profileName}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            profile_label.grid(row=rowNum, column=1, padx=20, pady=10, sticky="w")
            
            # Add three buttons horizontally
            viewAccButton = tk.Button(self.viewAllAccFrame, text="View", command=lambda user=account: self.openAccountInfoPg(user))
            viewAccButton.grid(row=rowNum, column=2, padx=10)

            updateAccButton = tk.Button(self.viewAllAccFrame, text="Update", command=lambda user=account: self.openUpdateAccPg(user))
            updateAccButton.grid(row=rowNum, column=3, padx=10)

            suspendAccButton = tk.Button(self.viewAllAccFrame, text="Suspend", command=lambda user=account: self.suspendAcc(user))
            suspendAccButton.grid(row=rowNum, column=4, padx=10)
            
            rowNum += 1
        
        backButton = tk.Button(self.viewAllAccFrame, text="Back", command= self.back)
        backButton.grid(row=rowNum, column=0)

        logoutButton = tk.Button(self.viewAllAccFrame, text="Logout", command = self.logout)
        logoutButton.grid(row=rowNum, column=1)
        
        self.viewAllAccFrame.bind("<Configure>", lambda e: self.viewAllAccCanvas.configure(scrollregion=self.viewAllAccCanvas.bbox("all")))

        # Show account information frame
        #self.viewAllAccFrame.pack(padx=50, pady=50)
    
    def displaySearchAcc(self):
        inputUsername = self.searchEntry.get()
        if (inputUsername):
            # Call controller to get the user account
            account = self.searchUserAccController.searchUserAcc(inputUsername)

            if account:
                self.viewAllAccFrame.pack_forget()
                self.viewAllAccCanvas.pack_forget()
                self.viewAllAccScrollbar.pack_forget()
                self.newFrame.pack_forget()
                # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)                
                username_label = tk.Label(self.newFrame, text=f"Username: {account.username}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
                username_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

                profile_label = tk.Label(self.newFrame, text=f"Profile Name: {account.userProfile.profileName}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
                profile_label.grid(row=0, column=1, padx=20, pady=10, sticky="w")
                
                # Add three buttons horizontally
                veiwAccButton = tk.Button(self.newFrame, text="View", command=lambda user=account: self.openAccountInfoPg(user))
                veiwAccButton.grid(row=0, column=2, padx=10)

                updateAccButton = tk.Button(self.newFrame, text="Update", command=lambda user=account: self.openUpdateAccPg(user))
                updateAccButton.grid(row=0, column=3, padx=10)

                suspendAccButton = tk.Button(self.newFrame, text="Suspend", command=lambda user=account: self.suspendAcc(user))
                suspendAccButton.grid(row=0, column=4, padx=10)

                backButton = tk.Button(self.newFrame, text="Back", command= self.back)
                backButton.grid(row=1, column=0)

                logoutButton = tk.Button(self.newFrame, text="Logout", command = self.logout)
                logoutButton.grid(row=1, column=1)
                
                self.newFrame.pack(fill="both", expand=True)
            
                # ViewAccountInfoPg(self.root, userAcc)
            else:
                # Handle the case when the user is not found
                messagebox.showerror("Notice", f"User with username {inputUsername} not found.")

        else:
            # Handle the case when the input is empty
            messagebox.showerror("Notice", "Please enter a username for the search.")
            
    def suspendAcc(self, userAcc):
        if (userAcc.isSuspended):
            messagebox.showinfo("Notice", "Already Suspended!")
        else:
            result = self.suspendUserAccController.suspendUserAcc(userAcc.username)
            if (result):
                messagebox.showinfo("Successful", "Successfully Suspended!")
            
    def openAccountInfoPg(self, userAcc):
        self.viewAllAccFrame.pack_forget()
        self.viewAllAccCanvas.pack_forget()
        self.viewAllAccScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        ViewAccountInfoPg(self.root, self.user, userAcc) 
        
    def openUpdateAccPg(self, userAcc):
        self.viewAllAccFrame.pack_forget()
        self.viewAllAccCanvas.pack_forget()
        self.viewAllAccScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        UpdateAccountPg(self.root, self.user, userAcc)
    
    def back(self):
        self.viewAllAccFrame.pack_forget()
        self.viewAllAccCanvas.pack_forget()
        self.viewAllAccScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        AdminPg(self.root, self.user)

    def logout(self):
        self.viewAllAccFrame.pack_forget()
        self.viewAllAccCanvas.pack_forget()
        self.viewAllAccScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        LoginPg(self.root)


class ViewAccountInfoPg:
    def __init__(self, root, user, userAcc):
        self.root = root
        self.user = user
        self.userAcc = userAcc

        self.displayAccountInfoPg()
    
    def displayAccountInfoPg(self):
        self.ownAccountFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.ownAccountFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #making container frame
        self.container_frame = tk.Frame(self.ownAccountFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Account Information", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Display the account information in labels
        rowNum = 0
        for i, (attribute, value) in enumerate(vars(self.userAcc).items()):
            if (attribute == "password"):
                continue
            elif (attribute == "userProfile"):
                value = value.profileName
            elif (attribute == "cafeRole"):
                value = value.roleName
        
            label_text = f"{attribute}: {value}"
            label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
            label.grid(row=i+1, column=0, padx=20, pady=10, sticky="w")
            rowNum += 1
            label_text = f"{attribute}: {value}"
            label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
            label.grid(row=i + 1, column=0, padx=20, pady=10, sticky="w")
            rowNum += 1
        
        
        # Show account information frame
        self.ownAccountFrame.pack(fill="both", expand=True)

    def back(self):
        
        if(self.user.userProfile.profileName == "system_admin"):
            self.ownAccountFrame.pack_forget()
            ViewAllAccPg(self.root, self.user)
        elif(self.user.userProfile.profileName == "cafe_owner"):
            self.ownAccountFrame.pack_forget()
            OwnerPg(self.root, self.user)
        elif(self.user.userProfile.profileName == "cafe_manager"):
            self.ownAccountFrame.pack_forget()
            ViewAllStaffsPg(self.root, self.user)
        

    def logout(self):
        self.ownAccountFrame.pack_forget()
        LoginPg(self.root)
        
     
class UpdateAccountPg:
    def __init__(self, root, user, userAcc):
        self.root = root
        
        self.user = user
        self.userAcc = userAcc

        self.updateAccountController = controller.UpdateUserAccController()
        self.viewAllUserProfileController = controller.ViewAllUserProfileController()

        self.displayUpdateAccountPg()

    def displayUpdateAccountPg(self):
        self.updateAccountFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.updateAccountFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #creating continer page
        self.container_frame = tk.Frame(self.updateAccountFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Updating Account", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Username label and entry
        self.usernameLabel = tk.Label(self.container_frame, text="Username:", bg="#D3D3D3", fg ="black")
        self.usernameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.usernameEntry = tk.Entry(self.container_frame)
        self.usernameEntry.grid(row=1, column=1, padx=5, pady=5)
        
        # Password label and entry
        self.passwordLabel = tk.Label(self.container_frame, text="Password:", bg="#D3D3D3", fg ="black")
        self.passwordLabel.grid(row=2, column=0, padx=5, pady=5)
        self.passwordEntry = tk.Entry(self.container_frame)
        self.passwordEntry.grid(row=2, column=1, padx=5, pady=5)
        
        # full name label and entry
        self.fullNameLabel = tk.Label(self.container_frame, text="Full Name:",bg="#D3D3D3", fg ="black")
        self.fullNameLabel.grid(row=3, column=0, padx=5, pady=5)
        self.fullNameEntry = tk.Entry(self.container_frame)
        self.fullNameEntry.grid(row=3, column=1, padx=5, pady=5)
        
        # Email label and entry
        self.emailLabel = tk.Label(self.container_frame, text="Email:", bg="#D3D3D3", fg ="black")
        self.emailLabel.grid(row=4, column=0, padx=5, pady=5)
        self.emailEntry = tk.Entry(self.container_frame)
        self.emailEntry.grid(row=4, column=1, padx=5, pady=5)

        # Phone Number label and entry
        self.phoneNumLabel = tk.Label(self.container_frame, text="Phone Number:", bg="#D3D3D3", fg ="black")
        self.phoneNumLabel.grid(row=5, column=0, padx=5, pady=5)
        self.phoneNumEntry = tk.Entry(self.container_frame)
        self.phoneNumEntry.grid(row=5, column=1, padx=5, pady=5)
        
        # Address label and entry
        self.addressLabel = tk.Label(self.container_frame, text="Address:", bg="#D3D3D3", fg = "black")
        self.addressLabel.grid(row=6, column=0, padx=5, pady=5)
        self.addressEntry = tk.Entry(self.container_frame)
        self.addressEntry.grid(row=6, column=1, padx=5, pady=5)

        # Date of Birth label and entry
        self.dobLabel = tk.Label(self.container_frame, text="Date of Birth:", bg="#D3D3D3", fg ="black")
        self.dobLabel.grid(row=7, column=0, padx=5, pady=5)
        self.dobEntry = tk.Entry(self.container_frame)
        self.dobEntry.grid(row=7, column=1, padx=5, pady=5)

        # User Profile label and entry
        self.userProfileLabel = tk.Label(self.container_frame, text="User Profile:", bg="#D3D3D3", fg ="black")
        self.userProfileLabel.grid(row=8, column=0, padx=5, pady=5)
        pfoptions = []
        
        profiles = self.viewAllUserProfileController.viewAllUserProfile()
        
        for profile in profiles:
           pfoptions.append(profile.profileName)

        # Create a variable to store the selected value
        self.selected_pf = StringVar(root)
        self.selected_pf.set(pfoptions[0])  # Set the default value

        # Create a dropdown list
        self.dropdown = tk.OptionMenu(self.container_frame, self.selected_pf, *pfoptions)
        self.dropdown.grid(row=8, column=1, padx=5, pady=5)
        
        
        #is suspended lable and option
        # self.isSuspendedLabel = tk.Label(self.container_frame, text="Is Suspended:", bg="#D3D3D3", fg ="black")
        # self.isSuspendedLabel.grid(row=9, column=0, padx=5, pady=5)
        
        # options = ["true", "false"]

        # # Create a variable to store the selected value
        # self.selected_var = StringVar(root)
        # self.selected_var.set(options[1])  # Set the default value

        # # Create a dropdown list
        # self.dropdown = tk.OptionMenu(self.container_frame, self.selected_var, *options)
        # self.dropdown.grid(row=9, column=1, padx=5, pady=5)

    
        # Create Account button
        self.updateAccButton = tk.Button(self.container_frame, text="Update Account", command=self.updateAccount)
        self.updateAccButton.grid(row=10, column=1, padx=5, pady=5)
        
        self.updateAccountFrame.pack(fill = "both", expand = True)
        
    def updateAccount(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        fullName = self.fullNameEntry.get()
        email = self.emailEntry.get()
        phoneNum = self.phoneNumEntry.get()
        address = self.addressEntry.get()
        dateOfBirth = self.dobEntry.get()
        profileName = self.selected_pf.get()
        # isSuspended = self.selected_var.get()
        
        
        # if (isSuspended.lower() == "true"):
        #     isSuspended = True
        # elif (isSuspended.lower() == "false"):
        #     isSuspended = False
        # else:
        #     messagebox.showerror("Notice", "is_suspended can only be true or false. Please try again.")
        
        
        if (username == ""):
            username = self.userAcc.username 
        if (password == ""):
            password = self.userAcc.password
        if (fullName == ""):
            fullName = self.userAcc.fullName
        if (email == ""):
            email = self.userAcc.email
        if (phoneNum == ""):
            phoneNum = self.userAcc.phoneNumber
        if (address == ""):
            address = self.userAcc.address
        if (dateOfBirth == ""):
            dateOfBirth = self.userAcc.dateOfBirth
        if (profileName == ""):
             profileName = self.userAcc.userProfile.profileName
            
       
        updateAcc = entity.UserAccount(username, password, fullName, email, phoneNum, address, dateOfBirth, entity.UserProfile(profileName))
        result = self.updateAccountController.updateUserAcc(self.userAcc.username, updateAcc)
    
        if (result):
            messagebox.showinfo("Successful!", "Account Updated Successfully!")
        else:
            messagebox.showerror("Failed!", "User Account cannot update")
        
    def back(self):
        self.updateAccountFrame.pack_forget()
        ViewAllAccPg(self.root, self.user)

    def logout(self):
        self.updateAccountFrame.pack_forget()
        LoginPg(self.root)
        
# User Profile starts # User Profile starts # User Profile starts #user profile starts

class CreateUserProfilePg:
    def __init__(self, root, user):
        self.root = root
        

        self.user = user

        self.createUserProfileController = controller.CreateUserProfileController()

        self.displayCreateUserProfilePg()

    def displayCreateUserProfilePg(self):
        self.createProfileFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.createProfileFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #creating continer page
        self.container_frame = tk.Frame(self.createProfileFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Creating Profile", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Username label and entry
        self.profileNameLabel = tk.Label(self.container_frame, text="Profile name:", bg="#D3D3D3", fg = "black")
        self.profileNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.profileNameEntry = tk.Entry(self.container_frame)
        self.profileNameEntry.grid(row=1, column=1, padx=5, pady=5)
    
        # password label and entry
        self.descriptionLabel = tk.Label(self.container_frame, text="Description:",bg="#D3D3D3", fg = "black")
        self.descriptionLabel.grid(row=2, column=0, padx=5, pady=5)
        self.descriptionEntry = tk.Text(self.container_frame, height = 10, width = 26)
        self.descriptionEntry.grid(row=2, column=1, padx=5, pady=5)
        
        # Create Account button
        self.createAccButton = tk.Button(self.container_frame, text="Create User Profile", command=self.createProfile, bg="#D3D3D3")
        self.createAccButton.grid(row=6, column=1, padx=5, pady=5)
        
        self.createProfileFrame.pack(fill = "both", expand = True)
        
    def createProfile(self):
        profileName = self.profileNameEntry.get()
        description = self.descriptionEntry.get("1.0", "end-1c")
        
        userProfile = entity.UserProfile(profileName, description)
        result = self.createUserProfileController.createUserProfile(userProfile)
        if (result):
            messagebox.showinfo("Successful!", "Profile Created Successfully!")
        else:
            messagebox.showerror("Failed!", "User Profile already existed")
        
    def back(self):
        self.createProfileFrame.pack_forget()
        AdminPg(self.root, self.user)

    def logout(self):
        self.createProfileFrame.pack_forget()
        LoginPg(self.root)

class ViewAllProfilePg:
    def __init__(self, root, user):
        self.root = root
    
        self.user = user
        
        self.viewAllUserProfileController = controller.ViewAllUserProfileController()
        self.updateUserProfileController = controller.UpdateUserProfileController()
        self.suspendUserProfileController = controller.SuspendUserProfileController()
        self.searchUserProfileController = controller.SearchUserProfileController()

        self.displayViewAllProfilePg() 

    def displayViewAllProfilePg(self):
        self.newFrame = tk.Frame(self.root, bg="#EBDFD3")
        # Creating a header frame
        self.headerFrame = tk.Frame(self.root, bg="#EBDFD3")
        self.headerFrame.pack(side=tk.TOP, fill=tk.X)

        # Adding a search bar to the header frame
        self.searchLabel = tk.Label(self.headerFrame, text="Search User Profile: ", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
        self.searchLabel.pack(side=tk.LEFT, padx=10, pady=10)

        self.searchEntry = tk.Entry(self.headerFrame, font=("Josefin Sans", 14))
        self.searchEntry.pack(side=tk.LEFT, padx=10, pady=10)

        self.searchButton = tk.Button(self.headerFrame, text="Search", command=self.displaySearchProfile, font=("Josefin Sans", 14))
        self.searchButton.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Calling controller to get a list of users
        profiles = self.viewAllUserProfileController.viewAllUserProfile()
        
        self.viewAllProfileCanvas = tk.Canvas(self.root,bg="#EBDFD3")
        self.viewAllProfileCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.viewAllProfileScrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.viewAllProfileCanvas.yview)
        self.viewAllProfileScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.viewAllProfileCanvas.configure(yscrollcommand=self.viewAllProfileScrollbar.set)
        
        self.viewAllProfileFrame = tk.Frame(self.viewAllProfileCanvas, bg="#EBDFD3")
        self.viewAllProfileCanvas.create_window((0, 0), window=self.viewAllProfileFrame, anchor="nw")

        rowNum = 0
        for profile in profiles:
            # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)
            username_label = tk.Label(self.viewAllProfileFrame, text=f"Profile Name: {profile.profileName}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            username_label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")

            # Add three buttons horizontally
            viewAccButton = tk.Button(self.viewAllProfileFrame, text="View", command=lambda user=profile: self.openProfileInfoPg(user))
            viewAccButton.grid(row=rowNum, column=2, padx=10)

            updateAccButton = tk.Button(self.viewAllProfileFrame, text="Update", command=lambda user=profile: self.openUpdateProfilePg(user))
            updateAccButton.grid(row=rowNum, column=3, padx=10)

            suspendAccButton = tk.Button(self.viewAllProfileFrame, text="Suspend", command=lambda user=profile: self.suspendProfile(user))
            suspendAccButton.grid(row=rowNum, column=4, padx=10)
            
            rowNum += 1
        
        backButton = tk.Button(self.viewAllProfileFrame, text="Back", command= self.back)
        backButton.grid(row=rowNum, column=0)

        logoutButton = tk.Button(self.viewAllProfileFrame, text="Logout", command = self.logout)
        logoutButton.grid(row=rowNum, column=1)
        
        self.viewAllProfileFrame.bind("<Configure>", lambda e: self.viewAllProfileCanvas.configure(scrollregion=self.viewAllProfileCanvas.bbox("all")))

        # Show account information frame
        #self.viewAllAccFrame.pack(padx=50, pady=50)
    
    def displaySearchProfile(self):
        inputProfilename = self.searchEntry.get()
        if (inputProfilename):
            # Call controller to get the user account
            profile = self.searchUserProfileController.searchUserProfile(inputProfilename)

            if profile:
                self.viewAllProfileFrame.pack_forget()
                self.viewAllProfileCanvas.pack_forget()
                self.viewAllProfileScrollbar.pack_forget()
                self.newFrame.pack_forget()
                # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)                
                username_label = tk.Label(self.newFrame, text=f"Profile Name: {profile.profileName}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
                username_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
                
                # Add three buttons horizontally
                veiwAccButton = tk.Button(self.newFrame, text="View", command=lambda user=profile: self.openProfileInfoPg(user))
                veiwAccButton.grid(row=0, column=2, padx=10)

                updateAccButton = tk.Button(self.newFrame, text="Update", command=lambda user=profile: self.openUpdateProfilePg(user))
                updateAccButton.grid(row=0, column=3, padx=10)

                suspendAccButton = tk.Button(self.newFrame, text="Suspend", command=lambda user=profile: self.suspendProfile(user))
                suspendAccButton.grid(row=0, column=4, padx=10)

                backButton = tk.Button(self.newFrame, text="Back", command= self.back)
                backButton.grid(row=1, column=0)

                logoutButton = tk.Button(self.newFrame, text="Logout", command = self.logout)
                logoutButton.grid(row=1, column=1)

                self.newFrame.pack(fill="both", expand=True)
            
                # ViewAccountInfoPg(self.root, userAcc)
            else:
                # Handle the case when the user is not found
                messagebox.showerror("Notice", f"UserProfile with profile name {inputProfilename} not found.")
            
            

        else:
            # Handle the case when the input is empty
            messagebox.showerror("Notice", "Please enter a profile name for the search.")
            
    def suspendProfile(self, userPf):
        if (userPf.isSuspended):
            messagebox.showinfo("Notice", "Already Suspended!")
        else:
            result = self.suspendUserProfileController.suspendUserProfile(userPf.profileName)
            if (result):
                messagebox.showinfo("Successful", "Successfully Suspended!")
            else:
                messagebox.showerror("Notice", "Cannot Suspend! Profile is already Suspended!")
            
            
    def openProfileInfoPg(self, userAcc):
        self.viewAllProfileFrame.pack_forget()
        self.viewAllProfileCanvas.pack_forget()
        self.viewAllProfileScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        ViewProfileInfoPg(self.root, self.user, userAcc) 
        
    def openUpdateProfilePg(self, userAcc):
        self.viewAllProfileFrame.pack_forget()
        self.viewAllProfileCanvas.pack_forget()
        self.viewAllProfileScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        UpdateProfilePg(self.root, self.user, userAcc)
    
    def back(self):
        self.viewAllProfileFrame.pack_forget()
        self.viewAllProfileCanvas.pack_forget()
        self.viewAllProfileScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        AdminPg(self.root, self.user)

    def logout(self):
        self.viewAllProfileFrame.pack_forget()
        self.viewAllProfileCanvas.pack_forget()
        self.viewAllProfileScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        LoginPg(self.root)


class ViewProfileInfoPg:
    def __init__(self, root, user, userAcc):
        self.root = root
        self.user = user
        self.userAcc = userAcc

        self.displayProfileInfoPg()
    
    def displayProfileInfoPg(self):
        self.ownAccountFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.ownAccountFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #making container frame
        self.container_frame = tk.Frame(self.ownAccountFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Profile Information", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Display the account information in labels
        rowNum = 0
        for i, (attribute, value) in enumerate(vars(self.userAcc).items()):
            if (attribute == "password"):
                continue
            label_text = f"{attribute}: {value}"
            label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
            label.grid(row=i + 1, column=0, padx=20, pady=10, sticky="w")
            rowNum += 1
        
        
        # Show account information frame
        self.ownAccountFrame.pack(fill="both", expand=True)

    def back(self):
        self.ownAccountFrame.pack_forget()
        ViewAllProfilePg(self.root, self.user)

    def logout(self):
        self.ownAccountFrame.pack_forget()
        LoginPg(self.root)
        
        
class UpdateProfilePg:
    def __init__(self, root, user, userAcc):
        self.root = root
        

        self.user = user
        self.userAcc = userAcc

        self.updateProfileController = controller.UpdateUserProfileController()

        self.displayUpdateProfilePg()

    def displayUpdateProfilePg(self):
        self.updateProfileFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.updateProfileFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #creating continer page
        self.container_frame = tk.Frame(self.updateProfileFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Updating Profile", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Username label and entry
        self.profileNameLabel = tk.Label(self.container_frame, text="Profile Name:", bg="#D3D3D3", fg = "black")
        self.profileNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.profileNameEntry = tk.Entry(self.container_frame)
        self.profileNameEntry.grid(row=1, column=1, padx=5, pady=5)
    
        # password label and entry
        self.descriptionLabel = tk.Label(self.container_frame, text="Description:",bg="#D3D3D3", fg = "black")
        self.descriptionLabel.grid(row=2, column=0, padx=5, pady=5)
        self.descriptionEntry = tk.Text(self.container_frame, height = 10, width = 26)
        self.descriptionEntry.grid(row=2, column=1, padx=5, pady=5)
        
        #is suspended lable and option
        # self.isSuspendedLabel = tk.Label(self.container_frame, text="Is Suspended:", bg="#D3D3D3", fg ="black")
        # self.isSuspendedLabel.grid(row=5, column=0, padx=5, pady=5)
        
        # options = ["true", "false"]

        # # Create a variable to store the selected value
        # self.selected_var = StringVar(root)
        # self.selected_var.set(options[1])  # Set the default value

        # # Create a dropdown list
        # self.dropdown = tk.OptionMenu(self.container_frame, self.selected_var, *options)
        # self.dropdown.grid(row=5, column=1, padx=5, pady=5)
        

        # Create profile button
        self.createAccButton = tk.Button(self.container_frame, text="Update User Profile", command=self.updateProfile, bg="#D3D3D3")
        self.createAccButton.grid(row=6, column=1, padx=5, pady=5)
        
        self.updateProfileFrame.pack(fill = "both", expand = True)
        
    def updateProfile(self):
        profileName = self.profileNameEntry.get()
        description = self.descriptionEntry.get("1.0", "end-1c")
        # isSuspended = self.selected_var.get()
        
        # if (isSuspended.lower() == "true"):
        #     isSuspended = True
        # elif (isSuspended.lower() == "false"):
        #     isSuspended = False
        
        if (profileName == ""):
            profileName = self.userAcc.profileName
        if (description == ""):
            description = self.userAcc.description
        
            

        updatePf = entity.UserProfile(profileName, description)
        result = self.updateProfileController.updateUserProfile(self.userAcc.profileName, updatePf)
    
        if (result):
            messagebox.showinfo("Successful!", "Profile Updated Successfully!")
        else:
            messagebox.showerror("Failed!", "User Profile cannot update")
        
    def back(self):
        self.updateProfileFrame.pack_forget()
        ViewAllProfilePg(self.root, self.user)

    def logout(self):
        self.updateProfileFrame.pack_forget()
        LoginPg(self.root)
        
#cafe owner starts #cafe owner starts #cafe owner starts #cafe owner starts #cafe owner starts

class OwnerPg():
    def __init__(self, root, user):
        self.loginController = controller.LoginController()
        self.root = root
        self.user = user

        self.displayOwnerPg()

    def displayOwnerPg(self):
        # Display welcome label
        self.mainLabel = tk.Label(self.root, text="Welcome to the Owner Page")
        self.mainLabel.pack(fill="both", expand=True)

        
        #creating owner main frame
        self.ownerFrame = tk.Frame(self.root, bg="#EBDFD3")
        self.ownerFrame.pack(fill="both", expand=True)
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.ownerFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)
        

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        self.logoutButton = tk.Button(self.sidebar, text="Logout", command=self.logout)
        self.logoutButton.pack(pady=(520, 0))

        # Create the main content area
        self.main_content = tk.Frame(self.ownerFrame, width=1400, height=800, bg="#EBDFD3")
        self.main_content.grid(row=0, column=1)

        # Add a welcome message
        self.welcome_label = tk.Label(self.main_content, text="Welcome Cafe Owner!", font=("Josefin Sans", 30), bg="#EBDFD3", fg = "black")
        self.welcome_label.pack(pady=55)

        # Create function buttons
        self.function_buttons = tk.Frame(self.main_content, bg="#EBDFD3")
        self.function_buttons.pack()
        
        self.function_buttons = tk.Frame(self.main_content, bg="#EBDFD3")
        self.function_buttons.pack()
        
        self.button_frame = tk.Frame(self.function_buttons, bg="#EBDFD3")
        self.button_frame.pack(side="left", padx=40, pady=40)


        # Add four buttons
        self.button1 = tk.Button(self.button_frame, text="View Own Account", command=self.openOwnAccountInfoPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button1.grid(row= 0, column = 0)

        self.button2 = tk.Button(self.button_frame, text="Create Work Slots", command=self.openCreateWorkSlotPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button2.grid(row= 0, column = 1)

        self.button3 = tk.Button(self.button_frame, text="Manage Work Slots", command= self.openViewAllWSPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button3.grid(row= 0, column = 2)

        
    def openOwnAccountInfoPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.ownerFrame.pack_forget()
        OwnAccountInfoPg(self.root, self.user)

    def openCreateWorkSlotPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.ownerFrame.pack_forget()
        CreateWorkSlotPg(self.root, self.user)
        
    def openViewAllWSPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.ownerFrame.pack_forget()
        ViewAllWorkSlotsPg(self.root, self.user)
        
    def openCreateProfilePg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.ownerFrame.pack_forget()
        CreateUserProfilePg(self.root, self.user)
    
    def openViewAllAProfilePg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.ownerFrame.pack_forget()
        ViewAllProfilePg(self.root, self.user)
        
    def logout(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.ownerFrame.pack_forget()
        LoginPg(self.root)


class CreateWorkSlotPg:
    def __init__(self, root, user):
        self.root = root

        self.user = user

        self.createWorkSlotController = controller.CreateWorkSlotController()

        self.displayCreateWorkSlotPg()

    def displayCreateWorkSlotPg(self):
        self.createWSFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.createWSFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #creating continer page
        self.container_frame = tk.Frame(self.createWSFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Creating Work Slot", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # location label and entry
        self.locationLabel = tk.Label(self.container_frame, text="Location:", bg="#D3D3D3", fg = "black")
        self.locationLabel.grid(row=1, column=0, padx=5, pady=5)
        self.locationEntry = tk.Entry(self.container_frame)
        self.locationEntry.grid(row=1, column=1, padx=5, pady=5)
    
        # date label and entry
        self.dateLabel = tk.Label(self.container_frame, text="Date:",bg="#D3D3D3", fg = "black")
        self.dateLabel.grid(row=2, column=0, padx=5, pady=5)
        self.dateEntry = tk.Entry(self.container_frame)
        self.dateEntry.grid(row=2, column=1, padx=5, pady=5)
        
        #start time
        self.startTimeLabel = tk.Label(self.container_frame, text="Start Time:",bg="#D3D3D3", fg = "black")
        self.startTimeLabel.grid(row=3, column=0, padx=5, pady=5)
        self.startTimeEntry = tk.Entry(self.container_frame)
        self.startTimeEntry.grid(row=3, column=1, padx=5, pady=5)
        
        # end time
        self.endTimeLabel = tk.Label(self.container_frame, text="End Time:",bg="#D3D3D3", fg = "black")
        self.endTimeLabel.grid(row=4, column=0, padx=5, pady=5)
        self.endTimeEntry = tk.Entry(self.container_frame)
        self.endTimeEntry.grid(row=4, column=1, padx=5, pady=5)
        
        
        self.chefLabel = tk.Label(self.container_frame, text="Chef:",bg="#D3D3D3", fg = "black")
        self.chefLabel.grid(row=5, column=0, padx=5, pady=5)
        self.chefEntry = tk.Entry(self.container_frame)
        self.chefEntry.grid(row=5, column=1, padx=5, pady=5)
        
        
        self.cashierLabel = tk.Label(self.container_frame, text="Cashier:",bg="#D3D3D3", fg = "black")
        self.cashierLabel.grid(row=6, column=0, padx=5, pady=5)
        self.cashierEntry = tk.Entry(self.container_frame)
        self.cashierEntry.grid(row=6, column=1, padx=5, pady=5)
        
        
        self.waiterLabel = tk.Label(self.container_frame, text="Waiter:",bg="#D3D3D3", fg = "black")
        self.waiterLabel.grid(row=7, column=0, padx=5, pady=5)
        self.waiterEntry = tk.Entry(self.container_frame)
        self.waiterEntry.grid(row=7, column=1, padx=5, pady=5)
        
        
        # Create Account button
        self.createAccButton = tk.Button(self.container_frame, text="Create Work Slot", command=self.createWorkSlot, bg="#D3D3D3")
        self.createAccButton.grid(row=8, column=1, padx=5, pady=5)
        
        self.createWSFrame.pack(fill = "both", expand = True)
        
    def createWorkSlot(self):
        location = self.locationEntry.get()
        date = self.dateEntry.get()
        startTime = self.startTimeEntry.get()
        endTime = self.endTimeEntry.get()
        chef = self.chefEntry.get()
        cashier = self.cashierEntry.get()
        waiter = self.cashierEntry.get()
        roleAssignment1 = entity.RoleAssignment(entity.CafeRole("chef"), chef)
        roleAssignment2 = entity.RoleAssignment(entity.CafeRole("cashier"), cashier)
        roleAssignment3 = entity.RoleAssignment(entity.CafeRole("waiter"), waiter)
        roleAssignments = [roleAssignment1, roleAssignment2, roleAssignment3]
        workSlot = entity.WorkSlot(location=location, date=date, startTime=startTime, endTime=endTime, roleAssignments=roleAssignments)
        result = self.createWorkSlotController.createWorkSlot(workSlot)
        if (result):
            messagebox.showinfo("Successful!", "Work slot Created Successfully!")
        else:
            messagebox.showerror("Failed!", "Work slot already existed")
        
    def back(self):
        self.createWSFrame.pack_forget()
        OwnerPg(self.root, self.user)

    def logout(self):
        self.createWSFrame.pack_forget()
        LoginPg(self.root)

class ViewAllWorkSlotsPg:
    def __init__(self, root, user):
        self.root = root
        

        self.user = user
        
        self.viewAllWorkSlotsController = controller.ViewAllWorkSlotsController()
        self.updateWorkSlotController = controller.UpdateWorkSlotController()
        self.deleteWorkSlotController = controller.DeleteWorkSlotController()
        self.searchWorkSlotController = controller.SearchWorkSlotController()
        self.createBidController = controller.CreateBidController()

        self.displayViewAllWorkSlotsPg() 

    def displayViewAllWorkSlotsPg(self):
        self.newFrame = tk.Frame(self.root, bg="#EBDFD3")
        # Creating a header frame
        self.headerFrame = tk.Frame(self.root, bg="#EBDFD3")
        self.headerFrame.pack(side=tk.TOP, fill=tk.X)

        # Adding a search bar to the header frame
        self.searchLabel = tk.Label(self.headerFrame, text="Search by WorkSlot ID: ", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
        self.searchLabel.pack(side=tk.LEFT, padx=10, pady=10)

        self.searchEntry = tk.Entry(self.headerFrame, font=("Josefin Sans", 14))
        self.searchEntry.pack(side=tk.LEFT, padx=10, pady=10)

        self.searchButton = tk.Button(self.headerFrame, text="Search", command=self.displaySearchWorkSlot, font=("Josefin Sans", 14))
        self.searchButton.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Calling controller to get a list of users
        slots = self.viewAllWorkSlotsController.viewAllWorkSlots()
        
        self.viewAllWSCanvas = tk.Canvas(self.root,bg="#EBDFD3")
        self.viewAllWSCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.viewAllWSScrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.viewAllWSCanvas.yview)
        self.viewAllWSScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.viewAllWSCanvas.configure(yscrollcommand=self.viewAllWSScrollbar.set)
        
        self.viewAllWSFrame = tk.Frame(self.viewAllWSCanvas, bg="#EBDFD3")
        self.viewAllWSCanvas.create_window((0, 0), window=self.viewAllWSFrame, anchor="nw")

        rowNum = 0
        for slot in slots:
            # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)
        
            location_label = tk.Label(self.viewAllWSFrame, text=f"Location: {slot.location}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            location_label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
            
            date_label = tk.Label(self.viewAllWSFrame, text=f"Date: {slot.date}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            date_label.grid(row=rowNum, column=1, padx=20, pady=10, sticky="w")

            
            if (self.user.userProfile.profileName == "cafe_staff"):
                bidButton = tk.Button(self.viewAllWSFrame, text="Bid", command=lambda user=slot: self.createBid(user))
                bidButton.grid(row=rowNum, column=3, padx=10)
            elif (self.user.userProfile.profileName == "cafe_owner"):
                updateAccButton = tk.Button(self.viewAllWSFrame, text="Update", command=lambda user=slot: self.openUpdateWSPg(user))
                updateAccButton.grid(row=rowNum, column=3, padx=10)

                suspendAccButton = tk.Button(self.viewAllWSFrame, text="Delete", command=lambda user=slot: self.deleteWorkSlot(user))
                suspendAccButton.grid(row=rowNum, column=4, padx=10)
                
            # Add three buttons horizontally
            viewAccButton = tk.Button(self.viewAllWSFrame, text="View", command=lambda user=slot: self.openWSInfoPg(user))
            viewAccButton.grid(row=rowNum, column=2, padx=10)
            
            rowNum += 1
        
        backButton = tk.Button(self.viewAllWSFrame, text="Back", command= self.back)
        backButton.grid(row=rowNum, column=0)

        logoutButton = tk.Button(self.viewAllWSFrame, text="Logout", command = self.logout)
        logoutButton.grid(row=rowNum, column=1)
        
        self.viewAllWSFrame.bind("<Configure>", lambda e: self.viewAllWSCanvas.configure(scrollregion=self.viewAllWSCanvas.bbox("all")))

        # Show account information frame
        #self.viewAllAccFrame.pack(padx=50, pady=50)
    
    def displaySearchWorkSlot(self):
        inputWS = self.searchEntry.get()
        if (inputWS):
            # Call controller to get the user account
            slot = self.searchWorkSlotController.searchWorkSlot(inputWS)
            if slot:
                self.viewAllWSFrame.pack_forget()
                self.viewAllWSCanvas.pack_forget()
                self.viewAllWSScrollbar.pack_forget()
                self.newFrame.pack_forget()
                # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)                
                username_label = tk.Label(self.newFrame, text=f"Location: {slot.location}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
                username_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
                
                date_label = tk.Label(self.newFrame, text=f"Date: {slot.date}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
                date_label.grid(row=0, column=1, padx=20, pady=10, sticky="w")

                # Add three buttons horizontally
                viewWSButton = tk.Button(self.newFrame, text="View", command=lambda user=slot: self.openWSInfoPg(user))
                viewWSButton.grid(row=0, column=2, padx=10)

                if (self.user.userProfile.profileName == "cafe_staff"):
                    bidButton = tk.Button(self.newFrame, text="Bid", command=lambda user=slot: self.createBid(user))
                    bidButton.grid(row=0, column=3, padx=10)
                elif (self.user.userProfile.profileName == "cafe_owner"):
                    updateAccButton = tk.Button(self.newFrame, text="Update", command=lambda user=slot: self.openUpdateWSPg(user))
                    updateAccButton.grid(row=0, column=3, padx=10)

                    suspendAccButton = tk.Button(self.newFrame, text="Delete", command=lambda user=slot: self.deleteWorkSlot(user))
                    suspendAccButton.grid(row=0, column=4, padx=10)

                backButton = tk.Button(self.newFrame, text="Back", command= self.back)
                backButton.grid(row=1, column=0)

                logoutButton = tk.Button(self.newFrame, text="Logout", command = self.logout)
                logoutButton.grid(row=1, column=1)
            
                self.newFrame.pack(fill="both", expand=True)
                    
            else:
                # Handle the case when the user is not found
                messagebox.showerror("Notice", f"Work Slot with this work slot ID {inputWS} not found.")
                
        else:
            # Handle the case when the input is empty
            messagebox.showerror("Notice", "Please enter a work slot id for the search.")
            
    def deleteWorkSlot(self, workslot):
        if (workslot.workSlotId):
            result = self.deleteWorkSlotController.deleteWorkSlot(workslot.workSlotId)
            if (result):
                messagebox.showinfo("Successful", "Successfully Deleted!")
                self.viewAllWSFrame.pack_forget()
                self.viewAllWSCanvas.pack_forget()
                self.viewAllWSScrollbar.pack_forget()
                self.headerFrame.pack_forget()
                self.newFrame.pack_forget()
                self.displayViewAllWorkSlotsPg()
            
        else:
            messagebox.showinfo("Notice", "Already deleted!")
            
    def createBid(self, workSlot):
        bid = entity.Bid(workSlot, self.user)
        result = self.createBidController.createBid(bid)
        if(result):
            messagebox.showinfo("Successful", "You have successfully submitted a bid!")
        else:
            messagebox.showerror("Error","Bid failed")
            
        
            
    def openWSInfoPg(self, userAcc):
        self.viewAllWSFrame.pack_forget()
        self.viewAllWSCanvas.pack_forget()
        self.viewAllWSScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        ViewWSInfoPg(self.root, self.user, userAcc) 
        
    def openUpdateWSPg(self, userAcc):
        self.viewAllWSFrame.pack_forget()
        self.viewAllWSCanvas.pack_forget()
        self.viewAllWSScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        UpdateWSPg(self.root, self.user, userAcc)
    
    def back(self):
        if (self.user.userProfile.profileName == "cafe_owner"):
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
            self.headerFrame.pack_forget()
            self.newFrame.pack_forget()
            OwnerPg(self.root, self.user)
        elif (self.user.userProfile.profileName == "cafe_staff"):
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
            self.headerFrame.pack_forget()
            self.newFrame.pack_forget()
            StaffPg(self.root, self.user)
        elif(self.user.userProfile.profileName == "cafe_manager"):
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
            self.headerFrame.pack_forget()
            self.newFrame.pack_forget()
            ManagerPg(self.root, self.user)

    def logout(self):
        self.viewAllWSFrame.pack_forget()
        self.viewAllWSCanvas.pack_forget()
        self.viewAllWSScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        LoginPg(self.root)    

class ViewWSInfoPg:
    def __init__(self, root, user, workslot):
        self.root = root
        self.user = user
        self.workslot = workslot

        self.displayWSInfoPg()
    
    def displayWSInfoPg(self):
        self.ownAccountFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.ownAccountFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #making container frame
        self.container_frame = tk.Frame(self.ownAccountFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Work Slot Information", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Display the account information in labels
        rowNum = 1
        for i, (attribute, value) in enumerate(vars(self.workslot).items()):
            if (attribute == "roleAssignments"):
                for assignment in value:
                    label_text = f"{assignment.role.roleName}: {assignment.numOfStaff}"
                    label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                    label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
                    rowNum += 1
                    # label_text += f"\n    {assignment.role.roleName}: {assignment.noOfStaff}"
            else:
                label_text = f"{attribute}: {value}"
                label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
                rowNum += 1
            
           
        # Show account information frame
        self.ownAccountFrame.pack(fill="both", expand=True)

    def back(self):
        self.ownAccountFrame.pack_forget()
        ViewAllWorkSlotsPg(self.root, self.user)

    def logout(self):
        self.ownAccountFrame.pack_forget()
        LoginPg(self.root)
        
class UpdateWSPg:
    def __init__(self, root, user, workslot):
        self.root = root
        

        self.user = user
        self.workslot = workslot

        self.updateWorkSlotController = controller.UpdateWorkSlotController()

        self.displayUpdateWSPg()

    def displayUpdateWSPg(self):
        self.updateProfileFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.updateProfileFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #creating continer page
        self.container_frame = tk.Frame(self.updateProfileFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Updating Work Slot", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # location label and entry
        self.locationLabel = tk.Label(self.container_frame, text="Location:", bg="#D3D3D3", fg = "black")
        self.locationLabel.grid(row=1, column=0, padx=5, pady=5)
        self.locationEntry = tk.Entry(self.container_frame)
        self.locationEntry.grid(row=1, column=1, padx=5, pady=5)
    
        # date label and entry
        self.dateLabel = tk.Label(self.container_frame, text="Date:",bg="#D3D3D3", fg = "black")
        self.dateLabel.grid(row=2, column=0, padx=5, pady=5)
        self.dateEntry = tk.Entry(self.container_frame)
        self.dateEntry.grid(row=2, column=1, padx=5, pady=5)
        
        #start time
        self.startTimeLabel = tk.Label(self.container_frame, text="Start Time:",bg="#D3D3D3", fg = "black")
        self.startTimeLabel.grid(row=3, column=0, padx=5, pady=5)
        self.startTimeEntry = tk.Entry(self.container_frame)
        self.startTimeEntry.grid(row=3, column=1, padx=5, pady=5)
        
        # end time
        self.endTimeLabel = tk.Label(self.container_frame, text="End Time:",bg="#D3D3D3", fg = "black")
        self.endTimeLabel.grid(row=4, column=0, padx=5, pady=5)
        self.endTimeEntry = tk.Entry(self.container_frame)
        self.endTimeEntry.grid(row=4, column=1, padx=5, pady=5)
        
        
        self.chefLabel = tk.Label(self.container_frame, text="Chef:",bg="#D3D3D3", fg = "black")
        self.chefLabel.grid(row=5, column=0, padx=5, pady=5)
        self.chefEntry = tk.Entry(self.container_frame)
        self.chefEntry.grid(row=5, column=1, padx=5, pady=5)
        
        
        self.cashierLabel = tk.Label(self.container_frame, text="Cashier:",bg="#D3D3D3", fg = "black")
        self.cashierLabel.grid(row=6, column=0, padx=5, pady=5)
        self.cashierEntry = tk.Entry(self.container_frame)
        self.cashierEntry.grid(row=6, column=1, padx=5, pady=5)
        
        
        self.waiterLabel = tk.Label(self.container_frame, text="Waiter:",bg="#D3D3D3", fg = "black")
        self.waiterLabel.grid(row=7, column=0, padx=5, pady=5)
        self.waiterEntry = tk.Entry(self.container_frame)
        self.waiterEntry.grid(row=7, column=1, padx=5, pady=5)
        
        
        # Create Account button
        self.createAccButton = tk.Button(self.container_frame, text="Update Work Slot", command=self.updateWorkSlot, bg="#D3D3D3")
        self.createAccButton.grid(row=8, column=1, padx=5, pady=5)
        
        self.updateProfileFrame.pack(fill = "both", expand = True)
        
    def updateWorkSlot(self):
        location = self.locationEntry.get()
        date = self.dateEntry.get()
        startTime = self.startTimeEntry.get()
        endTime = self.endTimeEntry.get()
        chef = self.chefEntry.get()
        cashier = self.cashierEntry.get()
        waiter = self.cashierEntry.get()
        
        if (location == ""):
            location = self.workslot.location 
        if (date == ""):
            date = self.workslot.date
        if (startTime == ""):
            startTime = self.workslot.startTime
        if (endTime == ""):
            endTime = self.workslot.endTime
        if (chef == ""):
            chef = self.workslot.roleAssignments[0].numOfStaff
        if (cashier == ""):
            cashier = self.workslot.roleAssignments[1].numOfStaff
        if (waiter == ""):
            waiter = self.workslot.roleAssignments[2].numOfStaff
        
        roleAssignment1 = entity.RoleAssignment(entity.CafeRole("chef"), chef)
        roleAssignment2 = entity.RoleAssignment(entity.CafeRole("cashier"), cashier)
        roleAssignment3 = entity.RoleAssignment(entity.CafeRole("waiter"), waiter)
        roleAssignments = [roleAssignment1, roleAssignment2, roleAssignment3]
        
        workSlot = entity.WorkSlot(workSlotId=self.workslot.workSlotId, location=location, date=date, startTime=startTime, endTime=endTime, roleAssignments=roleAssignments)
        result = self.updateWorkSlotController.updateWorkSlot(workSlot)
        
        if (result):
            messagebox.showinfo("Successful!", "Work slot Updated Successfully!")
        else:
            messagebox.showerror("Failed!", "Work slot update failed")
        
    def back(self):
        self.updateProfileFrame.pack_forget()
        ViewAllWorkSlotsPg(self.root, self.user)

    def logout(self):
        self.updateProfileFrame.pack_forget()
        LoginPg(self.root)

#cafe manager starts #cafe manager starts #cafe manager starts #cafe manager starts

class ManagerPg():
    def __init__(self, root, user):
        self.loginController = controller.LoginController()
        self.root = root
        self.user = user

        self.displayManagerPg()

    def displayManagerPg(self):
        # Display welcome label
        self.mainLabel = tk.Label(self.root, text="Welcome to the Manager Page")
        self.mainLabel.pack(fill="both", expand=True)

        
        #creating admin main frame
        self.adminFrame = tk.Frame(self.root, bg="#EBDFD3")
        self.adminFrame.pack(fill="both", expand=True)
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.adminFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)
        

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        self.logoutButton = tk.Button(self.sidebar, text="Logout", command=self.logout)
        self.logoutButton.pack(pady=(520, 0))

        # Create the main content area
        self.main_content = tk.Frame(self.adminFrame, width=1400, height=800, bg="#EBDFD3")
        self.main_content.grid(row=0, column=1)

        # Add a welcome message
        self.welcome_label = tk.Label(self.main_content, text="Welcome Manager!", font=("Josefin Sans", 30), bg="#EBDFD3", fg = "black")
        self.welcome_label.pack(pady=55)

        # Create function buttons
        self.function_buttons = tk.Frame(self.main_content, bg="#EBDFD3")
        self.function_buttons.pack()
        
        self.function_buttons = tk.Frame(self.main_content, bg="#EBDFD3")
        self.function_buttons.pack()
        
        self.button_frame = tk.Frame(self.function_buttons, bg="#EBDFD3")
        self.button_frame.pack(side="left", padx=40, pady=40)


        # Add buttons
        self.button1 = tk.Button(self.button_frame, text="View Own Account", command=self.openOwnAccountInfoPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button1.grid(row= 0, column = 0)

        self.button2 = tk.Button(self.button_frame, text="View All Bids", command=self.openViewAllBidsPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button2.grid(row= 0, column = 1)

        self.button3 = tk.Button(self.button_frame, text="View All Staffs", command= self.openViewAllStaffsPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button3.grid(row= 1, column = 0)

        self.button4 = tk.Button(self.button_frame, text="View All Work Slots", command = self.openViewAllWorkSlotPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button4.grid(row= 1, column = 1)
        
        self.button5 = tk.Button(self.button_frame, text="View Work Assignments", command = self.openViewAllWorkAssignmentsPg, font=("Josefin Sans", 18), width=15, height=4)
        self.button5.grid(row= 0, column = 2)

        
    def openOwnAccountInfoPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        OwnAccountInfoPg(self.root, self.user)

    def openViewAllBidsPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllBidsPg(self.root, self.user)
        
    def openViewAllStaffsPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllStaffsPg(self.root, self.user)
        
    def openViewAllWorkAssignmentsPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllWorkAssignmentsPg(self.root, self.user)
    
    def openViewAllWorkSlotPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllWorkSlotsPg(self.root, self.user)
        
    def logout(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        LoginPg(self.root)
        
        
class ViewAllStaffsPg:
    def __init__(self, root, user):
        self.root = root
        

        self.user = user
        
        self.viewAllStaffsController = controller.ViewAllStaffsController()
        self.searchUserAccController = controller.SearchUserAccController()

        self.displayViewAllStaffsPg() 
 
    def displayViewAllStaffsPg(self):
        
        
        # Calling controller to get a list of users
        accounts = self.viewAllStaffsController.viewAllStaffs()
        
        self.viewAllAccCanvas = tk.Canvas(self.root,bg="#EBDFD3")
        self.viewAllAccCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.viewAllAccScrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.viewAllAccCanvas.yview)
        self.viewAllAccScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.viewAllAccCanvas.configure(yscrollcommand=self.viewAllAccScrollbar.set)
        
        self.viewAllAccFrame = tk.Frame(self.viewAllAccCanvas, bg="#EBDFD3")
        self.viewAllAccCanvas.create_window((0, 0), window=self.viewAllAccFrame, anchor="nw")

        rowNum = 0
        for account in accounts:
            # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)
            username_label = tk.Label(self.viewAllAccFrame, text=f"Full name: {account.fullName}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            username_label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")

            profile_label = tk.Label(self.viewAllAccFrame, text=f"Email: {account.email}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            profile_label.grid(row=rowNum, column=1, padx=20, pady=10, sticky="w")

            max_label = tk.Label(self.viewAllAccFrame, text=f"Maximum Work Slots: {account.numOfWorkSlots}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            max_label.grid(row=rowNum, column=2, padx=20, pady=10, sticky="w")
            
            # Add three buttons horizontally
            viewAccButton = tk.Button(self.viewAllAccFrame, text="View", command=lambda user=account: self.openAccountInfoPg(user))
            viewAccButton.grid(row=rowNum, column=3, padx=10)

            updateAccButton = tk.Button(self.viewAllAccFrame, text="Assign", command=lambda user=account: self.openAssignWorkPg(user))
            updateAccButton.grid(row=rowNum, column=4, padx=10)

    
            
            rowNum += 1
        
        backButton = tk.Button(self.viewAllAccFrame, text="Back", command= self.back)
        backButton.grid(row=rowNum, column=0)

        logoutButton = tk.Button(self.viewAllAccFrame, text="Logout", command = self.logout)
        logoutButton.grid(row=rowNum, column=1)
        
        self.viewAllAccFrame.bind("<Configure>", lambda e: self.viewAllAccCanvas.configure(scrollregion=self.viewAllAccCanvas.bbox("all")))

        # Show account information frame
        #self.viewAllAccFrame.pack(padx=50, pady=50)
    
    
            
    def openAccountInfoPg(self, userAcc):
        self.viewAllAccFrame.pack_forget()
        self.viewAllAccCanvas.pack_forget()
        self.viewAllAccScrollbar.pack_forget()
        
        ViewAccountInfoPg(self.root, self.user, userAcc) 
        
    def openAssignWorkPg(self, staff):
        self.viewAllAccFrame.pack_forget()
        self.viewAllAccCanvas.pack_forget()
        self.viewAllAccScrollbar.pack_forget()
        
        AssignWork(self.root, self.user, staff)
    
    def back(self):
        self.viewAllAccFrame.pack_forget()
        self.viewAllAccCanvas.pack_forget()
        self.viewAllAccScrollbar.pack_forget()

        ManagerPg(self.root, self.user)

    def logout(self):
        self.viewAllAccFrame.pack_forget()
        self.viewAllAccCanvas.pack_forget()
        self.viewAllAccScrollbar.pack_forget()
    
        LoginPg(self.root)
        
            
class AssignWork():
    
    def __init__(self, root, user, staff):
        self.assignWorkController = controller.AssignWorkController()
        self.root = root
        self.user = user
        self.staff = staff

        self.displayAssignWorkPg()

    def displayAssignWorkPg(self):
        self.roleFrame = tk.Frame(self.root, bg="#EBDFD3")
        self.roleFrame.pack(fill="both", expand=True)
        
        #work slot Id and entry
        self.WSLabel = tk.Label(self.roleFrame, text="Type in the work slot ID:",bg="#D3D3D3", fg = "black")
        self.WSLabel.grid(row=3, column=0, padx=5, pady=5)
        self.WSEntry = tk.Entry(self.roleFrame)
        self.WSEntry.grid(row=3, column=1, padx=5, pady=5)
        
        self.submit = tk.Button(self.roleFrame, text="Assign", command = self.assignwork, font=("Josefin Sans", 18), width=8, height=2)
        self.submit.grid(row= 4, column = 1)
        
        backButton = tk.Button(self.roleFrame, text="Back", command= self.back)
        backButton.grid(row=6, column=0)

        logoutButton = tk.Button(self.roleFrame, text="Logout", command = self.logout)
        logoutButton.grid(row=6, column=1)
    
    def assignwork(self):
        
        workSlotId = self.WSEntry.get()
        
        # Validate input (you may want to add more validation)
        if not workSlotId:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create a WorkAssignment object
        workAssignment = entity.WorkAssignment(entity.WorkSlot(workSlotId), self.staff, self.user)

        # Call the assignWork method in the controller
        result = self.assignWorkController.assignWork(workAssignment)

        if result:
            messagebox.showinfo("Success", "Work assigned successfully!")
            # self.assignWorkWindow.destroy()
        else:
            messagebox.showerror("Error", "Failed to assign work.")
            
    def back(self):
        self.roleFrame.pack_forget()
        ViewAllStaffsPg(self.root, self.user) 
        
    def logout(self):
        self.roleFrame.pack_forget()
        LoginPg(self.root)  
        
        
        
        
#cafe staff starts #cafe staff starts #cafe staff starts # cafe staff starts #cafe staff starts

class StaffPg():
    def __init__(self, root, user):
        self.loginController = controller.LoginController()
        self.chooseCafeRoleController = controller.ChooseCafeRoleController()
        self.chooseMaxWorkSlotController = controller.ChooseMaxWorkSlotController()
        self.viewAllBidsController = controller.ViewAllBidsController()
        self.root = root
        self.user = user

        self.displayStaffPg()

    def displayStaffPg(self):
        
        if(self.user.cafeRole.roleName == None):
            self.roleFrame = tk.Frame(self.root, bg="#EBDFD3")
            self.roleFrame.pack(fill="both", expand=True)
            
            #is suspended lable and option
            self.isSuspendedLabel = tk.Label(self.roleFrame, text="Choose role:", bg="#D3D3D3", fg ="black")
            self.isSuspendedLabel.grid(row=2, column=0, padx=5, pady=5)
            
            options = ["chef", "cashier", "waiter"]

            # Create a variable to store the selected value
            self.selected_var = StringVar(root)
            self.selected_var.set(options[0])  # Set the default value

            # Create a dropdown list
            self.dropdown = tk.OptionMenu(self.roleFrame, self.selected_var, *options)
            self.dropdown.grid(row=2, column=1, padx=5, pady=5)
            
            # max work slot label and entry
            self.maxWSLabel = tk.Label(self.roleFrame, text="Maximum Number of work slots within a month:",bg="#D3D3D3", fg = "black")
            self.maxWSLabel.grid(row=3, column=0, padx=5, pady=5)
            self.maxWSEntry = tk.Entry(self.roleFrame)
            self.maxWSEntry.grid(row=3, column=1, padx=5, pady=5)
            
            self.submit = tk.Button(self.roleFrame, text="Submit", command = self.submitRoleAndMaxWorkSlot, font=("Josefin Sans", 18), width=8, height=2)
            self.submit.grid(row= 4, column = 1)
        

        else:
            
            # Display welcome label
            self.mainLabel = tk.Label(self.root, text="Welcome to the Staff Page")
            self.mainLabel.pack(fill="both", expand=True)

            
            #creating admin main frame
            self.adminFrame = tk.Frame(self.root, bg="#EBDFD3")
            self.adminFrame.pack(fill="both", expand=True)
            
            # Create the sidebar
            self.sidebar = tk.Frame(self.adminFrame, width=150, height=750, bg="#DA7635")
            self.sidebar.grid(row=0, column=0)
            

            # Add a logo to the sidebar
            self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
            self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
            self.logo_label.pack(pady=10)
            
            self.logoutButton = tk.Button(self.sidebar, text="Logout", command=self.logout)
            self.logoutButton.pack(pady=(520, 0))

            # Create the main content area
            self.main_content = tk.Frame(self.adminFrame, width=1400, height=800, bg="#EBDFD3")
            self.main_content.grid(row=0, column=1)

            # Add a welcome message
            self.welcome_label = tk.Label(self.main_content, text="Welcome Staff!", font=("Josefin Sans", 30), bg="#EBDFD3", fg = "black")
            self.welcome_label.pack(pady=55)

            # Create function buttons
            self.function_buttons = tk.Frame(self.main_content, bg="#EBDFD3")
            self.function_buttons.pack()
            
            self.function_buttons = tk.Frame(self.main_content, bg="#EBDFD3")
            self.function_buttons.pack()
            
            self.button_frame = tk.Frame(self.function_buttons, bg="#EBDFD3")
            self.button_frame.pack(side="left", padx=40, pady=40)


            # Add buttons
            self.button1 = tk.Button(self.button_frame, text="View Own Account", command=self.openOwnAccountInfoPg, font=("Josefin Sans", 18), width=15, height=4)
            self.button1.grid(row= 0, column = 0)

            self.button2 = tk.Button(self.button_frame, text="View All Bids", command=self.openViewAllBidsPg, font=("Josefin Sans", 18), width=15, height=4)
            self.button2.grid(row= 0, column = 1)

            # self.button3 = tk.Button(self.button_frame, text="View All Staffs", command= self.openViewAllAccPg, font=("Josefin Sans", 18), width=15, height=4)
            # self.button3.grid(row= 1, column = 0)

            self.button4 = tk.Button(self.button_frame, text="View All Work Slots", command = self.openViewAllWorkSlotsPg, font=("Josefin Sans", 18), width=15, height=4)
            self.button4.grid(row= 1, column = 0)
            
            self.button5 = tk.Button(self.button_frame, text="View Work Assignments", command = self.openViewAllWorkAssignmentsPg, font=("Josefin Sans", 18), width=15, height=4)
            self.button5.grid(row= 0, column = 2)

    def openOwnAccountInfoPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        OwnAccountInfoPg(self.root, self.user)

    def openViewAllWorkAssignmentsPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllWorkAssignmentsPg(self.root, self.user)
        
    def openViewAllWorkSlotsPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllWorkSlotsPg(self.root, self.user)
        
    def openViewAllBidsPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllBidsPg(self.root, self.user)
        
    def submitRoleAndMaxWorkSlot(self):
        roleName = self.selected_var.get()
        numOfWorkSlots = int(self.maxWSEntry.get())
        if (numOfWorkSlots < 1 or numOfWorkSlots > 60 or numOfWorkSlots == ""):
            messagebox.showinfo("Warning", "You can't work over 60 work slots!")
        else:
            result1 = self.chooseCafeRoleController.chooseCafeRole(self.user.staffId, roleName)
            result2 = self.chooseMaxWorkSlotController.chooseMaxWorkSlot(self.user.staffId, numOfWorkSlots)
            if (result1):
                messagebox.showinfo("Successful", "Role successfully added!")
            if (result2):
                messagebox.showinfo("Successful", "Maxmum No. of work slots successfully added!")
            #self.mainLabel.pack_forget()
            #self.logoLabel.place_forget()
            #self.adminFrame.pack_forget()
            self.roleFrame.pack_forget()
            LoginPg(self.root)
    
    def logout(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        LoginPg(self.root)
        
class ViewAllBidsPg():
    def __init__(self, root, user):
        self.viewAllBidsController = controller.ViewAllBidsController()
        self.searchBidController = controller.SearchBidController()
        self.deleteBidController = controller.DeleteBidController()
        self.approveBidController = controller.ApproveBidController()
        self.rejectBidController = controller.RejectBidController()
        self.assignWorkController = controller.AssignWorkController()
        self.root = root
        self.user = user

        self.displayViewAllBidsPg()

    def displayViewAllBidsPg(self):
        self.newFrame = tk.Frame(self.root, bg="#EBDFD3")
        # Creating a header frame
        self.headerFrame = tk.Frame(self.root, bg="#EBDFD3")
        self.headerFrame.pack(side=tk.TOP, fill=tk.X)

        # Adding a search bar to the header frame
        self.searchLabel = tk.Label(self.headerFrame, text="Search by WorkSlot ID: ", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
        self.searchLabel.pack(side=tk.LEFT, padx=10, pady=10)

        self.searchEntry = tk.Entry(self.headerFrame, font=("Josefin Sans", 14))
        self.searchEntry.pack(side=tk.LEFT, padx=10, pady=10)
        
        if(self.user.userProfile.profileName == "cafe_manager"):
            self.searchLabel2 = tk.Label(self.headerFrame, text="Search by Staff ID: ", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            self.searchLabel2.pack(side=tk.LEFT, padx=10, pady=10)

            self.searchEntry2 = tk.Entry(self.headerFrame, font=("Josefin Sans", 14))
            self.searchEntry2.pack(side=tk.LEFT, padx=10, pady=10)
        

        self.searchButton = tk.Button(self.headerFrame, text="Search", command=self.displaySearchBid, font=("Josefin Sans", 14))
        self.searchButton.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Calling controller to get a list of bids
        if (self.user.userProfile.profileName == "cafe_manager"):
            bids = self.viewAllBidsController.viewAllBids()
        elif (self.user.userProfile.profileName == "cafe_staff"):
            bids = self.viewAllBidsController.viewAllBids(self.user.staffId)
        
        self.viewAllWSCanvas = tk.Canvas(self.root,bg="#EBDFD3")
        self.viewAllWSCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.viewAllWSScrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.viewAllWSCanvas.yview)
        self.viewAllWSScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.viewAllWSCanvas.configure(yscrollcommand=self.viewAllWSScrollbar.set)
        
        self.viewAllWSFrame = tk.Frame(self.viewAllWSCanvas, bg="#EBDFD3")
        self.viewAllWSCanvas.create_window((0, 0), window=self.viewAllWSFrame, anchor="nw")

        rowNum = 0
        for bid in bids:
            # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)
        
            location_label = tk.Label(self.viewAllWSFrame, text=f"Location: {bid.workSlot.location}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            location_label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
            
            date_label = tk.Label(self.viewAllWSFrame, text=f"Date: {bid.workSlot.date}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            date_label.grid(row=rowNum, column=1, padx=20, pady=10, sticky="w")
            
            date_label = tk.Label(self.viewAllWSFrame, text=f"Staff ID: {bid.staff.staffId}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            date_label.grid(row=rowNum, column=2, padx=20, pady=10, sticky="w")

            # Add three buttons horizontally
            viewAccButton = tk.Button(self.viewAllWSFrame, text="View", command=lambda current=bid: self.openViewBidInfoPg(current))
            viewAccButton.grid(row=rowNum, column=3, padx=10) 
            
            if (self.user.userProfile.profileName == "cafe_staff"):
                bidButton = tk.Button(self.viewAllWSFrame, text="Delete", command=lambda current=bid: self.deleteBid(current))
                bidButton.grid(row=rowNum, column=4, padx=10)
            elif (self.user.userProfile.profileName == "cafe_manager"):
                updateAccButton = tk.Button(self.viewAllWSFrame, text="Approve", command=lambda current=bid: self.approveBid(current))
                updateAccButton.grid(row=rowNum, column=4, padx=10)

                suspendAccButton = tk.Button(self.viewAllWSFrame, text="Reject", command=lambda current=bid: self.rejectBid(current))
                suspendAccButton.grid(row=rowNum, column=5, padx=10)
                
               
            rowNum += 1
        
        backButton = tk.Button(self.viewAllWSFrame, text="Back", command= self.back)
        backButton.grid(row=rowNum, column=0)

        logoutButton = tk.Button(self.viewAllWSFrame, text="Logout", command = self.logout)
        logoutButton.grid(row=rowNum, column=1)
        
        self.viewAllWSFrame.bind("<Configure>", lambda e: self.viewAllWSCanvas.configure(scrollregion=self.viewAllWSCanvas.bbox("all")))
    
    def displaySearchBid(self):
        input = self.searchEntry.get()
        
        bid = None
        
        if (self.user.userProfile.profileName == "cafe_staff"):
            if (input):
                bid = self.searchBidController.searchBid(input, self.user.staffId)
            else:
                # Handle the case when the input is empty
                messagebox.showerror("Notice", "Please enter a workslot id for the search.")
        elif (self.user.userProfile.profileName == "cafe_manager"):
            input2 = self.searchEntry2.get()
            if (input and input2):
                bid = self.searchBidController.searchBid(input, input2)
            else:
                messagebox.showerror("Notice", "Please enter both inputs for the search.")
                
        if bid:
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
            self.newFrame.pack_forget()
            
            location_label = tk.Label(self.newFrame, text=f"Location: {bid.workSlot.location}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            location_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
            
            date_label = tk.Label(self.newFrame, text=f"Date: {bid.workSlot.date}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            date_label.grid(row=0, column=1, padx=20, pady=10, sticky="w")

            date_label = tk.Label(self.newFrame, text=f"Staff ID: {bid.staff.staffId}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            date_label.grid(row=0, column=2, padx=20, pady=10, sticky="w")
            
            # Add three buttons horizontally
            viewAccButton = tk.Button(self.newFrame, text="View", command=lambda current=bid: self.openViewBidInfoPg(current))
            viewAccButton.grid(row=0, column=3, padx=10)
            
            if (self.user.userProfile.profileName == "cafe_staff"):
                bidButton = tk.Button(self.newFrame, text="Delete", command=lambda current=bid: self.deleteBid(current))
                bidButton.grid(row=0, column=4, padx=10)
            elif (self.user.userProfile.profileName == "cafe_manager"):
                updateAccButton = tk.Button(self.newFrame, text="Approve", command=lambda current=bid: self.approveBid(current))
                updateAccButton.grid(row=0, column=4, padx=10)

                suspendAccButton = tk.Button(self.newFrame, text="Reject", command=lambda current=bid: self.rejectBid(current))
                suspendAccButton.grid(row=0, column=5, padx=10)
                
            backButton = tk.Button(self.newFrame, text="Back", command= self.back)
            backButton.grid(row=1, column=0)

            logoutButton = tk.Button(self.newFrame, text="Logout", command = self.logout)
            logoutButton.grid(row=1, column=1)
            
            self.newFrame.pack(fill="both", expand=True)
        
        
            # ViewAccountInfoPg(self.root, userAcc)
        else:
            # Handle the case when the user is not found
            messagebox.showinfo("Info","The work slot you are searching for does not exist")
            
        

        
            
    def approveBid(self, bid):
        
        ws = entity.WorkAssignment(entity.WorkSlot(bid.workSlot.workSlotId), entity.CafeStaff(bid.staff.staffId), entity.CafeManager(self.user.managerId))
        workAssignment = self.assignWorkController.assignWork(ws)
        if (workAssignment):
            result = self.approveBidController.approveBid(bid.workSlot.workSlotId, bid.staff.staffId)
            if (result):
                messagebox.showinfo("Successful", "Successfully Approved!")
        else: 
            messagebox.showinfo("Notice", "Staff is already assigned. Cannot assign twice.")
            
            
    def rejectBid(self, bid):
        result = self.rejectBidController.rejectBid(bid.workSlot.workSlotId, bid.staff.staffId)
        if (result):
            messagebox.showinfo("Successful", "Successfully Rejected!")
        
    def deleteBid(self, bid):
        if (bid.bidStatus != "Approve"):
            result = self.deleteBidController.deleteBid(bid.workSlot.workSlotId,self.user.staffId)
            if (result):
                messagebox.showinfo("Successful", "Successfully Deleted!")
                self.viewAllWSFrame.pack_forget()
                self.viewAllWSCanvas.pack_forget()
                self.viewAllWSScrollbar.pack_forget()
                self.headerFrame.pack_forget()
                self.newFrame.pack_forget()
                self.displayViewAllBidsPg()
            
        else:
            messagebox.showinfo("Notice", "Already assigned!Cannot delete now!")
            
    def openOwnAccountInfoPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        OwnAccountInfoPg(self.root, self.user)

    def openCreateAccountPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        CreateAccountPg(self.root, self.user)
        
    def openViewAllWorkSlotPg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        ViewAllWorkSlotsPg(self.root, self.user)
        
    def openCreateProfilePg(self):
        self.mainLabel.pack_forget()
        #self.logoLabel.place_forget()
        self.adminFrame.pack_forget()
        CreateUserProfilePg(self.root, self.user)
    
    def openViewBidInfoPg(self, bid):
        self.viewAllWSFrame.pack_forget()
        self.viewAllWSCanvas.pack_forget()
        self.viewAllWSScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        ViewBidInfoPg(self.root, self.user, bid)
    
    def back(self):
        if (self.user.userProfile.profileName == "cafe_owner"):
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
            self.headerFrame.pack_forget()
            self.newFrame.pack_forget()
            OwnerPg(self.root, self.user)
        elif (self.user.userProfile.profileName == "cafe_staff"):
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
            self.headerFrame.pack_forget()
            self.newFrame.pack_forget()
            StaffPg(self.root, self.user)
        elif(self.user.userProfile.profileName == "cafe_manager"):
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
            self.headerFrame.pack_forget()
            self.newFrame.pack_forget()
            ManagerPg(self.root, self.user)

    def logout(self):
        self.viewAllWSFrame.pack_forget()
        self.viewAllWSCanvas.pack_forget()
        self.viewAllWSScrollbar.pack_forget()
        self.headerFrame.pack_forget()
        self.newFrame.pack_forget()
        LoginPg(self.root)  

class ViewBidInfoPg:
    def __init__(self, root, user, bid):
        self.root = root
        self.user = user
        self.bid = bid

        self.displayViewBidInfoPg()
    
    def displayViewBidInfoPg(self):
        
        self.ownAccountFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.ownAccountFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #making container frame
        self.container_frame = tk.Frame(self.ownAccountFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Bids Information", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Display the account information in labels
        rowNum = 1
        for i, (attribute, value) in enumerate(vars(self.bid).items()):
            if (attribute == "workSlot"):
                for j, (lable, price) in enumerate(vars(value).items()):
                    if (lable == "roleAssignments"):
                        for assignment in price:
                            label_text = f"{assignment.role.roleName}: {assignment.numOfStaff}"
                            label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                            label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
                            rowNum += 1
                    else:
                        label_text = f"{lable}: {price}"
                        label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                        label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
                        rowNum += 1

            elif (attribute == "staff"):
                rowNo = 1
                for k, (lable, price) in enumerate(vars(value).items()):
                    if (lable != "username" and lable != "password" and lable != "userProfile" and lable != "isSuspended" and lable != "dateOfBirth"):
                        if (lable == "cafeRole"):
                            price = price.roleName
                        label_text = f"{lable}: {price}"
                        label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                        label.grid(row=rowNo, column=2, padx=20, pady=10, sticky="w")
                        rowNo += 1
            else:
                label_text = f"{attribute}: {value}"
                label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
                rowNum += 1
        
        
        # Show account information frame
        self.ownAccountFrame.pack(fill="both", expand=True)

    def back(self):
        self.ownAccountFrame.pack_forget()
        ViewAllBidsPg(self.root, self.user)

    def logout(self):
        self.ownAccountFrame.pack_forget()
        LoginPg(self.root)
        
        

#view work assignments view work assignment view work assignment view work assigment

class ViewAllWorkAssignmentsPg():
    def __init__(self, root, user):
        self.viewAllWorkAssignmentsController = controller.ViewAllWorkAssignmentsController()
        self.root = root
        self.user = user

        self.displayViewAllWorkAssignmentsPg()

    def displayViewAllWorkAssignmentsPg(self):
        
        
        # Calling controller to get a list of bids
        if (self.user.userProfile.profileName == "cafe_manager"):
            workAssignments = self.viewAllWorkAssignmentsController.viewAllWorkAssignments()
        elif (self.user.userProfile.profileName == "cafe_staff"):
            workAssignments = self.viewAllWorkAssignmentsController.viewAllWorkAssignments(self.user.staffId)
        
        self.viewAllWSCanvas = tk.Canvas(self.root,bg="#EBDFD3")
        self.viewAllWSCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.viewAllWSScrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.viewAllWSCanvas.yview)
        self.viewAllWSScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.viewAllWSCanvas.configure(yscrollcommand=self.viewAllWSScrollbar.set)
        
        self.viewAllWSFrame = tk.Frame(self.viewAllWSCanvas, bg="#EBDFD3")
        self.viewAllWSCanvas.create_window((0, 0), window=self.viewAllWSFrame, anchor="nw")

        rowNum = 0
        for wa in workAssignments:
            # userAcc = entity.UserAccount(account.username, account.password, account.email, account.phoneNumber, account.dateOfBirth, account.userProfile, account.isSuspended)
        
            location_label = tk.Label(self.viewAllWSFrame, text=f"Location: {wa.workSlot.location}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            location_label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
            
            date_label = tk.Label(self.viewAllWSFrame, text=f"Staff Name: {wa.staff.fullName}", bg="#EBDFD3", font=("Josefin Sans", 18), fg = "black")
            date_label.grid(row=rowNum, column=1, padx=20, pady=10, sticky="w")

            # Add three buttons horizontally
            viewAccButton = tk.Button(self.viewAllWSFrame, text="View", command=lambda current=wa: self.openViewWorkAssignmentInfoPg(current))
            viewAccButton.grid(row=rowNum, column=2, padx=10)    
            rowNum += 1
        
        backButton = tk.Button(self.viewAllWSFrame, text="Back", command= self.back)
        backButton.grid(row=rowNum, column=0)

        logoutButton = tk.Button(self.viewAllWSFrame, text="Logout", command = self.logout)
        logoutButton.grid(row=rowNum, column=1)
        
        self.viewAllWSFrame.bind("<Configure>", lambda e: self.viewAllWSCanvas.configure(scrollregion=self.viewAllWSCanvas.bbox("all")))
    
    
            
    
    def openViewWorkAssignmentInfoPg(self, wa):
        self.viewAllWSFrame.pack_forget()
        self.viewAllWSCanvas.pack_forget()
        self.viewAllWSScrollbar.pack_forget()
        
        ViewWorkAssignmentInfoPg(self.root, self.user, wa)
    
    def back(self):
        # if (self.user.userProfile.profileName == "cafe_owner"):
        #     self.viewAllWSFrame.pack_forget()
        #     self.viewAllWSCanvas.pack_forget()
        #     self.viewAllWSScrollbar.pack_forget()
        #     self.headerFrame.pack_forget()
        #     self.newFrame.pack_forget()
        #     OwnerPg(self.root, self.user)
        if (self.user.userProfile.profileName == "cafe_staff"):
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
            
            StaffPg(self.root, self.user)
        elif(self.user.userProfile.profileName == "cafe_manager"):
            self.viewAllWSFrame.pack_forget()
            self.viewAllWSCanvas.pack_forget()
            self.viewAllWSScrollbar.pack_forget()
    
            ManagerPg(self.root, self.user)

    def logout(self):
        self.viewAllWSFrame.pack_forget()
        self.viewAllWSCanvas.pack_forget()
        self.viewAllWSScrollbar.pack_forget()
    
        LoginPg(self.root)  

class ViewWorkAssignmentInfoPg:
    def __init__(self, root, user, wa):
        self.root = root
        self.user = user
        self.wa = wa  

        self.displayViewWorkAssignmentInfoPg()
    
    def displayViewWorkAssignmentInfoPg(self):
        
        self.ownAccountFrame = tk.Frame(self.root, bg="#D3D3D3")
        
        # Create the sidebar
        self.sidebar = tk.Frame(self.ownAccountFrame, width=150, height=750, bg="#DA7635")
        self.sidebar.grid(row=0, column=0)

        # Add a logo to the sidebar
        self.logo_image = tk.PhotoImage(file="Images/CafeLogo.png")
        self.logo_label = tk.Label(self.sidebar, image=self.logo_image, bg="#DA7635")
        self.logo_label.pack(pady=10)
        
        #adding back and log out button to the sidebar
        self.button_frame = tk.Frame(self.sidebar, bg="#DA7635")
        self.button_frame.pack(pady=(520, 0))

        self.backButton = tk.Button(self.button_frame, text="Back", command=self.back)
        self.backButton.pack(side=tk.LEFT, padx=5)
        
        self.logoutButton = tk.Button(self.button_frame, text="Logout", command=self.logout)
        self.logoutButton.pack(side=tk.LEFT, padx=5)
        
        #making container frame
        self.container_frame = tk.Frame(self.ownAccountFrame, bg="#D3D3D3")
        self.container_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.welcome_label = tk.Label(self.container_frame, text="Work Assignments", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        
        # Display the account information in labels
        
        for i, (attribute, value) in enumerate(vars(self.wa).items()):
            if (attribute == "workSlot"):
                self.welcome_label = tk.Label(self.container_frame, text="Work Slot", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
                self.welcome_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
                rowNum = 2
                for j, (lable, price) in enumerate(vars(value).items()):
                    if (lable == "roleAssignments"):
                        for assignment in price:
                            label_text = f"{assignment.role.roleName}: {assignment.numOfStaff}"
                            label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                            label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
                            rowNum += 1
                    else:
                        label_text = f"{lable}: {price}"
                        label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                        label.grid(row=rowNum, column=0, padx=20, pady=10, sticky="w")
                        rowNum += 1

            elif (attribute == "staff"):
                self.welcome_label = tk.Label(self.container_frame, text="Staff", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
                self.welcome_label.grid(row=1, column=2, padx=20, pady=10, sticky="w")
                rowNo = 2
                for k, (lable, price) in enumerate(vars(value).items()):
                    if (lable != "username" and lable != "password" and lable != "userProfile" and lable != "isSuspended" and lable != "dateOfBirth"):
                        if (lable == "cafeRole"):
                            price = price.roleName
                        label_text = f"{lable}: {price}"
                        label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                        label.grid(row=rowNo, column=2, padx=20, pady=10, sticky="w")
                        rowNo += 1
                        
            elif (attribute == "manager"):
                self.welcome_label = tk.Label(self.container_frame, text="Manager", font=("Josefin Sans", 30), bg="#D3D3D3", fg = "black")
                self.welcome_label.grid(row=1, column=4, padx=20, pady=10, sticky="w")
                rowNumber = 2
                for k, (lable, price) in enumerate(vars(value).items()):
                    if (lable != "username" and lable != "password" and lable != "userProfile" and lable != "isSuspended" and lable != "dateOfBirth"):
                        label_text = f"{lable}: {price}"
                        label = tk.Label(self.container_frame, text=label_text, bg="#D3D3D3", fg = "Black", font=("Arial", 20))
                        label.grid(row=rowNumber, column=4, padx=20, pady=10, sticky="w")
                        rowNumber += 1
        
        
        # Show account information frame
        self.ownAccountFrame.pack(fill="both", expand=True)

    def back(self):
        self.ownAccountFrame.pack_forget()
        ViewAllWorkAssignmentsPg(self.root, self.user)

    def logout(self):
        self.ownAccountFrame.pack_forget()
        LoginPg(self.root)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPg(root)
    root.mainloop()
