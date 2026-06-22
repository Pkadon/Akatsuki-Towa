label avg12121:

$ play_music("ED6104.ogg")
scene avg_bg_038
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7044.ogg"
get_char('c13') '[convertstrid(1128217)]' (**arg(1, 1128217))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c9581') '[convertstrid(1128218)]' (**arg(2, 1128218))
get_char('c9591') '[convertstrid(1128219)]' (**arg(3, 1128219))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128220)]' (**arg(4, 1128220))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c9591') '[convertstrid(1128221)]' (**arg(5, 1128221))
get_char('c9591') '[convertstrid(1128222)]' (**arg(6, 1128222))
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128223)]' (**arg(7, 1128223))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
get_char('c9591') '[convertstrid(1128224)]' (**arg(8, 1128224))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128225)]' (**arg(9, 1128225))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c9591') '[convertstrid(1128226)]' (**arg(10, 1128226))
get_char('c9591') '[convertstrid(1128227)]' (**arg(11, 1128227))
get_char('c9591') '[convertstrid(1128228)]' (**arg(12, 1128228))
get_char('c9591') '[convertstrid(1128229)]' (**arg(13, 1128229))
get_char('c9591') '[convertstrid(1128230)]' (**arg(14, 1128230))
menu:
    extend ""
    '[convertstrid(1100001)]':
        call avg12123
    '[convertstrid(1100002)]':
        call avg12122
return