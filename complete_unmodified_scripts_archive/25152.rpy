label avg25152(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1210481)]' (**arg(1, 1210481))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210482)]' (**arg(2, 1210482))
return "avg25152"