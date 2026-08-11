label avg25244(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6025.ogg"
get_char('c13') '[convertstrid(1210885)]' (**arg(1, 1210885))
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1210886)]' (**arg(2, 1210886))
return "avg25244"