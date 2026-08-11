label avg25293(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
get_char('c23') '[convertstrid(1211117)]' (**arg(1, 1211117))
hide p2
play sfx2 "other_7057.ogg"
get_char('c0') '[convertstrid(1211118)]' (**arg(2, 1211118))
get_char('c20153') '[convertstrid(1211119)]' (**arg(3, 1211119))
menu:
    extend ""
    '[convertstrid(1214995)]':
        call avg25294
    '[convertstrid(1214996)]':
        call avg25026
return _return