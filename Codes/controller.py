import entity

# User Account related Controllers
class LoginController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def userLogin(self, username, password):
        return self.userAccount.login(username, password)

class ChangePwController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def changePassword(self, username, oldPw, newPw):
        return self.userAccount.changePw(username, oldPw, newPw)

class CreateUserAccController:
    def __init__(self):
        self.userAccount = entity.UserAccount()

    def createUserAccount(self, userAcc):
        return self.userAccount.createUserAcc(userAcc)
    
class ViewAllUserAccController:
    def __init__(self):
        self.userAccount = entity.UserAccount()
    
    def viewAllUserAcc(self):
        return self.userAccount.viewAllAcc()
    
class UpdateUserAccController:
    def __init__(self):
        self.userAccount = entity.UserAccount()
    
    def updateUserAcc(self, username, userAcc):
        return self.userAccount.updateUserAcc(username, userAcc)
    
class SuspendUserAccController:
    def __init__(self):
        self.userAccount = entity.UserAccount()
    
    def suspendUserAcc(self, username):
        return self.userAccount.suspendUserAcc(username)
    
class SearchUserAccController:
    def __init__(self):
        self.userAccount = entity.UserAccount()
    
    def searchUserAcc(self, username):
        return self.userAccount.searchUserAcc(username)
    

# User Profile related controllers    
class CreateUserProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()

    def createUserProfile(self, userProfile):
        return self.userProfile.createUserProfile(userProfile)
    
class ViewAllUserProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()
    
    def viewAllUserProfile(self):
        return self.userProfile.viewAllProfile()
    
class UpdateUserProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()
    
    def updateUserProfile(self, profileName, userProfile):
        return self.userProfile.updateUserProfile(profileName, userProfile)
    
class SuspendUserProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()
    
    def suspendUserProfile(self, profileName):
        return self.userProfile.suspendUserProfile(profileName)

class SearchUserProfileController:
    def __init__(self):
        self.userProfile = entity.UserProfile()
    
    def searchUserProfile(self, profileName):
        return self.userProfile.searchUserProfile(profileName)
    

# Staff related controllers
class ChooseCafeRoleController:
    def __init__(self):
        self.cafeStaff = entity.CafeStaff()
    
    def chooseCafeRole(self, staffId, roleName):
        return self.cafeStaff.chooseCafeRole(staffId, roleName)
    
class ChooseMaxWorkSlotController:
    def __init__(self):
        self.cafeStaff = entity.CafeStaff()
    
    def chooseMaxWorkSlot(self, staffId, numOfWorkSlots):
        return self.cafeStaff.chooseMaxWorkSlot(staffId, numOfWorkSlots)
    
class ViewAllStaffsController:
    def __init__(self):
        self.cafeStaff = entity.CafeStaff()
    
    def viewAllStaffs(self):
        return self.cafeStaff.viewAllStaffs()
    
    
# Work Slot related controllers
class CreateWorkSlotController:
    def __init__(self):
        self.workSlot = entity.WorkSlot()
    
    def createWorkSlot(self, workSlot):
        return self.workSlot.createWorkSlot(workSlot)
    
class ViewAllWorkSlotsController:
    def __init__(self):
        self.workSlot = entity.WorkSlot()
    
    def viewAllWorkSlots(self):
        return self.workSlot.viewAllWorkSlots()

class UpdateWorkSlotController:
    def __init__(self):
        self.workSlot = entity.WorkSlot()
    
    def updateWorkSlot(self, workSlot):
        return self.workSlot.updateWorkSlot(workSlot)
    
class DeleteWorkSlotController:
    def __init__(self):
        self.workSlot = entity.WorkSlot()
    
    def deleteWorkSlot(self, workSlotId):
        return self.workSlot.deleteWorkSlot(workSlotId)
    
class SearchWorkSlotController:
    def __init__(self):
        self.workSlot = entity.WorkSlot()
    
    def searchWorkSlot(self, workSlotId):
        return self.workSlot.searchWorkSlot(workSlotId)
    

# Bid related controller
class CreateBidController:
    def __init__(self):
        self.bid = entity.Bid()
    
    def createBid(self, bid):
        return self.bid.createBid(bid)
    
