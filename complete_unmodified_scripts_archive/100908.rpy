label avg100908(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1218033)]' (**arg(1, 1218033))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218034)]' (**arg(2, 1218034))
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1218035)]' (**arg(3, 1218035))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218036)]' (**arg(4, 1218036))
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218037)]' (**arg(5, 1218037))
$ update_portrait('sc001_01 5', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1218038)]' (**arg(6, 1218038))
menu:
    extend ""
    '[convertstrid(1218039)]':
        call avg100909
    '[convertstrid(1218040)]':
        call avg100910
    '[convertstrid(1218041)]':
        call avg100911
return _return