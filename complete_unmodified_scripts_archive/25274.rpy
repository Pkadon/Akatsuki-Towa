label avg25274(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na24.ogg"
get_char('c13') '[convertstrid(1211043)]' (**arg(1, 1211043))
return "avg25274"