label avg25185(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with trans
play sfx2 "other_7092.ogg"
get_char('c6123') '[convertstrid(1210612)]' (**arg(1, 1210612))
get_char('c6123') '[convertstrid(1210613)]' (**arg(2, 1210613))
play sfx2 "other_7092.ogg"
get_char('c0') '[convertstrid(1210614)]' (**arg(3, 1210614))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210615)]' (**arg(4, 1210615))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210616)]' (**arg(5, 1210616))
return "avg25185"