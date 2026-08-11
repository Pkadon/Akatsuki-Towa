label avg29134(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1218309)]' (**arg(1, 1218309))
return "avg29134"