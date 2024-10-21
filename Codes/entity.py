import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cafe_staff_management"
)

class UserProfile:
    def __init__(self, profileName=None, description=None, isSuspended=False):
        self.profileName = profileName
        self.description = description
        self.isSuspended = isSuspended

    def createUserProfile(self, userProfile):
        try:
            mycursor = mydb.cursor()
            query = "INSERT INTO userprofile (profile_name, profile_description, is_suspended) VALUES (%s, %s, %s)"
            data = (userProfile.profileName, userProfile.description, userProfile.isSuspended)
            mycursor.execute(query, data)
            mydb.commit()

            rowsAffected = mycursor.rowcount
            
            if (rowsAffected > 0):
                return True
            else:
                return False
        except Exception as e:
            print(f"Error creating profile: {e}")
            return False
        
    def viewAllProfile(self):
        mycursor = mydb.cursor()
        query = "SELECT * FROM userprofile"
        mycursor.execute(query)

        profiles = mycursor.fetchall()

        profileList = []
        
        if (profiles):
            for (profileName, description, isSuspended) in profiles:
                userProfile = UserProfile(profileName, description, isSuspended)
                profileList.append(userProfile)
        
        return profileList

    def updateUserProfile(self, profileName, userProfile):
        try:
            mycursor = mydb.cursor()

            mycursor.execute("SET foreign_key_checks = 0")
            query2 = "UPDATE userprofile SET profile_name = %s, profile_description = %s WHERE profile_name = %s"
            data = (userProfile.profileName, userProfile.description, profileName)
            mycursor.execute(query2, data)
            
            mydb.commit()

            if (profileName != userProfile.profileName):
                query1 = f"UPDATE useraccount SET profile_name = %s WHERE profile_name = %s"
                data = (userProfile.profileName, profileName)
                mycursor.execute(query1, data)

            mycursor.execute("SET foreign_key_checks = 1")

            return True
        except Exception as e:
            print(f"Error updating user profile: {e}")
            return False
            
    def suspendUserProfile(self, profileName):
        mycursor = mydb.cursor()
        query1 = "UPDATE userprofile SET is_suspended = True WHERE profile_name = %s"
        data = [profileName]
        mycursor.execute(query1, data)

        rowsAffected = mycursor.rowcount

        query2 = "UPDATE useraccount SET is_suspended = True WHERE profile_name = %s"
        data = [profileName]
        mycursor.execute(query2, data)

        mydb.commit()
        
        if (rowsAffected > 0):
            return True
        else:
            return False
    
    def searchUserProfile(self, profileName):
        mycursor = mydb.cursor()
        query = "SELECT * FROM userprofile WHERE profile_name = %s"
        data = [profileName]
        mycursor.execute(query, data)

        profile = mycursor.fetchone()
        
        if (profile):
            return UserProfile(profile[0], profile[1], profile[2])
        else:
            return None
        
    def __eq__(self, other):
        if isinstance(other, UserProfile):
            return (
                self.profileName == other.profileName and
                self.description == other.description and
                self.isSuspended == other.isSuspended
            )
        return False
    

