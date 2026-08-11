label avg29034(trans=fade_in):

$ play_music("ED6104.ogg")
scene avg_bg_027
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1100018)]' (**arg(1, 1100018))
menu:
    extend ""
    '[convertstrid(1214998)]':
        call avg29035
    '[convertstrid(1215000)]':
        call avg29025
return _return