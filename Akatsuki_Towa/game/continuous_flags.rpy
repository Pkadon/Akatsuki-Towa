default flags = {
    'zeiss_partner': 'tio',
    'gelato_ingredient': 'royal leaf',
}

define set_flags = {
    'avg10063': { # 10062 (中央工房の盗難事件(1) 3/10) Choice 1
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10064': { # 10062 (中央工房の盗難事件(1) 3/10) Choice 2
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg10067': { # 中央工房の盗難事件(1) 4/10~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10068': { # 中央工房の盗難事件(1) 4/10~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg10070': { # 中央工房の盗難事件(1) 5/10~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10071': { # 中央工房の盗難事件(1) 5/10~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg20104': { # 中央工房の盗難事件(1) 6/10~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg20103': { # 中央工房の盗難事件(1) 6/10~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg10072': { # 中央工房の盗難事件(1) 7/10~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10073': { # 中央工房の盗難事件(1) 7/10~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg10075': { # 中央工房の盗難事件(1) 8/10~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10074': { # 中央工房の盗難事件(1) 8/10~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg20106': { # 中央工房の盗難事件(1) 9/10~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg20107': { # 中央工房の盗難事件(1) 9/10~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg10076': { # 中央工房の盗難事件(1) 10/10~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10077': { # 中央工房の盗難事件(1) 10/10~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },


    'avg10078': { # 中央工房の盗難事件(2) 1/7~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10079': { # 中央工房の盗難事件(2) 1/7~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg10082': { # 中央工房の盗難事件(2) 2/7~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10083': { # 中央工房の盗難事件(2) 2/7~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg10086': { # 中央工房の盗難事件(2) 3/7~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10087': { # 中央工房の盗難事件(2) 3/7~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },

    'avg10088': { # 中央工房の盗難事件(2) 4/7~ティオ
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10092': { # 中央工房の盗難事件(2) 4/7~ティオ Choice 1
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10094': { # 中央工房の盗難事件(2) 4/7~ティオ Choice 2
        'flag': 'zeiss_partner',
        'value': 'tio'
    },
    'avg10089': { # 中央工房の盗難事件(2) 4/7~ティータ
        'flag': 'zeiss_partner',
        'value': 'tita'
    },
    'avg10093': { # 中央工房の盗難事件(2) 4/7~ティータ Choice 1
        'flag': 'zeiss_partner',
        'value': 'tita'
    },
    'avg10095': { # 中央工房の盗難事件(2) 4/7~ティータ Choice 2
        'flag': 'zeiss_partner',
        'value': 'tita'
    },


    'avg12416': { # 12415 (至高のジェラート) Choice 1
        'flag': 'gelato_ingredient',
        'value': 'royal leaf'
    },
    'avg12417': { # 12415 (至高のジェラート) Choice 2
        'flag': 'gelato_ingredient',
        'value': 'bellberry'
    },
    'avg12418': { # 12415 (至高のジェラート) Choice 3
        'flag': 'gelato_ingredient',
        'value': 'wasabi'
    },


}

define decline_list = [
    'avg20016', # 20014 (詐欺事件の調査（2） 2/8) Choice 2
    'avg22023', # 22021 (協会からの挑戦状 1/2) Choice 2
    'avg12103', # 12102 (未認可店舗の調査協力 1/10) Choice 2
    'avg12122', # 12121 (キルシェ通り・街道灯の交換 1/7) Choice 2
    'avg12153', # 12151 (エルベ離宮への荷物配達 1/4) Choice 2
    'avg20129', # 20127 (導力停止の異常事故(2) 6/14) Choice 2
    'avg10314', # 10311 (アルモリカ村の魔獣退治 1/4) Choice 2
    'avg10310', # 10308 (日曜学校の講師(経済編) 1/3) Choice 2
    'avg12376', # 12374 (海浜公園の手配魔獣 2/3) Choice 2
    'avg10404', # 10403 (クロスベルへの帰還) Choice 1
    'avg19022', # 19010 (ミシェル先生の特別レッスン unused ver) Choice 2
    'avg12232', # 12230 (ツァイス支部からの挑戦) Choice 2
    'avg25000', # multiple unused scenes
    'avg25026', # multiple unused scenes
    'avg25275', # unused scene (25273)
    'avg25309', # unused scene (25307)
]