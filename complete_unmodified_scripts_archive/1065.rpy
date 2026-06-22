label avg1065:

$ play_music("ed7113.ogg")
scene avg_bg_021
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(2101206)]' (**arg(1, 2101206))
get_char('c0') '[convertstrid(2101207)]' (**arg(2, 2101207))
$ update_portrait('sc058_01 5', 'p63', [l(-20), light, flip], 6)
get_char('c631') '[convertstrid(2101208)]' (**arg(3, 2101208))
$ update_portrait('sc058_01 5', 'p63', [l(-20), dark, flip], 5)
$ update_portrait('st005_01 2', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101209)]' (**arg(4, 2101209))
$ update_portrait('st005_01 2', 'p205', [r(4), dark], 5)
$ update_portrait('sc058_01 1', 'p63', [l(-20), light, flip], 6)
get_char('c631') '[convertstrid(2101210)]' (**arg(5, 2101210))
$ update_portrait('sc058_01 1', 'p63', [l(-20), dark, flip], 5)
$ update_portrait('st005_01 3', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101211)]' (**arg(6, 2101211))
$ update_portrait('st005_01 3', 'p205', [r(4), dark], 5)
$ update_portrait('sc058_01 5', 'p63', [l(-20), light, flip], 6)
get_char('c631') '[convertstrid(2101212)]' (**arg(7, 2101212))
$ update_portrait('sc058_01 5', 'p63', [l(-20), dark, flip], 5)
$ update_portrait('st005_01 1', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101213)]' (**arg(8, 2101213))
$ update_portrait('st005_01 1', 'p205', [r(4), dark], 5)
$ update_portrait('sc058_01 1', 'p63', [l(-20), light, flip], 6)
get_char('c631') '[convertstrid(2101214)]' (**arg(9, 2101214))
$ update_portrait('sc058_01 1', 'p63', [l(-20), dark, flip], 5)
$ update_portrait('st005_01 4', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101215)]' (**arg(10, 2101215))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2101216)]' (**arg(11, 2101216))
get_char('c0') '[convertstrid(2101217)]' (**arg(12, 2101217))
scene avg_bg_025
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
$ update_narrator('c2021')
with fade
get_char('c2021') '[convertstrid(2101218)]' (**arg(13, 2101218))
$ update_portrait('st002_01 4', 'p202', [l(-9), dark, flip], 5)
get_char('c25113') '[convertstrid(2101219)]' (**arg(14, 2101219))
hide p202
get_char('c25071') '[convertstrid(2101220)]' (**arg(15, 2101220))
get_char('c0') '[convertstrid(2101221)]' (**arg(16, 2101221))
get_char('c0') '[convertstrid(2101222)]' (**arg(17, 2101222))
$ update_portrait('sc058_01 4', 'p63', [l(-20), light, flip], 6)
get_char('c631') '[convertstrid(2101223)]' (**arg(18, 2101223))
$ update_portrait('sc058_01 4', 'p63', [l(-20), dark, flip], 5)
$ update_portrait('st005_01 3', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101224)]' (**arg(19, 2101224))
hide p63
$ update_portrait('st005_01 3', 'p205', [r(4), dark], 5)
get_char('c25101') '[convertstrid(2101225)]' (**arg(20, 2101225))
hide p205
get_char('c25123') '[convertstrid(2101226)]' (**arg(21, 2101226))
$ update_portrait('st005_01 3', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101227)]' (**arg(22, 2101227))
$ update_portrait('st005_01 3', 'p205', [r(4), dark], 5)
$ update_portrait('sc058_01 1', 'p63', [l(-20), light, flip], 6)
get_char('c631') '[convertstrid(2101228)]' (**arg(23, 2101228))
$ update_portrait('sc058_01 1', 'p63', [l(-20), dark, flip], 5)
$ update_portrait('st005_01 2', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101229)]' (**arg(24, 2101229))
hide p63
hide p205
get_char('c0') '[convertstrid(2101230)]' (**arg(25, 2101230))
stop music
get_char('c0') '[convertstrid(2101231)]' (**arg(26, 2101231))
$ play_music("ed7151.ogg")
$ update_portrait('st005_01 4', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101232)]' (**arg(27, 2101232))
hide p205
play sfx2 "fight_6010.ogg"
get_char('c0') '[convertstrid(2101233)]' (**arg(28, 2101233)) with shake
$ update_portrait('sc058_01 2', 'p63', [l(-20), light, flip], 6)
get_char('c631') '[convertstrid(2101234)]' (**arg(29, 2101234))
hide p63
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101235)]' (**arg(30, 2101235))
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101236)]' (**arg(31, 2101236))
$ update_portrait('st002_01 4', 'p202', [l(-9), dark, flip], 5)
$ update_portrait('st005_01 3', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101237)]' (**arg(32, 2101237))
$ update_portrait('st005_01 3', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101238)]' (**arg(33, 2101238))
hide p202
$ update_portrait('st005_01 3', 'p205', [r(4), dark], 5)
get_char('c25061') '[convertstrid(2101239)]' (**arg(34, 2101239))
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101240)]' (**arg(35, 2101240))
$ update_portrait('st002_01 4', 'p202', [l(-9), dark, flip], 5)
$ update_portrait('st005_01 4', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101241)]' (**arg(36, 2101241))
hide p205
$ update_portrait('sc058_01 4', 'p63', [r(-20), light], 6)
get_char('c633') '[convertstrid(2101242)]' (**arg(37, 2101242))
$ update_portrait('sc058_01 4', 'p63', [r(-20), light], 6)
get_char('c633') '[convertstrid(2101243)]' (**arg(38, 2101243))
$ update_portrait('sc058_01 4', 'p63', [r(-20), dark], 5)
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101244)]' (**arg(39, 2101244))
hide p63
$ update_portrait('st002_01 4', 'p202', [l(-9), dark, flip], 5)
$ update_portrait('st005_01 3', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101245)]' (**arg(40, 2101245))
hide p205
get_char('c25043') '[convertstrid(2101246)]' (**arg(41, 2101246))
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101247)]' (**arg(42, 2101247))
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101248)]' (**arg(43, 2101248))
$ update_portrait('st002_01 4', 'p202', [l(-9), dark, flip], 5)
get_char('c25043') '[convertstrid(2101249)]' (**arg(44, 2101249))
stop music
hide p202
get_char('c25061') '[convertstrid(2101250)]' (**arg(45, 2101250))
$ play_music("ed7500.ogg")
get_char('c0') '[convertstrid(2101251)]' (**arg(46, 2101251))
get_char('c0') '[convertstrid(2101252)]' (**arg(47, 2101252))
get_char('c0') '[convertstrid(2101253)]' (**arg(48, 2101253))
get_char('c0') '[convertstrid(2101254)]' (**arg(49, 2101254))
get_char('c0') '[convertstrid(2101255)]' (**arg(50, 2101255))
get_char('c0') '[convertstrid(2101256)]' (**arg(51, 2101256))
get_char('c0') '[convertstrid(2101257)]' (**arg(52, 2101257))
play sfx2 "other_7063.ogg"
get_char('c0') '[convertstrid(2101258)]' (**arg(53, 2101258))
get_char('c0') '[convertstrid(2101259)]' (**arg(54, 2101259))
$ update_portrait('st005_01 5', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101260)]' (**arg(55, 2101260))
hide p205
get_char('c0') '[convertstrid(2101261)]' (**arg(56, 2101261))
stop music
get_char('c0') '[convertstrid(2101262)]' (**arg(57, 2101262))
$ update_portrait('st002_01 3', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101263)]' (**arg(58, 2101263))
$ update_portrait('st002_01 3', 'p202', [l(-9), dark, flip], 5)
$ update_portrait('st005_01 3', 'p205', [r(4), light], 6)
get_char('c2053') '[convertstrid(2101264)]' (**arg(59, 2101264))
$ update_portrait('st005_01 3', 'p205', [r(4), dark], 5)
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101265)]' (**arg(60, 2101265))
$ update_portrait('st002_01 4', 'p202', [l(-9), light, flip], 6)
get_char('c2021') '[convertstrid(2101266)]' (**arg(61, 2101266))
return