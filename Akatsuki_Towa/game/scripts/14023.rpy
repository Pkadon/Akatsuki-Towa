label avg14023:

play music "ed7300.ogg"
scene avg_bg_071
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1202446)]'
$ update_portrait('oc002_01 20', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "fight_6010.ogg"
c21 '[convertstrid(1202447)]'
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r_entrance(-2), light], 6)
play sfx2 "elc_5005.ogg"
c13 '[convertstrid(1202448)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1202459)]'
scene avg_bg_022
$ update_narrator('c0')
with fade
c0 '[convertstrid(1202474)]'
c9771 '[convertstrid(1202477)]'
$ update_portrait('oc002_01 18', 'p2', [r_entrance(-3), light], 6)
c23 '[convertstrid(1202478)]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
c11041 '[convertstrid(1202479)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1202480)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1202481)]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1202482)]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
c11041 '[convertstrid(1202484)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1202485)]'
scene avg_bg_071
$ update_narrator('c0')
with fade
c0 '[convertstrid(1202486)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1202487)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1202488)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1202489)]'
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1202490)]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
c20163 '[convertstrid(1202491)]'
return