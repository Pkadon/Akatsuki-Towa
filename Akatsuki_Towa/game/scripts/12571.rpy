label avg12571(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1155153)]' (**arg(1, 1155153))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155154)]' (**arg(2, 1155154))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 24', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155155)]' (**arg(3, 1155155))
return "avg12571"