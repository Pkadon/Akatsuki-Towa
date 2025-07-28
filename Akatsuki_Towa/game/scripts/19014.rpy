label avg19014:

stop music
scene avg_bg_023
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1216119)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 8', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216120)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('sc049_01 8', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216121)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1216122)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216123)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216124)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216125)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1216126)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216127)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1216128)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216129)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216130)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216131)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216132)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216133)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216134)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216135)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216136)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216137)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216138)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216139)]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
c0 '[convertstrid(1216140)]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1216141]]":
        call avg19015
    "[textdict[1216142]]":
        call avg19016
    "[textdict[1216143]]":
        call avg19017
return