label avg1023:

play music "ed7113.ogg"
scene avg_bg_024
$ update_portrait('sc015_01 2', 'p23', [l(9), light, flip], 6)
$ update_narrator('c231')
window show
with fade_in
c231 '[convertstrid(2100453)]'
$ update_portrait('sc015_01 2', 'p23', [l(9), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r_entrance(-3), light], 5)
play sfxvoice "avg_vocal_ch29.ogg"
c23 '[convertstrid(2100454)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[convertstrid(2100455)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100456)]'
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100457)]'
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100458)]'
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[convertstrid(2100459)]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(2100460)]'
return