class UserAccount:
    def __init__(self, username=None, password=None, fullName=None, email=None, phoneNumber=None, address=None, dateOfBirth=None, userProfile=None, isSuspended=False):
        self.username = username
        self.password = password
        self.fullName = fullName
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.dateOfBirth = dateOfBirth
        self.userProfile = userProfile
        self.isSuspended = isSuspended

    def login(self, username, password):
        mycursor = mydb.cursor()
        query1 = "SELECT * FROM useraccount WHERE username = %s AND password = %s"
        data = (username, password)
        mycursor.execute(query1, data)

        account = mycursor.fetchone()

        if (account):
            if (account[8] == True):
                return None

            if (account[7] == "system_admin"):
                query2 = "SELECT admin_id FROM system_admin WHERE username = %s"
                data = [username]
                mycursor.execute(query2, data)
                adminId = mycursor.fetchone()
                return SystemAdmin(adminId[0], account[0], account[1], account[2], account[3], account[4], account[5], account[6], UserProfile(account[7]), account[8])
            elif (account[7] == "cafe_owner"):
                query2 = "SELECT owner_id FROM cafe_owner WHERE username = %s"
                data = [username]
                mycursor.execute(query2, data)
                ownerId = mycursor.fetchone()
                return CafeOwner(ownerId[0], account[0], account[1], account[2], account[3], account[4], account[5], account[6], UserProfile(account[7]), account[8])
            elif (account[7] == "cafe_manager"):
                query2 = "SELECT manager_id FROM cafe_manager WHERE username = %s"
                data = [username]
                mycursor.execute(query2, data)
                managerId = mycursor.fetchone()
                return CafeManager(managerId[0], account[0], account[1], account[2], account[3], account[4], account[5], account[6], UserProfile(account[7]), account[8])
            elif (account[7] == "cafe_staff"):
                query2 = "SELECT * FROM cafe_staff WHERE username = %s"
                data = [username]
                mycursor.execute(query2, data)
                staff = mycursor.fetchone()
                return CafeStaff(staff[0], CafeRole(staff[2]), staff[3], account[0], account[1], account[2], account[3], account[4], account[5], account[6], UserProfile(account[7]), account[8])
            elif (account):
                return UserAccount(account[0], account[1], account[2], account[3], account[4], account[5], account[6], UserProfile(account[7]), account[8])
        else:
            return None
        
    def changePw(self, username, oldPw, newPw):
        mycursor = mydb.cursor()
        query = "UPDATE useraccount SET password = %s WHERE username = %s AND password = %s"
        data = (newPw, username, oldPw)
        mycursor.execute(query, data)
        mydb.commit()

        rowsAffected = mycursor.rowcount
        
        if (rowsAffected > 0):
            # Password updated successfully
            return True
        else:
            # No rows were updated; password change failed
            return False
        
    def createUserAcc(self, userAcc):
        try:
            mycursor = mydb.cursor()
            query1 = "INSERT INTO useraccount (username, password, fullname, email, phone_no, address, date_of_birth, profile_name, is_suspended) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (userAcc.username, userAcc.password, userAcc.fullName, userAcc.email, userAcc.phoneNumber, userAcc.address, userAcc.dateOfBirth, userAcc.userProfile.profileName, userAcc.isSuspended)
            mycursor.execute(query1, data)

            tables = ["system_admin", "cafe_owner", "cafe_manager", "cafe_staff"]
            if (userAcc.userProfile.profileName in tables):
                query2 = f"INSERT INTO {userAcc.userProfile.profileName} (username) VALUES (%s)"
                data = (userAcc.username,)
                mycursor.execute(query2, data)

            mydb.commit()
            return True
        except Exception as e:
            print(f"Error creating account: {e}")
            return False
        
    def viewAllAcc(self):
        mycursor = mydb.cursor()
        query = "SELECT useraccount.*, userprofile.profile_description, userprofile.is_suspended FROM useraccount LEFT JOIN userprofile ON useraccount.profile_name = userprofile.profile_name"
        mycursor.execute(query)

        accounts = mycursor.fetchall()
        rowsAffected = mycursor.rowcount

        accountList = []

        if (rowsAffected > 0):
            for (username, password, fullName, email, phoneNumber, address, dateOfBirth, profileName, accIsSuspended, profileDesc, profileIsSuspended) in accounts:
                userAcc = UserAccount(username, password, fullName, email, phoneNumber, address, dateOfBirth, UserProfile(profileName, profileDesc, profileIsSuspended), accIsSuspended)
                accountList.append(userAcc)
        
        return accountList
        
    def updateUserAcc(self, username, userAcc):
        try: 
            mycursor = mydb.cursor()
            
            if (username != userAcc.username):
                mycursor.execute("SET foreign_key_checks = 0")
                query1 = f"UPDATE {userAcc.userProfile.profileName} SET username = %s WHERE username = %s"
                data = (userAcc.username, username)
                mycursor.execute(query1, data)

            query2 = "UPDATE useraccount SET username = %s, password = %s, email = %s, phone_no = %s, date_of_birth = %s, profile_name = %s WHERE username = %s"
            data = (userAcc.username, userAcc.password, userAcc.email, userAcc.phoneNumber, userAcc.dateOfBirth, userAcc.userProfile.profileName, username)
            mycursor.execute(query2, data)
            mycursor.execute("SET foreign_key_checks = 1")
            mydb.commit()

            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    def suspendUserAcc(self, username):
        mycursor = mydb.cursor()
        query = "UPDATE useraccount SET is_suspended = True WHERE username = %s"
        data = [username]
        mycursor.execute(query, data)
        mydb.commit()

        rowsAffected = mycursor.rowcount
        
        if (rowsAffected > 0):
            return True
        else:
            return False
        
    def searchUserAcc(self, username):
        mycursor = mydb.cursor()
        query = "SELECT * FROM useraccount WHERE username = %s"
        data = [username]
        mycursor.execute(query, data)

        account = mycursor.fetchone()

        if (account):
            return UserAccount(account[0], account[1], account[2], account[3], account[4], account[5], account[6], UserProfile(account[7]), account[8])
        else:
            return None
        
    def __eq__(self, other):
        if isinstance(other, UserAccount):
            return (
                self.username == other.username and
                self.password == other.password and
                self.fullName == other.fullName and
                self.email == other.email and
                self.phoneNumber == other.phoneNumber and
                self.address == other.address and
                self.dateOfBirth == other.dateOfBirth and
                self.userProfile == other.userProfile and
                self.isSuspended == other.isSuspended
            )
        return False
        

