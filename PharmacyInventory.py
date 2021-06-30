# DrugNode Class
class DrugNode(object):
    def __init__(self, UId, availCount):

        """
        Object Initialization. 
        Attributes:
            UId - Unique ID for each Medicine
            avCount - Availbale Count
            chkoutCtr - Checkout Counter. Odd for BUY, Even for SELL
                chkoutCtr is 1 for first time entry
            HBBST(AVL) related - left, right, height
        """
        self.UId = UId
        self.avCount = availCount
        self.chkoutCtr = 1
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):

    # Recursive function to insert each medicine UId in
    # subtree rooted with node and returns
    # new root of subtree.
    def _readDrugList(self, root, UId, availCount):

        """
        Function is called from the main function (Trigger)
        This is invoked for each entry of UID and Qunatity in the input file

        """
    
        # Step 1 - Perform normal BST
        if not root:
            global COUNT
            COUNT = COUNT + 1
            return DrugNode(UId, availCount)

        # Checking if the Medicine/UId already exist in the tree
        # If already Exists in Tree, the control will be passed to _updateDrugList function 
        elif (UId == root.UId):
            kk = self._updateDrugList(root, UId, availCount) 
            return root
        # Traverse either of right or left subtree depending on the value
        elif UId < root.UId:
            root.left = self._readDrugList(root.left, UId, availCount)
        else:
            root.right = self._readDrugList(root.right, UId, availCount)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                        self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and UId < root.left.UId:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and UId > root.right.UId:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and UId > root.left.UId:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and UId < root.right.UId:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # AVL Operation left rotate for Balancing the height 
    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        # Return the new root
        return y

    #AVL Operation right rotate for Balancing the height 
    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def _updateDrugList(self, DrugNode, UId, availCount):
        
        """
        The Function updates is called from 2 sources
            1) If the "updateDrugList" command found in promptsPS1.txt
            2) If the UId already exists while creation of nodes, then the control is passed to this function.
        
        Check the value of chkoutCtr
        If value the odd then - BUY Operation - Availabilty counter is incremented
        If value is even then - SELL Operation - Availabilty counter is decremented
        Traverse the tree - 1 Leg
                """
        # Counter to check if the node is found while traversing the tree
        #this is retuned back to the main function
        # If not found, then the _readDrugList function is called for adding the node in the tree
        counter = 0

        # Check if root node exists
        if not DrugNode:
            return counter

        # Check if the UId already exists in the tree by Travering the tree
        elif(UId == DrugNode.UId):
            
            # Incrementing the Check Counter, if node is found
            DrugNode.chkoutCtr = DrugNode.chkoutCtr + 1

            # Checking if counter value is add
            if (DrugNode.chkoutCtr % 2 != 0):
                
                #Buy - Increment available value
                DrugNode.avCount = DrugNode.avCount + availCount
                
            else:
                
                # Error handling for the case where sell quantity is greater than available
                if DrugNode.avCount >= availCount:
                    DrugNode.avCount = DrugNode.avCount - availCount
                else:
                    
                    print ("Sorry - Not Enough Quantities available to Sell -- From the coomand updateDrugList: {0}, {1}".format(UId, availCount))
                
            counter = 1
            return counter
        
        # Tree Traversal - Only 1 leg needs to traversed
        elif UId < DrugNode.UId:
            DrugNode.left = self._updateDrugList(DrugNode.left, UId, availCount)
            
        else:
            DrugNode.right = self._updateDrugList(DrugNode.right, UId, availCount)

    def _printDrugInventory(self, DrugNode):

        """
        This function is called when "printDrugInventory" commadn is found in promptsPS1.txt input file
        Function traverses through all the nodes of the tree and 
        prints all UId's with available quantity

        Note - Inorder traversal to get the node list in ascending order

        """
        if not DrugNode:
            return 
        global outputfile
        self._printDrugInventory(DrugNode.left)
        #count = count + 1
        print("{0} {1}".format(DrugNode.UId, DrugNode.avCount), file=outputfile)
        self._printDrugInventory(DrugNode.right)

    def  _printStockOut(self,  DrugNode):

        """
        This function is called when "printStockOut" commadn is found in promptsPS1.txt input file
        Function traverses through all the nodes of the tree and 
        prints all UId's with zero available
        
        """        
        global outputfile
        if not DrugNode:
            return 
        
        self._printStockOut(DrugNode.left)
        # Checking for availability
        if DrugNode.avCount == 0:
            print("{0}".format(DrugNode.UId), file=outputfile)
            
        self._printStockOut(DrugNode.right)

    def  _checkDrugStatus(self,  DrugNode,  UId):

        """
        This function is called when "checkDrugStatus" commadn is found in promptsPS1.txt input file
        Function traverses through all the nodes of the tree and 
        finds the status of the UId's in the input
        
        """ 
        
        # Counter to check if the UId is found or not
        global EXIST
        global outputfile
        if not DrugNode:
            return 
        EXIST = 0
        if DrugNode.UId == UId:

            # Check if UID exist but no availability
            if DrugNode.avCount == 0:
                print ("All units of drug id {0} have been sold".format(UId), file=outputfile)
                EXIST = 1
                return

            # If check counter is odd - then last action was a Buy
            elif (DrugNode.chkoutCtr % 2) != 0:
                print ("Drug id {0} entered {1} times into the system. Its last status was \‘buy\’ and currently have {2} units available".format(UId, DrugNode.chkoutCtr, DrugNode.avCount), file=outputfile)
                print ("-----------------------------------------------", file=outputfile)
                EXIST = 1
                return
            # If check counter is even - then last action was a sell
            elif (DrugNode.chkoutCtr % 2) == 0:
                print ("Drug id {0} entered {1} times into the system. Its last status was \‘sell\’ and currently have {2} units available".format(UId, DrugNode.chkoutCtr, DrugNode.avCount), file=outputfile)
                print ("-----------------------------------------------", file=outputfile)
                EXIST = 1
                return

        # Traverse either the left or right subtree depending on the value.        
        elif UId < DrugNode.UId:
            self._checkDrugStatus(DrugNode.left, UId)
        else:
             self._checkDrugStatus(DrugNode.right, UId)

    def _highDemandDrugs(self,  DrugNode,  status,  frequency):
        
        """
        This function is called when "freqDemand" command is found in promptsPS1.txt input file
        Function traverses through all the nodes of the tree and 
        finds the  UId's with sell and buy options > than the mentioned frequency in the input
        
        """

        if not DrugNode:
            return 
        
        # Creates a List of List for UID's and Check Counter Value.
        global lst
        lst1 = []

        # Left tree traversal
        self._highDemandDrugs(DrugNode.left, status,  frequency)

        # Check Counter value consist of both buy and sell. Get the number of sells and buy 
        if status == "sell" and DrugNode.chkoutCtr > ((frequency * 2) +1):
            lst1 = [DrugNode.UId, DrugNode.chkoutCtr]
            lst.append(lst1)

        elif status != "sell" and DrugNode.chkoutCtr > (frequency * 2):
            lst1 = [DrugNode.UId, DrugNode.chkoutCtr]
            lst.append(lst1)

        # Left tree traversal
        self._highDemandDrugs(DrugNode.right, status,  frequency)    

    def _supplyShortage(self,  DrugNode,  minunits):

        """
        The function traverses through the tree and finds nodes/UId's where 
        available units are less then the minimum units supplied in the input 

        """
        global outputfile
        if not DrugNode:
            return 
        
        self._supplyShortage(DrugNode.left, minunits)

        # Only gives the ouput if the medicine has been sold atleast once and 
        # availability is less than the minunits
        if (DrugNode.avCount < minunits) and (DrugNode.chkoutCtr > 1):
            print("{0}, {1}".format(DrugNode.UId, DrugNode.avCount), file=outputfile)

        self._supplyShortage(DrugNode.right, minunits)