class ViewAllBidsController:
    def __init__(self):
        self.bid = entity.Bid()
    
    def viewAllBids(self, staffId=None):
        return self.bid.viewAllBids(staffId)

class DeleteBidController:
    def __init__(self):
        self.bid = entity.Bid()
    
    def deleteBid(self, workSlotId, staffId):
        return self.bid.deleteBid(workSlotId, staffId)
    
class ApproveBidController:
    def __init__(self):
        self.bid = entity.Bid()
    
    def approveBid(self, workSlotId, staffId):
        return self.bid.approveBid(workSlotId, staffId)
    
class RejectBidController:
    def __init__(self):
        self.bid = entity.Bid()
    
    def rejectBid(self, workSlotId, staffId):
        return self.bid.rejectBid(workSlotId, staffId)
    
class SearchBidController:
    def __init__(self):
        self.bid = entity.Bid()
    
    def searchBid(self, workSlotId, staffId):
        return self.bid.searchBid(workSlotId, staffId)
    

# Work Assignment related controller
class AssignWorkController:
    def __init__(self):
        self.workAssignment = entity.WorkAssignment()
    
    def assignWork(self, workAssignment):
        return self.workAssignment.assignWork(workAssignment)
    
class ViewAllWorkAssignmentsController:
    def __init__(self):
        self.workAssignment = entity.WorkAssignment()
    
    def viewAllWorkAssignments(self, staffId=None):
        return self.workAssignment.viewAllWorkAssignments(staffId)


    
    
## Create work slot test
# roleAssignment1 = entity.RoleAssignment(entity.CafeRole("chef"), 3)
# roleAssignment2 = entity.RoleAssignment(entity.CafeRole("waiter"), 1)
# roleAssignment3 = entity.RoleAssignment(entity.CafeRole("cashier"), 2)
# workSlot = entity.WorkSlot(location="Clementi", date="2023-12-18", startTime="9:00", endTime="17:00", roleAssignments=[roleAssignment1, roleAssignment2, roleAssignment3])
# wsController = CreateWorkSlotController()
# print(wsController.createWorkSlot(workSlot))

## View all work slot test
# viewallwsController = ViewAllWorkSlotController()
# wslist = viewallwsController.viewAllWorkSlot()
# for ws in wslist:
#     print(f"id: {ws.workSlotId} \nlocation: {ws.location} \ndate: {ws.date} \nstartTime: {ws.startTime} \nendTime: {ws.endTime} \n")
#     for roleAssignment in ws.roleAssignments:
#         print(f"roleName: {roleAssignment.role.roleName}\nnumOfStaff: {roleAssignment.numOfStaff}\n")

## Search work slot test
# searchwsController = SearchWorkSlotController()
# ws = searchwsController.searchWorkSlot(4)

# print(f"id: {ws.workSlotId} \nlocation: {ws.location} \ndate: {ws.date} \nstartTime: {ws.startTime} \nendTime: {ws.endTime} \n")
# for roleAssignment in ws.roleAssignments:
#     print(f"roleName: {roleAssignment.role.roleName}\nnumOfStaff: {roleAssignment.numOfStaff}\n")

## Update work slot test
# roleAssignment1 = entity.RoleAssignment(entity.CafeRole("chef"), 1)
# roleAssignment2 = entity.RoleAssignment(entity.CafeRole("waiter"), 1)
# roleAssignment3 = entity.RoleAssignment(entity.CafeRole("cashier"), 3)
# workSlot = entity.WorkSlot(4, location="City Hall", date="2023-12-18", startTime="9:00", endTime="17:00", roleAssignments=[roleAssignment1, roleAssignment2, roleAssignment3])
# updatewsController = UpdateWorkSlotController()
# print(updatewsController.updateWorkSlot(workSlot))

## Delete work slot test
# deletewsController = DeleteWorkSlotController()
# ws = deletewsController.deleteWorkSlot(4)
# print(ws)

# userAcc = LogInController.userLogIn("admin", "123456")
# userAcc.create_user_account("staff", "23456", "123@gmail.com", "0987", "21march", "cafe_staff")

# entity.SystemAdmin.create_user_account()
