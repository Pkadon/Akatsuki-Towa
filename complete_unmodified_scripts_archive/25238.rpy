label avg25238(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210847)]' (**arg(1, 1210847))
hide p1
play sfx2 "other_7057.ogg"
get_char('c20213') '[convertstrid(1210848)]' (**arg(2, 1210848))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210849)]' (**arg(3, 1210849))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210850)]' (**arg(4, 1210850))
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1210851)]' (**arg(5, 1210851))
return "avg25238"