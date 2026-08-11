label avg25043(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1210109)]' (**arg(1, 1210109))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210110)]' (**arg(2, 1210110))
return "avg25043"