label avg1003:

play music "ed7106.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[convertstrid(2100038)]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100039)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7037.ogg"
c561 '[convertstrid(2100040)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100041)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100042)]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(2100043)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100044)]'
hide p56
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
c21 '[convertstrid(2100045)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100046)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100047)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100048)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100049)]'
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100050)]'
return