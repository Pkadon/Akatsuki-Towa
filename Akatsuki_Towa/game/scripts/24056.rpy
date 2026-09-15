label avg24056(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200234)]' (**arg(1, 1200234))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c7583') '[convertstrid(1200235)]' (**arg(2, 1200235))
hide p1
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200236)]' (**arg(3, 1200236))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200237)]' (**arg(4, 1200237))
return "avg24056"