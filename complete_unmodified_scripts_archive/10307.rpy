label avg10307(trans=fade_in):

$ play_music("ed7126.ogg")
scene avg_bg_074
$ update_narrator('c10041')
window show
with trans
$ update_portrait('sc046_01 3', 'p1004', [l_entrance(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130223)]' (**arg(1, 1130223))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130224)]' (**arg(2, 1130224))
hide p1004
play sfx2 "other_7075.ogg"
get_char('c0') '[convertstrid(1130225)]' (**arg(3, 1130225))
$ update_portrait('sc046_01 5', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130226)]' (**arg(4, 1130226))
$ update_portrait('sc046_01 5', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7020.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1130227)]' (**arg(5, 1130227))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc046_01 5', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130228)]' (**arg(6, 1130228))
$ update_portrait('sc046_01 2', 'p1004', [l(-5), l_shake, light, flip], 6)
play sfx2 "other_7057.ogg"
get_char('c10041') '[convertstrid(1130229)]' (**arg(7, 1130229))
$ update_portrait('sc046_01 2', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1130230)]' (**arg(8, 1130230))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1130231)]' (**arg(9, 1130231))
hide p1
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130232)]' (**arg(10, 1130232))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc046_01 2', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130233)]' (**arg(11, 1130233))
$ update_portrait('sc046_01 2', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130234)]' (**arg(12, 1130234))
hide p1004
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1130235)]' (**arg(13, 1130235))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro17.ogg"
get_char('c31') '[convertstrid(1130236)]' (**arg(14, 1130236))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130237)]' (**arg(15, 1130237))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130238)]' (**arg(16, 1130238))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130239)]' (**arg(17, 1130239))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro11.ogg"
get_char('c31') '[convertstrid(1130240)]' (**arg(18, 1130240))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130241)]' (**arg(19, 1130241))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130242)]' (**arg(20, 1130242))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1130243)]' (**arg(21, 1130243))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130244)]' (**arg(22, 1130244))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130245)]' (**arg(23, 1130245))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc046_01 2', 'p1004', [l(-5), l_shake, light, flip], 6)
get_char('c10041') '[convertstrid(1130246)]' (**arg(24, 1130246))
hide p1
$ update_portrait('sc046_01 2', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130247)]' (**arg(25, 1130247))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130248)]' (**arg(26, 1130248))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130249)]' (**arg(27, 1130249))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130250)]' (**arg(28, 1130250))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li02.ogg"
get_char('c43') '[convertstrid(1130251)]' (**arg(29, 1130251))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 1', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130252)]' (**arg(30, 1130252))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130253)]' (**arg(31, 1130253))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130254)]' (**arg(32, 1130254))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('sc046_01 1', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130255)]' (**arg(33, 1130255))
hide p4
$ update_portrait('sc046_01 1', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130256)]' (**arg(34, 1130256))
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro11.ogg"
get_char('c33') '[convertstrid(1130257)]' (**arg(35, 1130257))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130258)]' (**arg(36, 1130258))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130259)]' (**arg(37, 1130259))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130260)]' (**arg(38, 1130260))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130261)]' (**arg(39, 1130261))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1130262)]' (**arg(40, 1130262))
hide p3
$ update_portrait('sc046_01 4', 'p1004', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130263)]' (**arg(41, 1130263))
hide p1004
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130264)]' (**arg(42, 1130264))
return "avg10307"