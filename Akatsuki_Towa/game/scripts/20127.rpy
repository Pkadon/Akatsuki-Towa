label avg20127(trans=fade_in):

$ play_music("ed7103.ogg")
scene avg_bg_019
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
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