label avg25086(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1210249)]' (**arg(1, 1210249))
hide p2
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na17.ogg"
get_char('c13') '[convertstrid(1210250)]' (**arg(2, 1210250))
return "avg25086"