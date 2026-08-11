label avg25087(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na23.ogg"
get_char('c13') '[convertstrid(1210251)]' (**arg(1, 1210251))
return "avg25087"