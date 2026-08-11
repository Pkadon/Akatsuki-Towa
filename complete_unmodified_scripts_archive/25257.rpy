label avg25257(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210953)]' (**arg(1, 1210953))
hide p2
get_char('c20093') '[convertstrid(1210954)]' (**arg(2, 1210954))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210955)]' (**arg(3, 1210955))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c23') '[convertstrid(1210956)]' (**arg(4, 1210956))
hide p2
get_char('c20093') '[convertstrid(1210957)]' (**arg(5, 1210957))
return "avg25257"