label avg19010:
stop music

scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
window show
with fade_in
c561 '[textdict[1216070]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1216071]]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1216072]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216073]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216074]]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1216075]]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1216076]]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1216077]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216078]]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1216079]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216080]]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1216081]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216082]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216083]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216084]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216085]]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1216086]]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1216087]]":
        call avg19011
    "[textdict[1216088]]":
        call avg19022
return