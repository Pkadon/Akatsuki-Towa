label avg12424(trans=fade_in):

$ play_music("ed7350.ogg")
scene avg_bg_052
$ update_narrator('c43')
window show
with trans
$ update_portrait('oc004_01 11', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1142945)]' (**arg(1, 1142945))
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro18.ogg"
get_char('c31') '[convertstrid(1142946)]' (**arg(2, 1142946))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1142947)]' (**arg(3, 1142947))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142948)]' (**arg(4, 1142948))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142949)]' (**arg(5, 1142949))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1142950)]' (**arg(6, 1142950))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1142951)]' (**arg(7, 1142951))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li15.ogg"
get_char('c43') '[convertstrid(1142952)]' (**arg(8, 1142952))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1142953)]' (**arg(9, 1142953))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1142954)]' (**arg(10, 1142954))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1142955)]' (**arg(11, 1142955))
return "avg12424"