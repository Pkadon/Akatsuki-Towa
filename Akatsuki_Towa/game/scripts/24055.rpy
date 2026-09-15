label avg24055(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1200230)]' (**arg(1, 1200230))
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200231)]' (**arg(2, 1200231))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
get_char('c7613') '[convertstrid(1200232)]' (**arg(3, 1200232))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200233)]' (**arg(4, 1200233))
return "avg24055"