label avg10066:

play music "ED6103.ogg"
scene avg_bg_037
$ update_narrator('c6933')
window show
with fade_in
$ update_portrait('sc015_01 1', 'p693', [r_entrance(9), light], 6)
c6933 '[convertstrid(1005010)]'
$ update_portrait('sc015_01 1', 'p693', [r(9), light], 6)
c6933 '[convertstrid(1005011)]'
$ update_portrait('sc015_01 1', 'p693', [r(9), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1005012)]'
hide p1
$ update_portrait('sc040_01 2', 'p47', [l(-9), light, flip], 6)
c471 '[convertstrid(1005027)]'
hide p693
$ update_portrait('sc040_01 2', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
c233 '[convertstrid(1005028)]'
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('sc040_01 6', 'p47', [l(-9), light, flip], 6)
c471 '[convertstrid(1005029)]'
hide p47
hide p23
c0 '[convertstrid(1005030)]'
$ update_portrait('sc015_01 2', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(1005031)]'
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(1005033)]'
hide p23
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
c11 '[convertstrid(1005034)]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
c473 '[convertstrid(1005035)]'
hide p1
$ update_portrait('sc040_01 1', 'p47', [r(-9), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1005036)]'
hide p47
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005037)]'
hide p1
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1005038)]'
hide p2
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[convertstrid(1005039)]'
return