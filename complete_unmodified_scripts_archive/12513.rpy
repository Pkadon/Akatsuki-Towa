label avg12513(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_narrator('c5241')
window show
with trans
play sfx2 "other_7071.ogg"
get_char('c5241') '[convertstrid(1151034)]' (**arg(1, 1151034))
get_char('c5241') '[convertstrid(1151035)]' (**arg(2, 1151035))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151036)]' (**arg(3, 1151036))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c5241') '[convertstrid(1151037)]' (**arg(4, 1151037))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151038)]' (**arg(5, 1151038))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c5241') '[convertstrid(1151039)]' (**arg(6, 1151039))
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1151040)]' (**arg(7, 1151040))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151041)]' (**arg(8, 1151041))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151042)]' (**arg(9, 1151042))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c5241') '[convertstrid(1151043)]' (**arg(10, 1151043))
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c31') '[convertstrid(1151044)]' (**arg(11, 1151044))
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151045)]' (**arg(12, 1151045))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c5241') '[convertstrid(1151046)]' (**arg(13, 1151046))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151047)]' (**arg(14, 1151047))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c5241') '[convertstrid(1151048)]' (**arg(15, 1151048))
hide p2
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151049)]' (**arg(16, 1151049))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7073.ogg"
get_char('c13') '[convertstrid(1151050)]' (**arg(17, 1151050))
return "avg12513"