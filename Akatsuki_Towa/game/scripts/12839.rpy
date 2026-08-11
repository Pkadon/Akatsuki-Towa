label avg12839(trans=fade_in):

$ play_music("ED6301.ogg")
scene avg_bg_218
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with trans
get_char('c31') '[convertstrid(1186141)]' (**arg(1, 1186141))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1186142)]' (**arg(2, 1186142))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1186143)]' (**arg(3, 1186143))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1186144)]' (**arg(4, 1186144))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1186145)]' (**arg(5, 1186145))
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1186146)]' (**arg(6, 1186146))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1186147)]' (**arg(7, 1186147))
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1186148)]' (**arg(8, 1186148))
hide p2
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1186149)]' (**arg(9, 1186149))
hide p1304
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1186150)]' (**arg(10, 1186150))
hide p3
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), r_shake, light, flip], 6)
get_char('c11') '[convertstrid(1186151)]' (**arg(11, 1186151))
hide p1
play sfx2 "other_7080.ogg"
get_char('c5001') '[convertstrid(1186152)]' (**arg(12, 1186152)) with shake
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
get_char('c31') '[convertstrid(1186153)]' (**arg(13, 1186153))
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1186154)]' (**arg(14, 1186154))
hide p3
hide p1
play sfx2 "fight_6009.ogg"
get_char('c0') '[convertstrid(1186155)]' (**arg(15, 1186155))
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1186156)]' (**arg(16, 1186156))
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1186157)]' (**arg(17, 1186157))
hide p2
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1186158)]' (**arg(18, 1186158))
return "avg12839"