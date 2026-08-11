label avg25153(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210483)]' (**arg(1, 1210483))
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210484)]' (**arg(2, 1210484))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210485)]' (**arg(3, 1210485))
return "avg25153"