## Global Variables      
my_file = open("inputPS1.txt", "r")
content_list = my_file.readlines()
myTree = AVL_Tree()
root = None
COUNT=0
EXIST = 0
lst = []
outputfile

# Main Method
def main():

    """
    Trigger function to invoke all methods mentioned in the problem statement

    """

    global my_file
    global content_list
    global myTree
    global root
    global COUNT
    global EXIST
    global lst
    global outputfile
    
    # Open and read the input file for creating the tree
    # If the UID already exists then update functioned is called
    my_file = open("inputPS1.txt", "r")
    content_list = my_file.readlines()
    myTree = AVL_Tree()
    root = None
    COUNT=0
    EXIST = 0
    lst = []

    open('outputPS1.txt', 'w').close()

    # As per the problem statement, all output needs to be redirected and saved in the output file
    outputfile = open("outputPS1.txt", "w")

    if not content_list:
        print("Empty Input File")

    # Extract each line of the input
    # Segragate the UID and available quantity supplied in input
    else:
        for line in content_list:
            if ',' in line:
                line.replace(" ","")
                UId, availCount = line.split(",")
                UId = int(UId)
                availCount = int(availCount)
                # Insert Node
                root=myTree._readDrugList(root, UId, availCount)
    # Read the 2nd input file with commands and instructions for the system.
    my_file = open("promptsPS1.txt", "r")
    content_list = my_file.readlines()

    if not content_list:
        print("Empty Input File", file=outputfile)

    # Read and Extract the input passed in each line of the input file
    # Call the appropriate function accordingly
    else:
        for line in content_list:
            line.replace(" ","")
            if "updateDrugList" in line:
                command, value = line.split(":")
                value.replace(" ","")
                UId, availCount = value.split(",")

                counter = myTree._updateDrugList(root, int(UId), int(availCount))
                if counter == 0:
                    root=myTree._readDrugList(root, int(UId), int(availCount))

            elif "printDrugInventory" in line:
                print ("------------- printDrugInventory ---------------", file=outputfile)            
                print ("Total number of medicines entered in the inventory: {0}".format(COUNT), file=outputfile )
                myTree._printDrugInventory(root)
                print ("-----------------------------------------------", file=outputfile)
            
            elif "printStockOut" in line:
                print ("------------- printStockOut ---------------", file=outputfile)
                print ("The following medicines are out of stock:", file=outputfile)
                myTree._printStockOut(root)
                print ("-----------------------------------------------", file=outputfile)

            elif "checkDrugStatus" in line:
                command, UId = line.split(":")
                print ("------------- checkDrugStatus:{0} ---------------".format(int(UId)), file=outputfile)
                myTree._checkDrugStatus(root, int(UId))
                if EXIST == 0:
                    print ("Drug id {0} does not exist.".format(int(UId)), file=outputfile)
                    print ("-----------------------------------------------", file=outputfile)

            elif "freqDemand" in line:

                command, value = line.split(":")
                value.replace(" ","")
                status, frequency = value.split(",")
                print ("------------- freqDemand: {0}, {1} ---------------".format(status, int(frequency)), file=outputfile)
                myTree._highDemandDrugs(root,  status,  int(frequency))
                if any(lst) is None:
                    print ("No such drug id present in the system", file=outputfile)
                else:
                    print ("Drugs with {0} entries more than {1} times are:".format(status, int(frequency)), file=outputfile)
                    for i in lst:
                        a=int(i[0])
                        b=int(i[1])
                        print (a, b, file=outputfile)
                print ("-----------------------------------------------", file=outputfile)

            elif "supplyShortage" in line:
                command, minunits = line.split(":")
                print ("------------- supplyShortage: {0} ---------------".format(int(minunits)), file=outputfile)
                print ("minunits: {0}".format(int(minunits)), file=outputfile)
                print ("Drugs with supply shortage:", file=outputfile)
                myTree._supplyShortage(root, int(minunits))
                print ("-----------------------------------------------", file=outputfile)
            
            else:
                print ("Incorrect Input Format", file=outputfile)

    # Close Output File
    outputfile.close()
    
 # Cals to main function       
if __name__=="__main__":
    main()



