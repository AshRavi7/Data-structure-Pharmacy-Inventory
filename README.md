Problem Statement

Apollo pharmacy store requires your assistance in implementing a medicine inventory tracker system. The objective is to keep a track of each product and also determine which ones to order if they are less than a specific quantity. In order to maintain this information, each drug has a unique identification number and a counter to keep a track of its available quantity in the system. Whenever a product moves in/out of the inventory its unique drug ID is recorded.
When a medicine is added to the inventory for the first time, the checkout counter is set to 1 and is considered a buy order. From then onwards, the counter is incremented for each subsequent entry of the same product is a buy and sell order. If the counter is odd, it means a buy order and if the counter is even, it means a sell order.
Every time when ‘x’ units of a drug/medicine are added into the inventory, its available count increases by ‘x’ value. On the other hand, when ‘x’ units of a medicine are ordered by customers, its available count reduces by ‘x’ in the inventory.
In addition to this a list of medicines less than a specific quantity ‘a’ and ordered at least once by the customers is prepared to determine by how many units these medicines have a supply shortage and needs to be ordered by the store.

The planning team uses the above system to answer the below questions:
1. List of distinct medicines added into the inventory and their currently available quantity.
2. List of medicines which are stocked out (all available quantities sold)
3. Determine the latest status of a particular medicine.
4. List of medicines that have moved in/out of the inventory more than ’z’ number of times.
5. List of all the medicines that have a supply shortage and by what quantity.

Requirements:
1. Implement the above problem statement in Python 3.7 using BINARY TREE ADT.
2. Perform an analysis for the questions above and give the running time in terms of input size: n.
The basic structure of the drug node will be:

Class DrugNode:
def __init__(self, Uid, availCount):
self.UId = Uid
self.avCount = availCount
self.chkoutCtr = 1

Operations:

1. def _readDrugList(self, DrugNode, Uid, availCount): This function reads the drug ids and the quantity available, bought and sold from the inputPS1.txt file. One drug id should be populated per line (in the input text file) along with the quantity separated by a comma. The input data is used to populate the tree.
If a medicine is already added to the tree, then the checkout counter is incremented for every subsequent occurrence of that medicine in the input file. If the counter is odd, it means a buy order and if the counter is even, it is a sell order. For each buy order its available counter increases by ‘x’ quantity while for each sell order the available counter is decremented by ‘x’ quantity.
Use a trigger function to call this recursive function from the root node.

Sample Input
111, 10
112, 6
113, 1
114, 25
112, 3
….
112, 2
114, 5
113, 1

2. def _updateDrugList(self, DrugNode, Uid, availCount): This function updates the existing inventory with drug ids and the quantity available, bought and sold from the promptsPS1.txt file. If the medicine is updated into the inventory for the first time, the checkout counter is set to 1. If the medicine is already added to the tree, then the checkout counter is incremented for the update occurrence of that medicine in the input file. If the counter is odd, it means a buy order and if the
counter is even, it is a sell order. For each buy order its available counter increases by ‘x’ quantity while for each sell order the available counter is decremented by ‘x’ quantity.
This function reads the drug id & its quantity from the promptsPS1.txt file to be updated in the system. The tag is shown below.
updateDrugList: 112, 2

3. def _printDrugInventory(self, DrugNode): The input should be read from the promptsPS1.txt file with the tag as shown below.
printDrugInventory
This function counts the distinct products and prints the list of drugs ids added into the inventory and the available quantity in outputPS1.txt. The output file should show:
Total number of medicines entered in the inventory: xx
111, 10
112, 5
113, 0
114, 20

Use a traversal method that displays the current inventory in ascending order of drug id
4. def _printStockOut(self, DrugNode): This function is triggered when the following tag is encountered in the promptsPS1.txt file
printStockOut
This function prints the medicines for which all the units have been sold and outputs the list into the outputPS1.txt file.
The following medicines are out of stock:
113

5. def _checkDrugStatus(self, DrugNode, Uid): This function reads the drug id from the promptsPS1.txt file to be searched for availability in the system. The drug id is mentioned with the tag as shown below.
checkDrugStatus: 114
The search function is called for every checkDrugStatus tag the program finds in the promptsPS1.txt file.
If the drug id is found with an odd checkout counter, the below string is output to the into the outputPS1.txt file
Drug id xx entered yy times into the system. Its last status was ‘buy’ and currently have zz units available
If the drug id is found with an even checkout counter, the below string is output to the into the outputPS1.txt file
Drug id xx entered yy times into the system. Its last status was ‘sell’ and currently have zz units available
If the drug id is found but stocked out, the below string is output into the outputPS1.txt file
All units of drug id xx have been sold
If the drug id is not found it outputs the below string into the outputPS1.txt file
Drug id xx does not exist.
Use a trigger function to call this recursive function from the root node.

6. def _highDemandDrugs(self, DrugNode, status, frequency): The function searches through the list of medicines and the checkout counter and lists the ones that have been bought/sold more than ‘z’ number of times. The buy/sell condition is determined by the status attribute of the prompt. The function is triggered when the following tag is encountered in the promptsPS1.txt file.
freqDemand: sell, 1
The function outputs the drug ids and their number of entries into the outputPS1.txt file as shown below.
Drugs with sell entries more than xx times are:
Drug id, checkout counter.
If no qualifying drug print: ‘No such drug id present in the system’
Use a trigger function to call this recursive function from the root node.

7. def _supplyShortage(self, DrugNode, minunits): This function prints the drug ids that have been ordered at least once by the customers and have a supply less than a specific quantity ‘a’. This is determined by the ‘minunits’ mentioned with the tag in promptsPS1.txt as shown below.
supplyShortage: 11
This function prints the list of drug ids that have a supply shortage and by how many units into the file outputPS1.txt.
If the minimum available units should be 11 the output file should show:
minunits: 11
Drugs with supply shortage:
112, 6
113, 11
Ensure that you use a traversal method that displays the sequence of drugs in ascending order of drug id.
Note that the input/output data shown here is only for understanding and testing, the actual file used for evaluation will be different.
Sample file formats
Sample Input file
Each row will have one drug id followed by the quantity separated by a comma. The input file name must be called inputPS1.txt.

Sample inputPS1.txt
111, 10
112, 6
113, 1
114, 25
112, 3
….
112, 2
114, 5
113, 1

Sample promptsPS1.txt
printDrugInventory
printStockOut
updateDrugList: 112, 2
printDrugInventory
checkDrugStatus: 114
checkDrugStatus: 111
freqDemand: sell, 1
supplyShortage: 11

Sample outputPS1.txt
------------- printDrugInventory ---------------
Total number of medicines entered in the inventory: 4
111, 10
112, 5
113, 0
114, 20
-----------------------------------------------
------------- printStockOut ---------------
The following medicines are out of stock:
113
-----------------------------------------------
------------- printDrugInventory ---------------
Total number of medicines entered in the inventory: 4
111, 10
112, 3
113, 0
114, 20
-----------------------------------------------
------------- checkDrugStatus:114 ---------------
Drug id 114 entered 2 times into the system. Its last status was ‘sell’ and currently have 20 units available
-----------------------------------------------
------------- checkDrugStatus:111 ---------------
Drug id 111 entered 1 time into the system. Its last status was ‘buy’ and have 10 units available
-----------------------------------------------
------------- freqDemand: Sell, 1 ---------------
Drugs with sell entries more than 1 times are:
112, 4
-----------------------------------------------
------------- supplyShortage: 11 ---------------
minunits: 11
Drugs with supply shortage:
112, 8

113, 11
-----------------------------------------------