label avg24009:

$ play_music("ed7105.ogg")
scene avg_bg_064
$ update_narrator('c7431')
window show
with fade_in
get_char('c7431') '[convertstrid(1200030)]' (**arg(1, 1200030))
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200031)]' (**arg(2, 1200031))
return