class SystemAdmin(UserAccount):
    def __init__(self, adminId=None, username=None, password=None, fullName=None, email=None, phoneNumber=None, address=None, dateOfBirth=None, userProfile=None, isSuspended=False):
        super().__init__(username, password, fullName, email, phoneNumber, address, dateOfBirth, userProfile, isSuspended)
        self.adminId = adminId

    # def __eq__(self, other):
    #     if isinstance(other, SystemAdmin):
    #         return (
    #             self.adminId == other.adminId and
    #             self.username == other.username and
    #             self.password == other.password and
    #             self.fullName == other.fullName and
    #             self.email == other.email and
    #             self.phoneNumber == other.phoneNumber and
    #             self.address == other.address and
    #             self.dateOfBirth == other.dateOfBirth and
    #             self.userProfile == other.userProfile and
    #             self.isSuspended == other.isSuspended
    #         )
    #     return False
    
class CafeOwner(UserAccount):
    def __init__(self, ownerId=None, username=None, password=None, fullName=None, email=None, phoneNumber=None, address=None, dateOfBirth=None, userProfile=None, isSuspended=False):
        super().__init__(username, password, fullName, email, phoneNumber, address, dateOfBirth, userProfile, isSuspended)
        self.ownerId = ownerId
    
class CafeManager(UserAccount):
    def __init__(self, managerId=None, username=None, password=None, fullName=None, email=None, phoneNumber=None, address=None, dateOfBirth=None, userProfile=None, isSuspended=False):
        super().__init__(username, password, fullName, email, phoneNumber, address, dateOfBirth, userProfile, isSuspended)
        self.managerId = managerId
    
