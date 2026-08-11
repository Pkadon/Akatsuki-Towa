label avg25115(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1210342)]' (**arg(1, 1210342))
return "avg25115"