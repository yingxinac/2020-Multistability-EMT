# 2020-Multistability-EMT

### Results of the simulations for our EMT databases are summarized in the tables in the spreadsheet "SpreadSheets.xlsx", which includes five tabs:
 --"ALLE": results for the database with all the nodes in our EMT network essential
 --"Snail1": results for the database with only the node Snail1 inessential
 --"Ovol2": results for the database with only the node Ovol2 inessential
 --"TGFb": results for the database with only the node TGFb inessential
 --"Zeb1": results for the database with only the node Zeb1 inessential
The meanings of the data summarized in these tables are specified in the headlines of them. 

# Methods: 
## [Part 1: Creating a database for a network]
### STEPS: 
STEP1: Installing the software DSGRN.  Instructions can be found at https://github.com/shaunharker/DSGRN and https://dsgrn.readthedocs.io/en/latest/
       
STEP2: Specify the network for which DSGRN database needs to  be computed in a .txt file.  
       Examples can be found in: EMT.txt, EMT_Ovol2notE.txt, EMT_Snail1notE.txt, EMT_TGFbnotE.txt, EMT_Zeb1notE.txt.
       
STEP3: Create a database for the specified network using DSGRN.  Instructions can be found here:           https://dsgrn.readthedocs.io/en/latest/signatures.html
       Here we quote from the above link: "Signatures is a program which computes databases of Morse graphs for an entire Parameter            graph. Here is a demonstration.  
       First, we use the Signatures program to create an SQLite database. From the DSGRN folder, type:
       > mpiexec -np 5 Signatures networks/2D_Example_C.txt ./2D_Example_C.db".  
       In " > mpiexec -np 5 Signatures networks/2D_Example_C.txt ./2D_Example_C.db":
       -- "5" is the number of cores that will be used in this job
       -- "networks/2D_Example_C.txt" is the .txt file specifying the network of interest from STEP2
       -- "./2D_Example_C.db" specifies the file name of the database.

## [Part2: Computing data needed for the Figures in our EMT database query]
### Remarks:
#Remark 1: When switching to a different database, one needs to change the database file used in  "PointLayers.py" first.
Then, when using
"PointLayers.py",
"ExactlyNstable.py",
"MonoEM_in_HexLayers.py",
"EMoccur_in_HexLayers.py",
"PlayersMono_in_HexLayers.py",
"Psoccur_in_HexLayers.py",
"Nstable_in_Hexlayers.py",
"Nstable_EM_in_Hexlayers.py" and
"Mono_at_FPs.py",
one needs to make modifications according to the database file being used.  
Places in each script where modifications need to be made are indicated with "###****** modifications ******###" at the end of those lines.  
For example, when using the database file "Zeb1notE.db", but used "Ovol2notE.db" before, then one needs to change all the "Ovol2" into "Zeb1" in those lines.
Details on what each script does is inside those scripts.

#Remark 2: Hex codes -- details can be found at https://dsgrn.readthedocs.io/en/latest/parameters.html

#Remark 3: "HexLayers", "HexcodeLayer", "HexcodeLayers", "hexlayers" and other similar terms in the file names and the codes, can be understood as a set of hex codes corresponding to a parameter graph layer.

#Remark4: FP layer -- a FP layer is a set of FPs on the projection of the states in the six-dimensional phase space of the EMT network to three dimensions corresponding to Zeb1, Snail1 and Ovol2, with a particular fixed Hamming distance from the extreme values representing E and M states.

### STEPS (Take the Zeb1 case as an example): 
STEP1: Run "ExactlyNstable.py" -- get some basic information about the network of interest.
       (For different databases, choose the input database file in the line "database = DSGRN.Query.Database.Database("....db")" 
        according to the database being used.  In this case, write "database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db")")

STEP2: Modify "PointLayers.py". 
       (For different databases, choose the input database file in the line "database = DSGRN.Query.Database.Database("....db")" 
        according to the database being used.  In this case, write "database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db")")

STEP3: Get the list of Zeb1 hex codes and the factor parameter graph structure, so that we know how many parameter graph layers there          are, and which hex codes are included in each layer.
       (Use DSGRN directly: SingleGeneQuery(Database("EMT_Zeb1notE.db"), "Zeb1")(0))

STEP4: According to the information from STEP3, create "Zeb1HexcodeLayers.py".  
       (Examples: "Ovol2HexcodeLayer.py", "Snail1HexcodeLayer.py", "TGFbHexcodeLayer.py", "Zeb1HexcodeLayer.py")

STEP5: Run "MonoEM_in_HexLayers.py" and save the outputs -- get the number of parameter nodes with monostable at E/M state in each              parameter graph layer.
       (For different databases, choose the input database file in the line "database = DSGRN.Query.Database.Database("....db")" 
        according to the database being used.  In this case, write "database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db")")
       (Also choose the input for "hexlayers" variale in the line " import ...HexcodeLayers
                                                                  hexlayers = ...HexcodeLayers...._layers" accordingly.
        In this case, write "import Zeb1HexcodeLayers
                             hexlayers = Zeb1HexcodeLayers.zeb1_layers") 
     
STEP6: Run "EMoccur_in_HexLayers.py" and save the outputs -- get the number of parameter nodes with the occurrence of E/M state in each        parameter graph layer.
       (For different databases, choose the input database file in the line "database = DSGRN.Query.Database.Database("....db")" 
        according to the database being used.  In this case, write "database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db")")
       (Also choose the input for "hexlayers" variale in the line " import ...HexcodeLayers
                                                                  hexlayers = ...HexcodeLayers...._layers" accordingly.
        In this case, write "import Zeb1HexcodeLayers
                             hexlayers = Zeb1HexcodeLayers.zeb1_layers") 
STEP7: Run "PlayersMono_in_HexLayers.py" and save the outputs -- get the number of parameter nodes in each parameter graph layer at            which the network is monostable at each FP layer.
       (For different databases, choose the input database file in the line "database = DSGRN.Query.Database.Database("....db")" 
        according to the database being used.  In this case, write "database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db")")
       (Also choose the input for "hexlayers" variale in the line " import ...HexcodeLayers
                                                                  hexlayers = ...HexcodeLayers...._layers" accordingly.
        In this case, write "import Zeb1HexcodeLayers
                             hexlayers = Zeb1HexcodeLayers.zeb1_layers")  

STEP8: Run "Psoccur_in_HexLayers.py" and save the outputs -- get the number of parameter nodes in each parameter graph layer with the          occurrence of each FP layer.
       (Need to choose the input for "hexlayers" variale in the line " import ...HexcodeLayers
                                                                     hexlayers = ...HexcodeLayers...._layers" according to the database         being used.  In this case, write "import Zeb1HexcodeLayers
                                   hexlayers = Zeb1HexcodeLayers.zeb1_layers")

STEP9: Run "Nstable_in_Hexlayers.py" and save the outputs -- get the number of parameter nodes in each parameter graph layer with N            fixed points in phase space, for all N.
       (For different databases, choose the input database file in the line "database = DSGRN.Query.Database.Database("....db")" 
        according to the database being used.  In this case, write "database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db")")
       (Also choose the input for "hexlayers" variale in the line " import ...HexcodeLayers
                                                                  hexlayers = ...HexcodeLayers...._layers" accordingly.
        In this case, write "import Zeb1HexcodeLayers
                             hexlayers = Zeb1HexcodeLayers.zeb1_layers") 
#"Nstable_EM_in_Hexlayers.py" and "Mono_at_FPs.py" are optional, which are not necessary for our current purposes.


