label avg25142(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1210444)]' (**arg(1, 1210444))
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210445)]' (**arg(2, 1210445))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210446)]' (**arg(3, 1210446))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1210447)]' (**arg(4, 1210447))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1210448)]' (**arg(5, 1210448))
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1210449)]' (**arg(6, 1210449))
hide p2
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210450)]' (**arg(7, 1210450))
menu:
    extend ""
    '[convertstrid(1210451)]':
        call avg25144
    '[convertstrid(1210452)]':
        call avg25145
    '[convertstrid(1210453)]':
        call avg25143
return _return