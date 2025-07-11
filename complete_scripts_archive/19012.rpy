label avg19012:

scene avg_bg_023
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1216111]]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1216112]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216113]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216134]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216135]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216136]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1216137]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216138]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216139]]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
c0 '[textdict[1216140]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1216141]]":
        call avg19015
    "[textdict[1216142]]":
        call avg19016
    "[textdict[1216143]]":
        call avg19017
return