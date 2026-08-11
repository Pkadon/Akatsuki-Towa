label avg20003(trans=fade_in):

$ play_music("ed7300.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7020.ogg"
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1000180)]' (**arg(1, 1000180))
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000181)]' (**arg(2, 1000181))
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000182)]' (**arg(3, 1000182))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000183)]' (**arg(4, 1000183))
$ update_portrait('oc002_01 18', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000184)]' (**arg(5, 1000184))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000185)]' (**arg(6, 1000185))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000186)]' (**arg(7, 1000186))
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000187)]' (**arg(8, 1000187))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1000188)]' (**arg(9, 1000188))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000189)]' (**arg(10, 1000189))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000190)]' (**arg(11, 1000190))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000191)]' (**arg(12, 1000191))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000192)]' (**arg(13, 1000192))
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000193)]' (**arg(14, 1000193))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000194)]' (**arg(15, 1000194))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000195)]' (**arg(16, 1000195))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000196)]' (**arg(17, 1000196))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000197)]' (**arg(18, 1000197))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000198)]' (**arg(19, 1000198))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000199)]' (**arg(20, 1000199))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000200)]' (**arg(21, 1000200))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000201)]' (**arg(22, 1000201))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000202)]' (**arg(23, 1000202))
$ play_music("ed9997.ogg")
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1000206)]' (**arg(24, 1000206))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c23') '[convertstrid(1000207)]' (**arg(25, 1000207))
return "avg20003"