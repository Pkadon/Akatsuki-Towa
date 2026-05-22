label avg14039:

$ play_music("ed7110.ogg")
scene avg_bg_015
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[convertstrid(1202760)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1202761)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1202762)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
c7521 '[convertstrid(1202763)]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1202764)]'
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
c7521 '[convertstrid(1202765)]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1202766)]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c7521 '[convertstrid(1202767)]'
c7521 '[convertstrid(1202768)]'
hide p2
c0 '[convertstrid(1202769)]'
return