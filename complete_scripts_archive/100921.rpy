label avg100921:

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with fade_in
c91 '[convertstrid(1218074)]'
$ update_portrait('sc001_01 2', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[convertstrid(1218075)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[convertstrid(1218076)]'
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[convertstrid(1218077)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 4', 'p9', [l(-11), light, flip], 6)
c91 '[convertstrid(1218078)]'
$ update_portrait('sc001_01 4', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_arts_02.ogg"
c13 '[convertstrid(1218079)]'
menu:
    extend ""
    "[textdict[1218080]]":
        call avg100922
    "[textdict[1218081]]":
        call avg100923
    "[textdict[1218082]]":
        call avg100924
return