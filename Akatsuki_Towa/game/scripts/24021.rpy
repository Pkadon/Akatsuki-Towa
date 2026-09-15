label avg24021(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_041
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with trans
get_char('c33') '[convertstrid(1200089)]' (**arg(1, 1200089))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
get_char('c7591') '[convertstrid(1200090)]' (**arg(2, 1200090))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1200091)]' (**arg(3, 1200091))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c7591') '[convertstrid(1200092)]' (**arg(4, 1200092))
get_char('c7591') '[convertstrid(1200093)]' (**arg(5, 1200093))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1200094)]' (**arg(6, 1200094))
return "avg24021"