label avg25184(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1210602)]' (**arg(1, 1210602))
hide p1
get_char('c6123') '[convertstrid(1210603)]' (**arg(2, 1210603))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210604)]' (**arg(3, 1210604))
hide p2
get_char('c20213') '[convertstrid(1210605)]' (**arg(4, 1210605))
get_char('c20213') '[convertstrid(1210606)]' (**arg(5, 1210606))
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na17.ogg"
get_char('c13') '[convertstrid(1210607)]' (**arg(6, 1210607))
hide p1
get_char('c20213') '[convertstrid(1210608)]' (**arg(7, 1210608))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210609)]' (**arg(8, 1210609))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
get_char('c13') '[convertstrid(1210610)]' (**arg(9, 1210610))
return "avg25184"