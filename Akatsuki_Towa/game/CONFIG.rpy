init python early:

#################################################################
#Silver and gold "booktab" buttons used in all Scene Select menus
#################################################################
### Width of all silver and gold buttons (in pixels):
    tabwidth = 330
### Text size for all silver and gold buttons:
    tabtextsize = 20

####################################################
#"bookpage" buttons that play cutscenes when clicked
####################################################
### Height of all book page buttons (in pixels):
    pageheight = 80
### Text size for all book page buttons:
    pagetextsize = 18

################################################################
#The questlog window that appears when you click a "Log" button
################################################################
### Text size for all questlogs:
    logtextsize = 16




#=======================================================================================
#===================================TRANSLATION=========================================
#=======================================================================================
#=================================================================================================
# SCRIPT FILE (text.json)
# place file in game/MonoBehaviour folder
#=================================================================================================
### text.json file structure:

### {
###     textrowkey: [
###         {
###             textidkey: 1,
###             textkey: "TEXT1"
###         },
###         {
###             textidkey: 2,
###             textkey: "TEXT2"
###         }
###     ]
### }
#=================================================================================================
### CSV example file:

### textidkey,textkey
### 1,"TEXT1"
### 2,"TEXT2"
#=================================================================================================

### The name of the file containing the game's script
### The file may be a .json file or a .csv file
    textfilename = "text.json"

### The key used to access the list of rows in text.json
### (skip this if using a csv file)
    textrowkey = "_rows"

### The key used to access the id value in text.json 
### (for a csv file, use the header at the top of the column instead)
    textidkey = "_id"

### The key used to access the string value in text.json 
### (for a csv file, use the header at the top of the column instead)
    textkey = "_text"



#=================================================================================================
# AVG ROLE FILE (avg_role.json)
# place file in game/MonoBehaviour folder
#=================================================================================================
### avg_role.json file structure:
### {
###     namerowkey: [
###         {
###             nameidkey: 1,
###             namekey: "Nacht",
###             "_folderName": "",    # unused, can be omitted
###             "_scale": 0,          # unused
###             "_xPostion": 0        # unused
###         },
###         {
###             nameidkey: 2,
###             namekey: "Chloe"
###         }
###     ]
### }
#=================================================================================================
### CSV example file:
###
### nameidkey,namekey
### 1,"Nacht"
### 2,"Chloe"
#=================================================================================================

### The name of the file containing character names
### The file may be a .json file or a .csv file
    namefilename = "avg_role.json"

### The key used to access the list of rows in avg_role.json
### (skip this if using a csv file)
    namerowkey = "_rows"

### The key used to access the id value in avg_role.json 
### (for a csv file, use the header at the top of the column instead)
    nameidkey = "_id"

### The key used to access the roleName string value in avg_role.json
### (for a csv file, use the header at the top of the column instead)
    namekey = "_roleName"


##############
#EXTRA STRINGS
##############

#Quest Log
#==========================================
### The tags put before the quest name to denote whether is is a main quest or a side quest
    logmain = "[メイン]"
    logsub = "[サブ]"
### The headers used in the questlog menu before each field
    loglevel = "【推奨レベル】"
    logclient = "【依頼人】"
    logdetails = "【内容】"
    logbullet = "●"