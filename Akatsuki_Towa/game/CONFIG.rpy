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

#Menu Buttons
#==========================================
### Back button text
    backtext = "Back"
### Jump button text
    jumptext = "Jump"
### Sprite test button text
    spritetext = "Sprite"
### Log button text
    logtext = "Log"

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

#Menu Strings
#Almost all other text used throughout the menus, that could not be sourced from the original script file
    extextdict = {
    "ex_1": "Optional Dialogue",
    "ex_2": "Extra Dialogue",
    "ex_3": "Extra/Unused",
    "ex_4": "exact timing unknown",
    "ex_5": "Unused Tio Version",
    "ex_6": "Unused Tita Version",
    "ex_7": "Unused Alt Version",
    "ex_8": "Unused Ending",
    "ex_9": "(2 questions correct)",
    "ex_10": "(1 or no questions correct)",
    "ex_11": "Conditional Dialogue",
    "ex_12": "Quest Complete",
    "ex_13": "Quest Complete (Unused)",
    "ex_14": "Unused",
    "ex_15": "Conditional Dialogue (Unused)",
    "ex_16": "Unused Scenes",
    "ex_17": "Fishing",
    "ex_18": "Fishing Unlock Scene",
    "ex_19": "(Prologue)",
    "ex_20": "Fisherman's Guild",
    "ex_21": "(Grancel, Chapter 1)",
    "ex_100": "受付嬢トリア",
    "ex_101": "スラッシュ",
    "ex_102": "キャンベル議員",
    "ex_103": "フェルナンド",
    "ex_104": "スラッシュ/ヒューイ",
    "ex_105": "リン/エオリア",
    "ex_106": "ティータ",
    "ex_107": "カルノー/プロメテ",
    "ex_108": "マードック工房長",
    "ex_109": "ウォン/グンドルフ",
    "ex_110": "ジリアン/ロナード",
    "ex_200": "中央工房の盗難事件(2) 3/7",
    "ex_201": "準遊撃士・ナハトの奮闘記",
    "ex_202": "Vol.1-エオリア編",
    "ex_203": "Vol.1-ヴェンツェル編",
    "ex_204": "Vol.1-スコット編",
    "ex_205": "Vol.1-リン編",
    "ex_206": "Vol.2 アネラス編",
    "ex_207": "Vol.3 ノエル編",
    "ex_208": "Vol.4 ティータ編",
    "ex_209": "Vol.5 ミレイユ編",
    "ex_210": "Vol.6 ヨシュア編",
    "ex_211": "Vol.7 エリィ編",
    "ex_212": "Vol.8 エステル編",
    "ex_213": "Vol.9 ティオ編",
    "ex_214": "Vol.10 ランディ編",
    "ex_215": "Vol.11 ロイド編",
    "ex_216": "Vol.12 レン編",
    "ex_217": "Vol.13 カシウス編",
    "ex_218": "Vol.14 ユリア編",
    "ex_219": "Vol.15 アガット編",
    "ex_220": "Vol.16 グラッツ編",
    "ex_221": "Vol.17 シェラザード編",
    "ex_222": "Vol.18 クローゼ編",
    "ex_223": "Vol.19 ギルバート編",
    "ex_224": "Vol.20 クルツ編",
    "ex_225": "Vol.21 カルナ編",
    "ex_226": "Vol.22 ダドリー編",
    "ex_227": "Vol.23 アリオス編",
    "ex_228": "Vol.24 リシャール編",
    "ex_229": "Vol.25 キール編",
    "ex_230": "Vol.26 ジョゼット編",
    "ex_231": "Vol.27 ドルン編",
    "ex_232": "Vol.28 ミシェル編",
    "ex_233": "EX.1　リース編",
    "ex_234": "EX.2 ケビン編",
    "ex_235": "ミシェル先生の特別レッスン",
    "ex_236": "歩んでいく道の途中で",
    "ex_237": "試験班の夏休み",
    "ex_238": "第１回《ハロウィンフェス》",
    "ex_239": "絵空の記憶",
    "ex_240": "作者：藤７８\n(2017.12 グランプリ受賞作品)",
    "ex_241": "作者：トム6W\n(2017.12 準グランプリ受賞作品)",
    "ex_242": "作者：月紅\n(2017.12 ブレイサー賞受賞作品)",
    "ex_243": "新米遊撃士のクリスマス",
    "ex_244": "Heroes War！",
    "ex_300": "毎日討伐",
    "ex_301": "ダルモア商会の依頼",
    "ex_302": "ラッセル博士の依頼",
    "ex_303": "リラの依頼",
    "ex_304": "マオ婆さんの依頼",
    "ex_305": "メイベルの依頼",
    "ex_306": "ホテル《ローエンバウム》の依頼",
    "ex_307": "クロスベル警察学校の依頼",
    "ex_308": "イメルダ夫人の依頼",
    "ex_309": "ウルスラ病院の依頼",
    "ex_310": "《リジョンフード》の依頼",
    "ex_311": "アルモリカ村の依頼",
    "ex_312": "《ホテル・ミレニアム》の依頼",
    "ex_313": "マイヤの依頼",
    "ex_314": "マルクの依頼",
    "ex_315": "ドナートの依頼",
    "ex_116": "カヌートの依頼",
    "ex_117": "セナの依頼",
    "ex_118": "クリントの依頼",
    "ex_119": "ルーシーの依頼",
    "ex_120": "モーリスの依頼"
}
