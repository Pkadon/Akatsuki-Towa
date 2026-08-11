label avg19120(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_071
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218072)]' (**arg(1, 1218072, size=(0.9)))
$ update_portrait('sc001_01 2', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_get_02.ogg"
get_char('c13') '[convertstrid(1218073)]' (**arg(2, 1218073, size=(0.9)))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218074)]' (**arg(3, 1218074, size=(0.9)))
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_get_02.ogg"
get_char('c13') '[convertstrid(1218075)]' (**arg(4, 1218075, size=(0.9)))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 4', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218076)]' (**arg(5, 1218076, size=(0.9)))
$ update_portrait('sc001_01 4', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_arts_02.ogg"
get_char('c13') '[convertstrid(1218077)]' (**arg(6, 1218077, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1218078)]':
        call avg19121
    '[convertstrid(1218079)]':
        call avg19122
    '[convertstrid(1218080)]':
        call avg19123
return _return