label avg12237(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_038
$ update_narrator('c9951')
window show
with trans
get_char('c9951') '[convertstrid(1121184)]' (**arg(1, 1121184))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121185)]' (**arg(2, 1121185))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121186)]' (**arg(3, 1121186))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
get_char('c9951') '[convertstrid(1121187)]' (**arg(4, 1121187))
get_char('c6871') '[convertstrid(1121188)]' (**arg(5, 1121188))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1121189)]' (**arg(6, 1121189))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c6871') '[convertstrid(1121190)]' (**arg(7, 1121190))
hide p2
get_char('c9953') '[convertstrid(1121191)]' (**arg(8, 1121191))
get_char('c6871') '[convertstrid(1121192)]' (**arg(9, 1121192))
get_char('c9953') '[convertstrid(1121193)]' (**arg(10, 1121193))
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch03_b.ogg"
get_char('c23') '[convertstrid(1121194)]' (**arg(11, 1121194))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121195)]' (**arg(12, 1121195))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c6871') '[convertstrid(1121196)]' (**arg(13, 1121196))
return "avg12237"