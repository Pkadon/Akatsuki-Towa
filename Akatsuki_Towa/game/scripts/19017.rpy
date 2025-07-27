label avg19017:

stop music
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1216150)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1216151)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216152)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216153)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216154)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216155)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1216156)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216157)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1216165)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1216166)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1216167)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216168)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1216169)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1216170)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1216171)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1216172)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216158)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216159)]' (what_size=(gui.text_size*0.9))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216160)]' (what_size=(gui.text_size*0.9))
hide p56
hide p1
c0 '[convertstrid(1216161)]' (what_size=(gui.text_size*0.9))
menu:
    extend ""
    "[textdict[1216162]]":
        call avg19017
    "[textdict[1216163]]":
        call avg19018
    "[textdict[1216164]]":
        call avg19019
return