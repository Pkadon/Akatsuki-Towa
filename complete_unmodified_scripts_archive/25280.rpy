label avg25280(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "common_tag_2.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1211062)]' (**arg(1, 1211062))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1211063)]' (**arg(2, 1211063))
return "avg25280"