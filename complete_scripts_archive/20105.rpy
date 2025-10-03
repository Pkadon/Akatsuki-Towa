label avg20105:

$ play_music("ED6103.ogg")
scene avg_bg_038
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7047.ogg"
c21 '[convertstrid(1005102)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfx2 "other_7064.ogg"
c13 '[convertstrid(1005103)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c6961 '[convertstrid(1005104)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005105)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6961 '[convertstrid(1005106)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005107)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6971 '[convertstrid(1005108)]'
c6961 '[convertstrid(1005109)]'
c6961 '[convertstrid(1005110)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1005111)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c6981 '[convertstrid(1005112)]'
hide p2
$ update_portrait('sc039_01 2', 'p46', [r(-13), r_shake, light], 6)
c463 '[convertstrid(1005113)]'
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
c6961 '[convertstrid(1005114)]'
hide p46
$ update_portrait('oc001_01 12', 'p1', [r_midback(-2), light], 6)
c13 '[convertstrid(1005115)]'
hide p1
c6973 '[convertstrid(1005116)]'
c6961 '[convertstrid(1005117)]'
c6961 '[convertstrid(1005118)]'
c6983 '[convertstrid(1005119)]'
$ update_portrait('sc039_01 4', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1005120)]'
$ update_portrait('sc039_01 4', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1005121)]'
hide p46
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1005122)]'
hide p1
hide p2
c0 '[convertstrid(1005123)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1005124)]'
return