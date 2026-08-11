label avg20129(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1100004)]' (**arg(1, 1100004))
return "avg20129"