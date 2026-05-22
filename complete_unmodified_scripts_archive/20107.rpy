label avg20107:

$ play_music("ED6103.ogg")
scene avg_bg_072
$ update_narrator('c11')
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7047.ogg"
c11 '[convertstrid(1005213)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
c6873 '[convertstrid(1005214)]'
hide p1
c0 '[convertstrid(1005215)]'
c6873 '[convertstrid(1005216)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1005217)]'
hide p1
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
c461 '[convertstrid(1005218)]'
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
c461 '[convertstrid(1005219)]'
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 5)
c6873 '[convertstrid(1005220)]'
hide p46
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1005221)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
c6873 '[convertstrid(1005222)]'
c6873 '[convertstrid(1005223)]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch19.ogg"
c21 '[convertstrid(1005224)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005225)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005226)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1005227)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
c151 '[convertstrid(1005229)]'
hide p1
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
c463 '[convertstrid(1005230)]'
hide p15
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1005231)]'
return