class CafeStaff(UserAccount):
    def __init__(self, staffId=None, cafeRole=None, numOfWorkSlots=None, username=None, password=None, fullName=None, email=None, phoneNumber=None, address=None, dateOfBirth=None, userProfile=None, isSuspended=False):
        super().__init__(username, password, fullName, email, phoneNumber, address, dateOfBirth, userProfile, isSuspended)
        self.staffId = staffId
        self.cafeRole = cafeRole
        self.numOfWorkSlots = numOfWorkSlots

    def chooseCafeRole(self, staffId, roleName):
        mycursor = mydb.cursor()
        query = "UPDATE cafe_staff SET role_name = %s WHERE staff_id = %s"
        data = (roleName, staffId)
        mycursor.execute(query, data)
        mydb.commit()

        rowsAffected = mycursor.rowcount
        
        if (rowsAffected > 0):
            return True
        else:
            return False
        
    def chooseMaxWorkSlot(self, staffId, numOfWorkSlots):
        mycursor = mydb.cursor()
        query = "UPDATE cafe_staff SET max_num_work_slots = %s WHERE staff_id = %s"
        data = (numOfWorkSlots, staffId)
        mycursor.execute(query, data)
        mydb.commit()

        rowsAffected = mycursor.rowcount
        
        if (rowsAffected > 0):
            return True
        else:
            return False

    def viewAllStaffs(self):
        query = '''
            SELECT
                cafe_staff.staff_id,
                cafe_staff.username,
                cafe_staff.role_name,
                cafe_staff.max_num_work_slots,
                useraccount.password,
                useraccount.fullname,
                useraccount.email,
                useraccount.phone_no,
                useraccount.address,
                useraccount.date_of_birth,
                useraccount.profile_name,
                useraccount.is_suspended
            FROM
                cafe_staff
            INNER JOIN
                useraccount ON cafe_staff.username = useraccount.username;
        '''
        mycursor = mydb.cursor()

        mycursor.execute(query)
        result = mycursor.fetchall()

        staffList = []

        for (staffId, username, roleName, numOfWorkSlots, password, fullName, email, phoneNumber, address, dateOfBirth, profileName, isSuspended) in result:
                staffAcc = CafeStaff(staffId, CafeRole(roleName), numOfWorkSlots, username, password, fullName, email, phoneNumber, address, dateOfBirth, UserProfile(profileName), isSuspended)
                staffList.append(staffAcc)

        return staffList
    

class CafeRole:
    def __init__(self, roleName, roleDescription=None):
        self.roleName = roleName
        self.roleDescription = roleDescription

class RoleAssignment:
    def __init__(self, role, numOfStaff):
        self.role = role
        self.numOfStaff = numOfStaff

class WorkSlot:
    def __init__(self, workSlotId=None, location=None, date=None, startTime=None, endTime=None, roleAssignments=None):
        self.workSlotId = workSlotId
        self.location = location
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.roleAssignments = roleAssignments


    def createWorkSlot(self, workSlot):
        try:
            mycursor = mydb.cursor()
            query1 = "INSERT INTO work_slot (location, work_date, start_time, end_time) VALUES (%s, %s, %s, %s)"
            data = (workSlot.location, workSlot.date, workSlot.startTime, workSlot.endTime)
            mycursor.execute(query1, data)

            mycursor.execute("SELECT LAST_INSERT_ID()")
            workSlotId = mycursor.fetchone()[0]

            for i in workSlot.roleAssignments:
                query2 = "INSERT INTO work_slot_cafe_role (work_slot_id, role_name, num_of_staff) VALUES (%s, %s, %s)"
                data = (workSlotId, i.role.roleName, i.numOfStaff)
                mycursor.execute(query2, data)
                
            mydb.commit()
            return True
        
        except Exception as e:
            print(f"Error creating work slot: {e}")
            return False
        
    def viewAllWorkSlots(self):
        mycursor = mydb.cursor()
        query = """
            SELECT
                ws.work_slot_id,
                ws.location,
                ws.work_date,
                ws.start_time,
                ws.end_time,
                wscr.role_name,
                wscr.num_of_staff
            FROM
                work_slot ws
            LEFT JOIN
                work_slot_cafe_role wscr ON ws.work_slot_id = wscr.work_slot_id;
        """

        mycursor.execute(query)

        result = mycursor.fetchall()

        workSlots = {}
        for row in result:
            workSlotId, location, date, startTime, endTime, roleName, numOfStaff = row

            if workSlotId not in workSlots:
                workSlots[workSlotId] = WorkSlot(
                    workSlotId=workSlotId,
                    location=location,
                    date=date,
                    startTime=startTime,
                    endTime=endTime,
                    roleAssignments=[]
                )

            workSlots[workSlotId].roleAssignments.append(RoleAssignment(CafeRole(roleName), numOfStaff))

        return list(workSlots.values())
    
    def updateWorkSlot(self, workSlot):
        try:
            mycursor = mydb.cursor()
            query = "UPDATE work_slot SET location = %s, work_date = %s, start_time = %s, end_time = %s WHERE work_slot_id = %s"
            data = (workSlot.location, workSlot.date, workSlot.startTime, workSlot.endTime, workSlot.workSlotId)
            mycursor.execute(query, data)

            for i in workSlot.roleAssignments:
                query2 = "UPDATE work_slot_cafe_role SET num_of_staff = %s WHERE work_slot_id = %s and role_name = %s"
                data = (i.numOfStaff, workSlot.workSlotId, i.role.roleName)
                mycursor.execute(query2, data)

            mydb.commit()
            return True
        except Exception as e:
            print(f"Error updating work slot {e}")
            return False
        
    def deleteWorkSlot(self, workSlotId):
        try:
            mycursor = mydb.cursor()
            query1 = "DELETE FROM work_slot_cafe_role WHERE work_slot_id = %s"
            query2 = "DELETE FROM bid WHERE work_slot_id = %s"
            query3 = "DELETE FROM work_assignment WHERE work_slot_id = %s"
            query4 = "DELETE FROM work_slot WHERE work_slot_id = %s"
            
            data = [workSlotId]
            mycursor.execute(query1, data)
            mycursor.execute(query2, data)
            mycursor.execute(query3, data)
            mycursor.execute(query4, data)

            mydb.commit()
            return True
        except Exception as e:
            print(f"Error deleting work slot: {e}")
            return False
    
    def searchWorkSlot(self, workSlotId):
        mycursor = mydb.cursor()
        query = """
            SELECT
                ws.work_slot_id,
                ws.location,
                ws.work_date,
                ws.start_time,
                ws.end_time,
                wscr.role_name,
                wscr.num_of_staff
            FROM
                work_slot ws
            LEFT JOIN
                work_slot_cafe_role wscr ON ws.work_slot_id = wscr.work_slot_id
            WHERE
                ws.work_slot_id = %s;
        """
        data = [workSlotId]
        mycursor.execute(query, data)

        result = mycursor.fetchall()
        workSlot = None
        if (result):
            for row in result:
                workSlotId, location, date, startTime, endTime, roleName, numOfStaff = row

                if workSlot is None:
                    workSlot = WorkSlot(
                        workSlotId=workSlotId,
                        location=location,
                        date=date,
                        startTime=startTime,
                        endTime=endTime,
                        roleAssignments=[]
                    )

                workSlot.roleAssignments.append(RoleAssignment(CafeRole(roleName), numOfStaff))
            
            return workSlot
        else:
            return None


