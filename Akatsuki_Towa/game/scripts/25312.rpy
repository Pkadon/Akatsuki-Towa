label avg25312:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
get_char('c23') '[convertstrid(1211199)]' (**arg(1, 1211199))
hide p2
play sfx2 "other_7057.ogg"
get_char('c0') '[convertstrid(1211200)]' (**arg(2, 1211200))
get_char('c20153') '[convertstrid(1211201)]' (**arg(3, 1211201))
menu:
    extend ""
    '[convertstrid(1214995)]':
        call avg25313
    '[convertstrid(1214996)]':
        call avg25026
return