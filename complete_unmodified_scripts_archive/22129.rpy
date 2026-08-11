label avg22129(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1128262)]' (**arg(1, 1128262))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1128263)]' (**arg(2, 1128263))
hide p2
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1128264)]' (**arg(3, 1128264))
hide p1
$ update_portrait('oc003_01 10', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1128265)]' (**arg(4, 1128265))
hide p3
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_sc01_01.ogg"
get_char('c13') '[convertstrid(1128266)]' (**arg(5, 1128266))
return "avg22129"