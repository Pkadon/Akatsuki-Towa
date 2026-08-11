label avg25316(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with trans
play sfx2 "other_7092.ogg"
get_char('c6123') '[convertstrid(1211221)]' (**arg(1, 1211221))
get_char('c6123') '[convertstrid(1211222)]' (**arg(2, 1211222))
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1211223)]' (**arg(3, 1211223))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1211224)]' (**arg(4, 1211224))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1211225)]' (**arg(5, 1211225))
return "avg25316"