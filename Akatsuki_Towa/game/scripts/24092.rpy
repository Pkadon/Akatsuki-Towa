label avg24092(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_039
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200332)]' (**arg(1, 1200332))
return "avg24092"