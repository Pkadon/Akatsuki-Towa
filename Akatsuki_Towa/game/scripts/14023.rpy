label avg14023:

play music "ed7300.ogg"
scene avg_bg_071
window show
with fade_in
c0 '[textdict[1202446]]'
$ update_portrait('oc002_01 20', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "fight_6010.ogg"
c21 '[textdict[1202447]]'
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r_entrance(-2), light], 5)
play sfx2 "elc_5005.ogg"
c13 '[textdict[1202448]]'
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1202459]]'
scene avg_bg_022
with fade
c0 '[textdict[1202474]]'
c9771 '[textdict[1202477]]'
$ update_portrait('oc002_01 18', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[1202478]]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
c11041 '[textdict[1202479]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1202480]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1202481]]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 5)
c23 '[textdict[1202482]]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
c11041 '[textdict[1202484]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1202485]]'
scene avg_bg_071
with fade
c0 '[textdict[1202486]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1202487]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1202488]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202489]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1202490]]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 6)
c20163 '[textdict[1202491]]'
return