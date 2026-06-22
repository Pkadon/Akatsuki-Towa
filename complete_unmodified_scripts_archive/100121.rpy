label avg100121:

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with fade_in
get_char('c91') '[convertstrid(1218074)]' (**arg(1, 1218074))
$ update_portrait('sc001_01 2', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_get_02.ogg"
get_char('c13') '[convertstrid(1218075)]' (**arg(2, 1218075))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218076)]' (**arg(3, 1218076))
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_get_02.ogg"
get_char('c13') '[convertstrid(1218077)]' (**arg(4, 1218077))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 4', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218078)]' (**arg(5, 1218078))
$ update_portrait('sc001_01 4', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_arts_02.ogg"
get_char('c13') '[convertstrid(1218079)]' (**arg(6, 1218079))
menu:
    extend ""
    '[convertstrid(1218080)]':
        call avg100122
    '[convertstrid(1218081)]':
        call avg100123
    '[convertstrid(1218082)]':
        call avg100124
return