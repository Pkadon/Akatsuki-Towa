label avg14040:

play music "ed7110.ogg"
scene avg_bg_015
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[textdict[1202760]]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202761]]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1202762]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
c7521 '[textdict[1202763]]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 5)
c23 '[textdict[1202764]]'
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
c7521 '[textdict[1202765]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 5)
c23 '[textdict[1202766]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c7521 '[textdict[1202767]]'
c7521 '[textdict[1202768]]'
hide p2
c0 '[textdict[1202769]]'
return