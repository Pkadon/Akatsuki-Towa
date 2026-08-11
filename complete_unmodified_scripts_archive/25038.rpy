label avg25038(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_na24.ogg"
get_char('c13') '[convertstrid(1210098)]' (**arg(1, 1210098))
return "avg25038"