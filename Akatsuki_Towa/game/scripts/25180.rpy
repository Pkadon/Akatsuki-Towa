label avg25180(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210583)]' (**arg(1, 1210583))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210584)]' (**arg(2, 1210584))
hide p1
$ update_portrait('oc002_01 16', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(1210585)]' (**arg(3, 1210585))
return "avg25180"