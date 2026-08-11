label avg20074(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_022
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1003943)]' (**arg(1, 1003943))
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7045.ogg"
get_char('c0') '[convertstrid(1003944)]' (**arg(2, 1003944))
scene avg_bg_022
$ update_narrator('c31')
with fade
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c31') '[convertstrid(1003945)]' (**arg(3, 1003945))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
get_char('c5413') '[convertstrid(1003946)]' (**arg(4, 1003946))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003947)]' (**arg(5, 1003947))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c5423') '[convertstrid(1003948)]' (**arg(6, 1003948))
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003949)]' (**arg(7, 1003949))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
get_char('c5413') '[convertstrid(1003950)]' (**arg(8, 1003950))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003951)]' (**arg(9, 1003951))
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003952)]' (**arg(10, 1003952))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
get_char('c5413') '[convertstrid(1003953)]' (**arg(11, 1003953))
get_char('c5413') '[convertstrid(1003954)]' (**arg(12, 1003954))
get_char('c5413') '[convertstrid(1003955)]' (**arg(13, 1003955))
get_char('c5423') '[convertstrid(1003956)]' (**arg(14, 1003956))
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003957)]' (**arg(15, 1003957))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003958)]' (**arg(16, 1003958))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003959)]' (**arg(17, 1003959))
return "avg20074"