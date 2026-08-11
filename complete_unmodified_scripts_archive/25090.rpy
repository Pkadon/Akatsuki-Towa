label avg25090(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_hurt_01.ogg"
get_char('c23') '[convertstrid(1210256)]' (**arg(1, 1210256))
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1210257)]' (**arg(2, 1210257))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210258)]' (**arg(3, 1210258))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210259)]' (**arg(4, 1210259))
menu:
    extend ""
    '[convertstrid(1214997)]':
        call avg25091
    '[convertstrid(1215000)]':
        call avg25026
return _return