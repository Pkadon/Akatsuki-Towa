label avg12033(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7046.ogg"
get_char('c0') '[convertstrid(1120184)]' (**arg(1, 1120184))
get_char('c9691') '[convertstrid(1120185)]' (**arg(2, 1120185))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1120186)]' (**arg(3, 1120186))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c9691') '[convertstrid(1120187)]' (**arg(4, 1120187))
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120188)]' (**arg(5, 1120188))
hide p2
play sfx2 "other_7081.ogg"
get_char('c9733') '[convertstrid(1120189)]' (**arg(6, 1120189))
get_char('c9691') '[convertstrid(1120190)]' (**arg(7, 1120190))
get_char('c9691') '[convertstrid(1120191)]' (**arg(8, 1120191))
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120192)]' (**arg(9, 1120192))
hide p2
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120193)]' (**arg(10, 1120193))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
get_char('c9691') '[convertstrid(1120194)]' (**arg(11, 1120194))
hide p1
play sfx2 "other_7081.ogg"
get_char('c9733') '[convertstrid(1120195)]' (**arg(12, 1120195))
return "avg12033"