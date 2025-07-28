label avg19022:

stop music
scene avg_bg_023
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1216226)]' (what_size=(gui.text_size*0.9))
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1216227)]' (what_size=(gui.text_size*0.9))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1216228)]' (what_size=(gui.text_size*0.9))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1216229)]' (what_size=(gui.text_size*0.9))
return