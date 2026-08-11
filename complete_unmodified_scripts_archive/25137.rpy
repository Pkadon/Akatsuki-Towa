label avg25137(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1210422)]' (**arg(1, 1210422))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c23') '[convertstrid(1210423)]' (**arg(2, 1210423))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "common_tag_2.ogg"
get_char('c13') '[convertstrid(1210424)]' (**arg(3, 1210424))
return "avg25137"