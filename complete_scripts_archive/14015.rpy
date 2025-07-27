label avg14015:

play music "ED6200.ogg"
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1202324)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202325)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1202326)]'
hide p2
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1202327)]'
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1202328)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202329)]'
hide p28
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
with fade
c281 '[convertstrid(1202330)]'
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202331)]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1202332)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202333)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1202334)]'
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1202335)]'
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1202336)]'
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202337)]'
hide p28
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1202338)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202339)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1202340)]'
hide p2
hide p1
$ update_narrator('c0')
with fade
c0 '[convertstrid(1202341)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202342)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1202343)]'
stop music
hide p2
hide p1
c0 '[convertstrid(1202344)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202345)]'
hide p1
$ update_narrator('c20161')
with fade
play sfx2 "other_7079.ogg"
c20161 '[convertstrid(1202346)]' (what_size=(gui.text_size*1.2))
play music "ed7511.ogg"
$ update_portrait('oc001_01 3', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1202347)]'
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1202348)]'
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1202770)]' (what_size=(gui.text_size*1.2))
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1202771)]' (what_size=(gui.text_size*1.2))
hide p1
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1202772)]' (what_size=(gui.text_size*1.2))
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1202773)]' (what_size=(gui.text_size*1.2))
return