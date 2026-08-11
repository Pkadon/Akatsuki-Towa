label avg22127(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1128253)]' (**arg(1, 1128253))
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1128254)]' (**arg(2, 1128254))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128255)]' (**arg(3, 1128255))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128256)]' (**arg(4, 1128256))
hide p1
$ update_portrait('oc003_01 13', 'p3', [mid(-6), light], 6)
play sfxvoice "bcv_oc003_com_01.ogg"
get_char('c33') '[convertstrid(1128257)]' (**arg(5, 1128257))
hide p3
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128258)]' (**arg(6, 1128258))
hide p1
$ update_portrait('oc003_01 6', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1128259)]' (**arg(7, 1128259))
$ update_portrait('oc003_01 10', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1128260)]' (**arg(8, 1128260))
hide p3
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfx2 "other_7079.ogg"
get_char('c13') '[convertstrid(1128261)]' (**arg(9, 1128261))
return "avg22127"