label avg14015:
stop music

play music "ED6200.ogg"
scene avg_bg_010
window show
with fade_in
c0 '[textdict[1202324]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1202325]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202326]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1202327]]'
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1202328]]'
hide p2
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1202329]]'
hide p28
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
with fade
c281 '[textdict[1202330]]'
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1202331]]'
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1202332]]'
hide p2
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1202333]]'
hide p28
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1202334]]'
hide p28
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1202335]]'
hide p28
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1202336]]'
hide p1
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1202337]]'
hide p28
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202338]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1202339]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202340]]'
hide p2
hide p1
with fade
c0 '[textdict[1202341]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1202342]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202343]]'
stop music
hide p2
hide p1
c0 '[textdict[1202344]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1202345]]'
hide p1
with fade
play sfx2 "other_7079.ogg"
c20161 '[textdict[1202346]]' (what_size=(gui.text_size*1.2))
play music "ed7511.ogg"
$ update_portrait('oc001_01 3', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1202347]]'
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1202348]]'
hide p28
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1202770]]' (what_size=(gui.text_size*1.2))
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1202771]]' (what_size=(gui.text_size*1.2))
hide p1
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 6)
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 5)
c23 '[textdict[1202772]]' (what_size=(gui.text_size*1.2))
hide p28
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[textdict[1202773]]' (what_size=(gui.text_size*1.2))
return