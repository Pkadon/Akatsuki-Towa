label avg25013(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_tag_2.ogg"
get_char('c13') '[convertstrid(1210023)]' (**arg(1, 1210023))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210024)]' (**arg(2, 1210024))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210025)]' (**arg(3, 1210025))
return "avg25013"