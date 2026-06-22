label avg10671:

$ play_music("ed6324.ogg")
scene avg_bg_041
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
$ update_narrator('c13041')
window show
with fade_in
get_char('c13041') '[convertstrid(1165936)]' (**arg(1, 1165936))
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165937)]' (**arg(2, 1165937))
hide p1304
hide p1
get_char('c0') '[convertstrid(1165938)]' (**arg(3, 1165938))
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165939)]' (**arg(4, 1165939))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165940)]' (**arg(5, 1165940))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165941)]' (**arg(6, 1165941))
stop music
hide p3
hide p4
$ update_narrator('c13621')
with fade
get_char('c13621') '[convertstrid(1165942)]' (**arg(7, 1165942))
get_char('c13633') '[convertstrid(1165943)]' (**arg(8, 1165943))
$ play_music("ed7511.ogg")
$ update_narrator('c13')
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
with fade
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1165944)]' (**arg(9, 1165944))
hide p1
get_char('c0') '[convertstrid(1165945)]' (**arg(10, 1165945))
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165946)]' (**arg(11, 1165946))
$ update_portrait('oc004_01 13', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1165947)]' (**arg(12, 1165947))
hide p4
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165948)]' (**arg(13, 1165948))
hide p2
hide p1
get_char('c0') '[convertstrid(1165949)]' (**arg(14, 1165949))
play sfx2 "other_7079.ogg"
get_char('c13621') '[convertstrid(1165950)]' (**arg(15, 1165950))
play sfx2 "other_7080.ogg"
get_char('c13633') '[convertstrid(1165951)]' (**arg(16, 1165951))
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165952)]' (**arg(17, 1165952))
$ update_portrait('oc003_01 21', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1165953)]' (**arg(18, 1165953))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1165954)]' (**arg(19, 1165954))
return