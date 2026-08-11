label avg10034(trans=fade_in):

stop music
scene avg_bg_027
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_correct.ogg"
get_char('c13') '[convertstrid(1003009)]' (**arg(1, 1003009))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003011)]' (**arg(2, 1003011))
hide p1
play sfx2 "fight_6022.ogg"
get_char('c0') '[convertstrid(1003012)]' (**arg(3, 1003012))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003013)]' (**arg(4, 1003013))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003014)]' (**arg(5, 1003014))
$ play_music("ed7151.ogg")
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003015)]' (**arg(6, 1003015))
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st016_01 2', 'p215', [r(-8), light], 6)
get_char('c2153') '[convertstrid(1003016)]' (**arg(7, 1003016))
hide p2
$ update_portrait('st016_01 2', 'p215', [r(-8), dark], 5)
$ update_portrait('st014_01 4', 'p213', [l(-18), light, flip], 6)
get_char('c2131') '[convertstrid(1003017)]' (**arg(8, 1003017))
hide p215
$ update_portrait('st014_01 4', 'p213', [l(-18), dark, flip], 5)
$ update_portrait('st018_01 5', 'p217', [r(-16), light], 6)
play sfx2 "other_7085.ogg"
get_char('c2173') '[convertstrid(1003018)]' (**arg(9, 1003018))
hide p213
$ update_portrait('st018_01 5', 'p217', [r(-16), dark], 5)
$ update_portrait('st019_01 5', 'p218', [l(-17), light, flip], 6)
get_char('c2181') '[convertstrid(1003019)]' (**arg(10, 1003019))
hide p217
$ update_portrait('st019_01 5', 'p218', [l(-17), dark, flip], 5)
$ update_portrait('st017_01 5', 'p216', [r(-18), light], 6)
get_char('c2163') '[convertstrid(1003020)]' (**arg(11, 1003020))
hide p218
$ update_portrait('st017_01 5', 'p216', [r(-18), dark], 5)
$ update_portrait('st016_01 5', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003021)]' (**arg(12, 1003021))
hide p216
$ update_portrait('st016_01 5', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7071.ogg"
get_char('c13') '[convertstrid(1003022)]' (**arg(13, 1003022))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7072.ogg"
get_char('c13') '[convertstrid(1003023)]' (**arg(14, 1003023))
hide p215
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c4981') '[convertstrid(1003024)]' (**arg(15, 1003024))
get_char('c4981') '[convertstrid(1003025)]' (**arg(16, 1003025))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfx2 "other_7059.ogg"
get_char('c13') '[convertstrid(1003026)]' (**arg(17, 1003026))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
get_char('c4981') '[convertstrid(1003027)]' (**arg(18, 1003027))
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1003028)]' (**arg(19, 1003028))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
get_char('c4981') '[convertstrid(1003029)]' (**arg(20, 1003029))
$ update_portrait('oc001_01 3', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003030)]' (**arg(21, 1003030))
$ play_music("ed6567.ogg")
hide p2
$ update_portrait('oc001_01 3', 'p1', [l(-2), dark, flip], 5)
play sfxvoice "ed7v0652.ogg"
get_char('c6023') '[convertstrid(1003032)]' (**arg(22, 1003032))
$ update_portrait('oc001_01 9', 'p1', [l(-2), l_shake, light, flip], 6)
get_char('c11') '[convertstrid(1003033)]' (**arg(23, 1003033))
hide p1
$ update_narrator('c6033')
with fade
$ update_portrait('sc001_01 4', 'p603', [r_entrance_midback(-11), light], 6)
play sfx2 "fight_6023.ogg"
play sfxvoice "ed7v0659.ogg"
get_char('c6033') '[convertstrid(1003034)]' (**arg(24, 1003034))
$ update_portrait('sc001_01 4', 'p603', [r(-11), light], 6)
play sfx2 "fight_6020.ogg"
get_char('c6033') '[convertstrid(1003035)]' (**arg(25, 1003035))
$ update_portrait('sc001_01 4', 'p603', [r(-11), dark], 5)
$ update_portrait('sc002_01 4', 'p604', [l_entrance(-12), light, flip], 6)
play sfx2 "other_7085.ogg"
play sfxvoice "ed7v0759.ogg"
get_char('c6041') '[convertstrid(1003036)]' (**arg(26, 1003036))
$ update_portrait('sc002_01 4', 'p604', [l_midback(-12), light, flip], 6)
play sfx2 "fight_6022.ogg"
play sfxvoice "ed7v0732.ogg"
get_char('c6041') '[convertstrid(1003037)]' (**arg(27, 1003037))
hide p604
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfx2 "elc_5007.ogg"
get_char('c21') '[convertstrid(1003038)]' (**arg(28, 1003038))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc001_01 5', 'p603', [r(-11), light], 6)
get_char('c6033') '[convertstrid(1003039)]' (**arg(29, 1003039))
hide p2
$ update_portrait('sc001_01 5', 'p603', [r(-11), dark], 5)
$ update_portrait('st016_01 5', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003040)]' (**arg(30, 1003040))
hide p603
$ update_portrait('st016_01 5', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003041)]' (**arg(31, 1003041))
hide p215
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003042)]' (**arg(32, 1003042))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc002_01 1', 'p604', [r(-12), light], 6)
get_char('c6043') '[convertstrid(1003043)]' (**arg(33, 1003043))
hide p2
$ update_portrait('sc002_01 1', 'p604', [r(-12), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c31') '[convertstrid(1003044)]' (**arg(34, 1003044))
hide p604
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li12.ogg"
get_char('c43') '[convertstrid(1003045)]' (**arg(35, 1003045))
hide p3
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003046)]' (**arg(36, 1003046))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc001_01 5', 'p603', [r(-11), light], 6)
get_char('c6033') '[convertstrid(1003047)]' (**arg(37, 1003047))
hide p603
$ update_portrait('sc001_01 1', 'p9', [r(-11), light], 6)
play sfxvoice "ed7v0702.ogg"
get_char('c93') '[convertstrid(1003048)]' (**arg(38, 1003048))
hide p2
$ update_portrait('sc001_01 1', 'p9', [r(-11), dark], 5)
$ update_portrait('sc002_01 1', 'p10', [l(-12), light, flip], 6)
play sfxvoice "ed7v0777.ogg"
get_char('c101') '[convertstrid(1003049)]' (**arg(39, 1003049))
return "avg10034"