class Bid:
    def __init__(self, workSlot=None, staff=None, bidStatus=None):
        self.workSlot = workSlot
        self.staff = staff
        self.bidStatus = bidStatus

    def createBid(self, bid):
        try:
            mycursor = mydb.cursor()
            query = "INSERT INTO bid (work_slot_id, cafe_staff_id, bid_status) VALUES (%s, %s, %s)"
            data = (bid.workSlot.workSlotId, bid.staff.staffId, bid.bidStatus)
            mycursor.execute(query, data)

            mydb.commit()
            return True
        except Exception as e:
            print(f"Error creating bid: {e}")
            return False
        
    def viewAllBids(self, staffId=None):
        mycursor = mydb.cursor()
        if (staffId == None):  #for manager view all bids
            query = '''
                SELECT
                    bid.work_slot_id,
                    bid.cafe_staff_id,
                    bid.bid_status,
                    work_slot.location,
                    work_slot.work_date,
                    work_slot.start_time,
                    work_slot.end_time,
                    work_slot_cafe_role.role_name,
                    work_slot_cafe_role.num_of_staff,
                    cafe_staff.username,
                    cafe_staff.role_name,
                    cafe_staff.max_num_work_slots,
                    useraccount.password,
                    useraccount.fullname,
                    useraccount.email,
                    useraccount.phone_no,
                    useraccount.address,
                    useraccount.date_of_birth,
                    useraccount.profile_name,
                    useraccount.is_suspended
                FROM
                    bid
                JOIN
                    work_slot ON bid.work_slot_id = work_slot.work_slot_id
                LEFT JOIN
                    work_slot_cafe_role ON work_slot.work_slot_id = work_slot_cafe_role.work_slot_id
                JOIN
                    cafe_staff ON bid.cafe_staff_id = cafe_staff.staff_id
                JOIN
                    useraccount ON cafe_staff.username = useraccount.username;
            '''
            mycursor.execute(query)

        else:   #for staff view all bids
            query = '''
                SELECT
                    bid.work_slot_id,
                    bid.cafe_staff_id,
                    bid.bid_status,
                    work_slot.location,
                    work_slot.work_date,
                    work_slot.start_time,
                    work_slot.end_time,
                    work_slot_cafe_role.role_name,
                    work_slot_cafe_role.num_of_staff,
                    cafe_staff.username,
                    cafe_staff.role_name,
                    cafe_staff.max_num_work_slots,
                    useraccount.password,
                    useraccount.fullname,
                    useraccount.email,
                    useraccount.phone_no,
                    useraccount.address,
                    useraccount.date_of_birth,
                    useraccount.profile_name,
                    useraccount.is_suspended
                FROM
                    bid
                JOIN
                    work_slot ON bid.work_slot_id = work_slot.work_slot_id
                LEFT JOIN
                    work_slot_cafe_role ON work_slot.work_slot_id = work_slot_cafe_role.work_slot_id
                JOIN
                    cafe_staff ON bid.cafe_staff_id = cafe_staff.staff_id
                JOIN
                    useraccount ON cafe_staff.username = useraccount.username
                WHERE 
                    bid.cafe_staff_id = %s;
            '''
            data = [staffId]
            mycursor.execute(query, data)
        
        result = mycursor.fetchall()

        bids = {}
        for row in result:
            workSlotId, cafeStaffId, bidStatus, location, date, startTime, endTime, roleName, numOfStaff, username, staffRole, numOfWorkSlots, password, fullName, email, phoneNum, address, dateOfBirth, profileName, isSuspended= row

            if (workSlotId, cafeStaffId) not in bids:
                bids[(workSlotId, cafeStaffId)] = Bid(
                    workSlot=WorkSlot(workSlotId, location, date, startTime, endTime, []),
                    staff=CafeStaff(cafeStaffId, CafeRole(staffRole), numOfWorkSlots, username, password, fullName, email, phoneNum, address, dateOfBirth, UserProfile(profileName), isSuspended),
                    bidStatus=bidStatus
                )
            
            bids[(workSlotId, cafeStaffId)].workSlot.roleAssignments.append(RoleAssignment(CafeRole(roleName), numOfStaff))

        return list(bids.values())

    def approveBid(self, workSlotId, staffId):
        mycursor = mydb.cursor()
        query = "UPDATE bid SET bid_status = 'Approve' WHERE work_slot_id = %s AND cafe_staff_id = %s"
        data = (workSlotId, staffId)
        mycursor.execute(query, data)
        
        mydb.commit()
        rowsAffected = mycursor.rowcount

        if (rowsAffected > 0):
            return True
        else:
            return False

    def rejectBid(self, workSlotId, staffId):
        mycursor = mydb.cursor()
        query = "UPDATE bid SET bid_status = 'Reject' WHERE work_slot_id = %s AND cafe_staff_id = %s"
        data = (workSlotId, staffId)
        mycursor.execute(query, data)
        
        mydb.commit()
        rowsAffected = mycursor.rowcount

        if (rowsAffected > 0):
            return True
        else:
            return False

    def deleteBid(self, workSlotId, staffId):
        mycursor = mydb.cursor()
        query = "DELETE FROM bid WHERE work_slot_id = %s AND cafe_staff_id = %s"
        data = (workSlotId, staffId)
        mycursor.execute(query, data)
        mydb.commit()

        rowsAffected = mycursor.rowcount
        
        if (rowsAffected > 0):
            return True
        else:
            return False
        
    def searchBid(self, workSlotId, staffId):
        mycursor = mydb.cursor()
        query = '''
                SELECT
                    bid.work_slot_id,
                    bid.cafe_staff_id,
                    bid.bid_status,
                    work_slot.location,
                    work_slot.work_date,
                    work_slot.start_time,
                    work_slot.end_time,
                    work_slot_cafe_role.role_name,
                    work_slot_cafe_role.num_of_staff,
                    cafe_staff.username,
                    cafe_staff.role_name,
                    cafe_staff.max_num_work_slots,
                    useraccount.password,
                    useraccount.fullname,
                    useraccount.email,
                    useraccount.phone_no,
                    useraccount.address,
                    useraccount.date_of_birth,
                    useraccount.profile_name,
                    useraccount.is_suspended
                FROM
                    bid
                JOIN
                    work_slot ON bid.work_slot_id = work_slot.work_slot_id
                LEFT JOIN
                    work_slot_cafe_role ON work_slot.work_slot_id = work_slot_cafe_role.work_slot_id
                JOIN
                    cafe_staff ON bid.cafe_staff_id = cafe_staff.staff_id
                JOIN
                    useraccount ON cafe_staff.username = useraccount.username
                WHERE 
                    bid.work_slot_id = %s AND bid.cafe_staff_id = %s;
            '''
        data = (workSlotId, staffId)
        mycursor.execute(query, data)

        result = mycursor.fetchall()
        bid = None

        if (result):
            for row in result:
                workSlotId, cafeStaffId, bidStatus, location, date, startTime, endTime, roleName, numOfStaff, username, staffRole, numOfWorkSlots, password, fullName, email, phoneNum, address, dateOfBirth, profileName, isSuspended= row

                if bid is None:
                    bid = Bid(
                        workSlot=WorkSlot(workSlotId, location, date, startTime, endTime, []),
                        staff=CafeStaff(cafeStaffId, CafeRole(staffRole), numOfWorkSlots, username, password, fullName, email, phoneNum, address, dateOfBirth, UserProfile(profileName), isSuspended),
                        bidStatus=bidStatus
                    )
                
                bid.workSlot.roleAssignments.append(RoleAssignment(CafeRole(roleName), numOfStaff))

            return bid
        else:
            return None

