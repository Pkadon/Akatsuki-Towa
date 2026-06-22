label avg25220:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6016.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
get_char('c23') '[convertstrid(1210762)]' (**arg(1, 1210762))
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210763)]' (**arg(2, 1210763))
hide p1
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch16.ogg"
get_char('c23') '[convertstrid(1210764)]' (**arg(3, 1210764))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "elc_5002.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210765)]' (**arg(4, 1210765))
return