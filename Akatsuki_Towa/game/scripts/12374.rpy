label avg12374(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_058
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1134071)]' (**arg(1, 1134071))
menu:
    extend ""
    '[convertstrid(1134072)]':
        call avg12375
    '[convertstrid(1134073)]':
        call avg12376
return _return