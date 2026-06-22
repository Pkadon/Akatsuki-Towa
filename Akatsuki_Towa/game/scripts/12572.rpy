label avg12572:

$ play_music("ED6105.ogg")
scene avg_bg_077
$ update_narrator('c12581')
window show
with fade_in
get_char('c12581') '[convertstrid(1155157)]' (**arg(1, 1155157))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155158)]' (**arg(2, 1155158))
hide p4
$ update_portrait('oc002_01 18', 'p2', [r_midback(-3), light], 6)
get_char('c23') '[convertstrid(1155159)]' (**arg(3, 1155159))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
get_char('c12581') '[convertstrid(1155160)]' (**arg(4, 1155160))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155161)]' (**arg(5, 1155161))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12581') '[convertstrid(1155162)]' (**arg(6, 1155162))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155163)]' (**arg(7, 1155163))
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1155164)]' (**arg(8, 1155164))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
get_char('c12581') '[convertstrid(1155165)]' (**arg(9, 1155165))
get_char('c12581') '[convertstrid(1155166)]' (**arg(10, 1155166))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c43') '[convertstrid(1155167)]' (**arg(11, 1155167))
hide p4
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1155168)]' (**arg(12, 1155168))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1155169)]' (**arg(13, 1155169))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155170)]' (**arg(14, 1155170))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155171)]' (**arg(15, 1155171))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155172)]' (**arg(16, 1155172))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1155173)]' (**arg(17, 1155173))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1155174)]' (**arg(18, 1155174))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155175)]' (**arg(19, 1155175))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155176)]' (**arg(20, 1155176))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155177)]' (**arg(21, 1155177))
hide p3
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12581') '[convertstrid(1155178)]' (**arg(22, 1155178))
get_char('c12581') '[convertstrid(1155179)]' (**arg(23, 1155179))
return