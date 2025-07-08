label avg1032:
stop music

play music "ed7201.ogg"
scene avg_bg_010
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[2100562]]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100563]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l_entrance(-25), light, flip], 6)
c591 '[textdict[2100564]]'
hide p1
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
c23 '[textdict[2100565]]'
hide p2
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[2100566]]'
hide p59
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[2100567]]'
hide p2
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100568]]'
hide p59
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[2100569]]'
return