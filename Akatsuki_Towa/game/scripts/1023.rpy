label avg1023(trans=fade_in):

$ play_music("ed7113.ogg")
scene avg_bg_024
$ update_portrait('sc015_01 2', 'p23', [l(9), light, flip], 6)
$ update_narrator('c231')
window show
with trans
get_char('c231') '[convertstrid(2100453)]' (**arg(1, 2100453))
$ update_portrait('sc015_01 2', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch29.ogg"
get_char('c23') '[convertstrid(2100454)]' (**arg(2, 2100454))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100455)]' (**arg(3, 2100455))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100456)]' (**arg(4, 2100456))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100457)]' (**arg(5, 2100457))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100458)]' (**arg(6, 2100458))
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100459)]' (**arg(7, 2100459))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100460)]' (**arg(8, 2100460))
return "avg1023"