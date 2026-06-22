label avg10036:

$ play_music("ed7151.ogg")
scene avg_bg_027
$ update_narrator('c13')
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
window show
with fade_in
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "common_wrong.ogg"
play sfxvoice "avg_vocal_na08.ogg"
get_char('c13') '[convertstrid(1003008)]' (**arg(1, 1003008))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1003031)]' (**arg(2, 1003031))
$ play_music("ed6567.ogg")
hide p1
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
play sfxvoice "ed7v0652.ogg"
get_char('c6023') '[convertstrid(1003032)]' (**arg(3, 1003032))
hide p2
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003033)]' (**arg(4, 1003033))
hide p1
$ update_narrator('c6033')
with fade
$ update_portrait('sc001_01 4', 'p603', [r_entrance_midback(-11), light], 6)
play sfx2 "fight_6023.ogg"
play sfxvoice "ed7v0659.ogg"
get_char('c6033') '[convertstrid(1003034)]' (**arg(5, 1003034))
$ update_portrait('sc001_01 4', 'p603', [r(-11), light], 6)
play sfx2 "fight_6020.ogg"
get_char('c6033') '[convertstrid(1003035)]' (**arg(6, 1003035))
$ update_portrait('sc001_01 4', 'p603', [r(-11), dark], 5)
$ update_portrait('sc002_01 4', 'p604', [l_entrance(-12), light, flip], 6)
play sfx2 "other_7085.ogg"
play sfxvoice "ed7v0759.ogg"
get_char('c6041') '[convertstrid(1003036)]' (**arg(7, 1003036))
$ update_portrait('sc002_01 4', 'p604', [l_midback(-12), light, flip], 6)
play sfx2 "fight_6022.ogg"
play sfxvoice "ed7v0732.ogg"
get_char('c6041') '[convertstrid(1003037)]' (**arg(8, 1003037))
hide p604
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfx2 "elc_5007.ogg"
get_char('c21') '[convertstrid(1003038)]' (**arg(9, 1003038))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc001_01 5', 'p603', [r(-11), light], 6)
get_char('c6033') '[convertstrid(1003039)]' (**arg(10, 1003039))
hide p2
$ update_portrait('sc001_01 5', 'p603', [r(-11), dark], 5)
$ update_portrait('st016_01 5', 'p215', [l(-8), light, flip], 6)
get_char('c2151') '[convertstrid(1003040)]' (**arg(11, 1003040))
hide p603
$ update_portrait('st016_01 5', 'p215', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003041)]' (**arg(12, 1003041))
hide p215
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003042)]' (**arg(13, 1003042))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc002_01 1', 'p604', [r(-12), light], 6)
get_char('c6043') '[convertstrid(1003043)]' (**arg(14, 1003043))
hide p2
$ update_portrait('sc002_01 1', 'p604', [r(-12), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c31') '[convertstrid(1003044)]' (**arg(15, 1003044))
hide p604
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li12.ogg"
get_char('c43') '[convertstrid(1003045)]' (**arg(16, 1003045))
hide p3
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003046)]' (**arg(17, 1003046))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc001_01 5', 'p603', [r(-11), light], 6)
get_char('c6033') '[convertstrid(1003047)]' (**arg(18, 1003047))
hide p603
$ update_portrait('sc001_01 1', 'p9', [r(-11), light], 6)
play sfxvoice "ed7v0702.ogg"
get_char('c93') '[convertstrid(1003048)]' (**arg(19, 1003048))
hide p2
$ update_portrait('sc001_01 1', 'p9', [r(-11), dark], 5)
$ update_portrait('sc002_01 1', 'p10', [l(-12), light, flip], 6)
play sfxvoice "ed7v0777.ogg"
get_char('c101') '[convertstrid(1003049)]' (**arg(20, 1003049))
return