label avg1040:

play music "ed7201.ogg"
scene avg_bg_010
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[convertstrid(2100628)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100629)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(2100630)]'
hide p2
$ update_portrait('sc046_01 1', 'p53', [l_entrance(-5), light, flip], 6)
c531 '[convertstrid(2100631)]'
$ update_portrait('sc046_01 1', 'p53', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100632)]'
hide p53
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100633)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100634)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100635)]'
hide p56
$ update_portrait('sc046_01 1', 'p53', [l(-5), light, flip], 6)
c531 '[convertstrid(2100636)]'
hide p1
$ update_portrait('sc046_01 1', 'p53', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100637)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100638)]'
hide p53
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(2100639)]'
return