label avg12575:

play music "ED6102.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na04_b.ogg"
c13 '[textdict[1155297]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155298]]'
hide p3
c12321 '[textdict[1155299]]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1155300]]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1155301]]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1155302]]'
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155303]]'
hide p1
$ update_portrait('oc003_01 14', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
c43 '[textdict[1155304]]'
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155305]]'
hide p3
hide p4
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch16.ogg"
c21 '[textdict[1155306]]'
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1155307]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1155308]]'
hide p2
hide p1
$ update_narrator('c43')
with fade
$ update_portrait('oc004_01 8', 'p4', [r_entrance(-5), light], 5)
c43 '[textdict[1155309]]'
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 24', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155310]]'
$ update_portrait('oc003_01 24', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 13', 'p4', [r(-5), r_shake, light], 5)
play sfxvoice "avg_vocal_li11.ogg"
c43 '[textdict[1155311]]'
$ update_portrait('oc004_01 13', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155312]]'
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
c31 '[textdict[1155313]]'
hide p3
hide p4
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
with fade
c13 '[textdict[1155314]]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
c13 '[textdict[1155315]]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[textdict[1155316]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1155317]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1155318]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
c31 '[textdict[1155319]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1155320]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1155321]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1155322]]'
hide p2
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
c31 '[textdict[1155323]]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[textdict[1155324]]' with shake
return