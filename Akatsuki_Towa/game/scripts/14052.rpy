label avg14052(trans=fade_in):

$ play_music("ED6100.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1203033)]' (**arg(1, 1203033))
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7047.ogg"
get_char('c23') '[convertstrid(1203034)]' (**arg(2, 1203034))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c12021') '[convertstrid(1203035)]' (**arg(3, 1203035))
get_char('c12021') '[convertstrid(1203036)]' (**arg(4, 1203036))
get_char('c12021') '[convertstrid(1203037)]' (**arg(5, 1203037))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1203038)]' (**arg(6, 1203038))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
get_char('c12021') '[convertstrid(1203039)]' (**arg(7, 1203039))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1203040)]' (**arg(8, 1203040))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12021') '[convertstrid(1203041)]' (**arg(9, 1203041))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1203042)]' (**arg(10, 1203042))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1203043)]' (**arg(11, 1203043))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c12021') '[convertstrid(1203044)]' (**arg(12, 1203044))
get_char('c12021') '[convertstrid(1203045)]' (**arg(13, 1203045))
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1203046)]' (**arg(14, 1203046))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
get_char('c12021') '[convertstrid(1203047)]' (**arg(15, 1203047))
stop music
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1203048)]' (**arg(16, 1203048))
$ play_music("ed7124.ogg")
scene avg_bg_059
$ update_narrator('c23')
with fade
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7047.ogg"
get_char('c23') '[convertstrid(1203049)]' (**arg(17, 1203049))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c12561') '[convertstrid(1203050)]' (**arg(18, 1203050))
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1203051)]' (**arg(19, 1203051))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
get_char('c12561') '[convertstrid(1203052)]' (**arg(20, 1203052))
hide p2
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1203053)]' (**arg(21, 1203053))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
get_char('c12561') '[convertstrid(1203054)]' (**arg(22, 1203054))
get_char('c12561') '[convertstrid(1203055)]' (**arg(23, 1203055))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1203056)]' (**arg(24, 1203056))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1203057)]' (**arg(25, 1203057))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12561') '[convertstrid(1203058)]' (**arg(26, 1203058))
get_char('c12561') '[convertstrid(1203059)]' (**arg(27, 1203059))
return "avg14052"