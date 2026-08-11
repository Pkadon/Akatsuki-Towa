label avg20127(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1006627)]' (**arg(1, 1006627))
menu:
    extend ""
    '[convertstrid(1006628)]':
        call avg20128
    '[convertstrid(1006629)]':
        call avg20129
return _return