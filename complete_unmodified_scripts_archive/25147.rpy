label avg25147(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_tag_2.ogg"
get_char('c13') '[convertstrid(1210468)]' (**arg(1, 1210468))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1210469)]' (**arg(2, 1210469))
return "avg25147"