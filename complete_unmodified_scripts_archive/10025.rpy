label avg10025:

$ play_music("ED6505.ogg")
scene avg_bg_001
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7018.ogg"
get_char('c0') '[convertstrid(1002140)]' (**arg(1, 1002140))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c41') '[convertstrid(1002141)]' (**arg(2, 1002141))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c33') '[convertstrid(1002142)]' (**arg(3, 1002142))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002143)]' (**arg(4, 1002143))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1002144)]' (**arg(5, 1002144))
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1002145)]' (**arg(6, 1002145))
hide p1
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1002146)]' (**arg(7, 1002146))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1002147)]' (**arg(8, 1002147))
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1002148)]' (**arg(9, 1002148))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l_exit(-5), light, flip], 6)
get_char('c41') '[convertstrid(1002149)]' (**arg(10, 1002149))
hide p4
hide p1
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1002150)]' (**arg(11, 1002150))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002151)]' (**arg(12, 1002151))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l_entrance(-6), light, flip], 6)
get_char('c51') '[convertstrid(1002152)]' (**arg(13, 1002152))
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002153)]' (**arg(14, 1002153))
hide p5
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1002154)]' (**arg(15, 1002154))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002155)]' (**arg(16, 1002155))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002156)]' (**arg(17, 1002156))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002157)]' (**arg(18, 1002157))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1002158)]' (**arg(19, 1002158))
hide p1
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1002159)]' (**arg(20, 1002159))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002160)]' (**arg(21, 1002160))
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002161)]' (**arg(22, 1002161))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 12', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1002162)]' (**arg(23, 1002162))
hide p1
$ update_portrait('oc005_01 12', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1002163)]' (**arg(24, 1002163))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji16.ogg"
get_char('c51') '[convertstrid(1002164)]' (**arg(25, 1002164))
return