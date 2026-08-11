label avg25317(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6020.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1211226)]' (**arg(1, 1211226))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211227)]' (**arg(2, 1211227))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1211228)]' (**arg(3, 1211228))
return "avg25317"