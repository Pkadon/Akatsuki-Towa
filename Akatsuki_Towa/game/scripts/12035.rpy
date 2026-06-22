label avg12035:

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1121557)]' (**arg(1, 1121557))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121558)]' (**arg(2, 1121558))
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121559)]' (**arg(3, 1121559))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 3', 'p537', [r(-7), light], 6)
get_char('c5373') '[convertstrid(1121560)]' (**arg(4, 1121560))
$ update_portrait('st033_01 3', 'p537', [r(-7), dark], 5)
$ update_portrait('oc002_01 20', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6003.ogg"
get_char('c21') '[convertstrid(1121561)]' (**arg(5, 1121561))
hide p537
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120215)]' (**arg(6, 1120215))
hide p1
$ update_portrait('st033_01 3', 'p537', [r(-7), light], 6)
get_char('c5373') '[convertstrid(1120216)]' (**arg(7, 1120216))
$ update_portrait('st033_01 3', 'p537', [r(-7), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120217)]' (**arg(8, 1120217))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 2', 'p537', [r(-7), light], 6)
get_char('c5373') '[convertstrid(1120218)]' (**arg(9, 1120218))
hide p2
hide p537
play sfx2 "other_7067.ogg"
get_char('c0') '[convertstrid(1120219)]' (**arg(10, 1120219))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120220)]' (**arg(11, 1120220))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120221)]' (**arg(12, 1120221))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120222)]' (**arg(13, 1120222))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120223)]' (**arg(14, 1120223))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1120224)]' (**arg(15, 1120224))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 2', 'p537', [r(-7), light], 6)
get_char('c5373') '[convertstrid(1120225)]' (**arg(16, 1120225))
$ update_portrait('st033_01 2', 'p537', [r(-7), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120226)]' (**arg(17, 1120226))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 4', 'p537', [r_exit(-7), light], 6)
get_char('c5373') '[convertstrid(1120227)]' (**arg(18, 1120227))
hide p537
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1120228)]' (**arg(19, 1120228))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120229)]' (**arg(20, 1120229))
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c21') '[convertstrid(1120230)]' (**arg(21, 1120230))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120231)]' (**arg(22, 1120231))
return