class WorkAssignment:
    def __init__(self, workSlot=None, staff=None, manager=None):
        self.workSlot = workSlot
        self.staff = staff
        self.manager = manager

    def assignWork(self, workAssignment):
        try:
            mycursor = mydb.cursor()
            query = "INSERT INTO work_assignment (work_slot_id, cafe_staff_id, manager_id) VALUES (%s, %s, %s)"
            data = (workAssignment.workSlot.workSlotId, workAssignment.staff.staffId, workAssignment.manager.managerId)
            mycursor.execute(query, data)

            mydb.commit()
            return True
        except Exception as e:
            print(f"Error assigning work: {e}")
            return False
        
    def viewAllWorkAssignments(self, staffId=None):
        mycursor = mydb.cursor()
        if (staffId == None):  #for manager view all bids
            query = '''
                    SELECT
                        wa.work_slot_id,
                        wa.cafe_staff_id,
                        wa.manager_id,
                        ws.location,
                        ws.work_date,
                        ws.start_time,
                        ws.end_time,
                        wscr.role_name,
                        wscr.num_of_staff,
                        cs.role_name AS staff_role_name,
                        cs.max_num_work_slots AS staff_max_work_slot,
                        cs.username AS staff_username,
                        ua_staff.password AS staff_password,
                        ua_staff.fullname AS staff_fullname,
                        ua_staff.email AS staff_email,
                        ua_staff.phone_no AS staff_phone_no,
                        ua_staff.address AS staff_address,
                        ua_staff.date_of_birth AS staff_date_of_birth,
                        ua_staff.profile_name AS staff_profile_name,
                        ua_staff.is_suspended AS staff_is_suspended,
                        cm.username AS manager_username,
                        ua_manager.password AS manager_password,
                        ua_manager.fullname AS manager_fullname,
                        ua_manager.email AS manager_email,
                        ua_manager.phone_no AS manager_phone_no,
                        ua_manager.address AS manager_address,
                        ua_manager.date_of_birth AS manager_date_of_birth,
                        ua_manager.profile_name AS manager_profile_name,
                        ua_manager.is_suspended AS manager_is_suspended
                    FROM
                        work_assignment wa
                    JOIN
                        work_slot ws ON wa.work_slot_id = ws.work_slot_id
                    LEFT JOIN
                        work_slot_cafe_role wscr ON ws.work_slot_id = wscr.work_slot_id
                    JOIN
                        cafe_staff cs ON wa.cafe_staff_id = cs.staff_id
                    JOIN
                        useraccount ua_staff ON cs.username = ua_staff.username
                    LEFT JOIN
                        cafe_manager cm ON wa.manager_id = cm.manager_id
                    LEFT JOIN
                        useraccount ua_manager ON cm.username = ua_manager.username
            '''
            mycursor.execute(query)

        else:   #for staff view all bids
            query = '''
                    SELECT
                        wa.work_slot_id,
                        wa.cafe_staff_id,
                        wa.manager_id,
                        ws.location,
                        ws.work_date,
                        ws.start_time,
                        ws.end_time,
                        wscr.role_name,
                        wscr.num_of_staff,
                        cs.role_name AS staff_role_name,
                        cs.max_num_work_slots AS staff_max_work_slot,
                        cs.username AS staff_username,
                        ua_staff.password AS staff_password,
                        ua_staff.fullname AS staff_fullname,
                        ua_staff.email AS staff_email,
                        ua_staff.phone_no AS staff_phone_no,
                        ua_staff.address AS staff_address,
                        ua_staff.date_of_birth AS staff_date_of_birth,
                        ua_staff.profile_name AS staff_profile_name,
                        ua_staff.is_suspended AS staff_is_suspended,
                        cm.username AS manager_username,
                        ua_manager.password AS manager_password,
                        ua_manager.fullname AS manager_fullname,
                        ua_manager.email AS manager_email,
                        ua_manager.phone_no AS manager_phone_no,
                        ua_manager.address AS manager_address,
                        ua_manager.date_of_birth AS manager_date_of_birth,
                        ua_manager.profile_name AS manager_profile_name,
                        ua_manager.is_suspended AS manager_is_suspended
                    FROM
                        work_assignment wa
                    JOIN
                        work_slot ws ON wa.work_slot_id = ws.work_slot_id
                    LEFT JOIN
                        work_slot_cafe_role wscr ON ws.work_slot_id = wscr.work_slot_id
                    JOIN
                        cafe_staff cs ON wa.cafe_staff_id = cs.staff_id
                    JOIN
                        useraccount ua_staff ON cs.username = ua_staff.username
                    LEFT JOIN
                        cafe_manager cm ON wa.manager_id = cm.manager_id
                    LEFT JOIN
                        useraccount ua_manager ON cm.username = ua_manager.username
                    WHERE
                        work_assignment.cafe_staff_id = %s;
            '''
            data = [staffId]
            mycursor.execute(query, data)
        
        result = mycursor.fetchall()

        workAssignments = {}
        for row in result:
            workSlotId, cafeStaffId, managerId, location, date, startTime, endTime, roleName, numOfStaff, staffRole, numOfWorkSlots, staffUsername, staffPassword, staffFullName, staffEmail, staffPhoneNum, staffAddress, staffDateOfBirth, staffProfileName, staffIsSuspended, managerUsername, managerPassword, managerFullName, managerEmail, managerPhoneNum, managerAddress, managerDateOfBirth, managerProfileName, managerIsSuspended = row

            if (workSlotId, cafeStaffId) not in workAssignments:
                workAssignments[(workSlotId, cafeStaffId)] = WorkAssignment(
                    workSlot=WorkSlot(workSlotId, location, date, startTime, endTime, []),
                    staff=CafeStaff(cafeStaffId, CafeRole(staffRole), numOfWorkSlots, staffUsername, staffPassword, staffFullName, staffEmail, staffPhoneNum, staffAddress, staffDateOfBirth, UserProfile(staffProfileName), staffIsSuspended),
                    manager=CafeManager(managerId, managerUsername, managerPassword, managerFullName, managerEmail, managerPhoneNum, managerAddress, managerDateOfBirth, UserProfile(managerProfileName), managerIsSuspended)
                )
            
            workAssignments[(workSlotId, cafeStaffId)].workSlot.roleAssignments.append(RoleAssignment(CafeRole(roleName), numOfStaff))

        return list(workAssignments.values())