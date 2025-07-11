label avg19016:

scene avg_bg_023
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1216147]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216148]]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1216149]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216158]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216159]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216160]]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
c0 '[textdict[1216161]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1216162]]":
        call avg19017
    "[textdict[1216163]]":
        call avg19018
    "[textdict[1216164]]":
        call avg19019
return