label avg19011:

stop music
scene avg_bg_023
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1216095)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216096)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1216097)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1216098)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216099)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216100)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216101)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216102)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1216103)]' (what_size=(gui.text_size*0.9))
hide p56
hide p2
c0 '[convertstrid(1216104)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216105)]' (what_size=(gui.text_size*0.9))
hide p56
c0 '[convertstrid(1216106)]' (what_size=(gui.text_size*0.9))
c0 '[convertstrid(1216107)]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1216108]]":
        call avg19012
    "[textdict[1216109]]":
        call avg19013
    "[textdict[1216110]]":
        call avg19014
return