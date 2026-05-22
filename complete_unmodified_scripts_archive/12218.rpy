label avg12218:

$ play_music("ed7569.ogg")
scene avg_bg_036
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7018.ogg"
c0 '[convertstrid(1121484)]'
$ update_portrait('oc002_01 18', 'p2', [r_entrance(-3), light], 6)
c23 '[convertstrid(1120924)]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1121485)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1120925)]'
hide p1
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('sc040_01 4', 'p47', [l(-9), light, flip], 6)
c471 '[convertstrid(1120926)]'
hide p47
hide p46
$ update_portrait('uc004_02 2', 'p990', [r(-6), light], 6)
$ update_narrator('c9903')
with fade
c9903 '[convertstrid(1120927)]'
$ update_portrait('uc004_02 2', 'p990', [r(-6), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[convertstrid(1120928)]'
hide p4
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120929)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc004_02 1', 'p990', [r(-6), light], 6)
c9903 '[convertstrid(1120930)]'
$ update_portrait('uc004_02 4', 'p990', [r(-6), light], 6)
c9903 '[convertstrid(1120931)]'
hide p1
$ update_portrait('uc004_02 4', 'p990', [r(-6), dark], 5)
$ update_portrait('sc040_01 8', 'p47', [l(-9), light, flip], 6)
c471 '[convertstrid(1120932)]'
hide p990
$ update_portrait('sc040_01 8', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1120933)]'
$ update_portrait('sc039_01 7', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1120934)]'
hide p47
$ update_portrait('sc039_01 7', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120935)]'
hide p46
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120936)]'
return