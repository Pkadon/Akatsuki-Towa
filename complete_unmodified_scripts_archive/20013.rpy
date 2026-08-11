label avg20013(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1000935)]' (**arg(1, 1000935))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
get_char('c23') '[convertstrid(1000936)]' (**arg(2, 1000936))
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000937)]' (**arg(3, 1000937))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000938)]' (**arg(4, 1000938))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000939)]' (**arg(5, 1000939))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000940)]' (**arg(6, 1000940))
return "avg20013"