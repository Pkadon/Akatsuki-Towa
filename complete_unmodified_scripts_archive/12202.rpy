label avg12202:

$ play_music("ed7104.ogg")
scene avg_bg_039
$ update_narrator('c2253')
window show
with fade_in
$ update_portrait('st026_01 1', 'p225', [r_entrance(-14), light], 6)
play sfx2 "other_7047.ogg"
c2253 '[convertstrid(1128668)]'
hide p225
$ update_portrait('oc001_01 21', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128669)]'
hide p1
$ update_portrait('st026_01 2', 'p225', [r(-14), light], 6)
c2253 '[convertstrid(1128670)]'
$ update_portrait('st026_01 2', 'p225', [r(-14), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128671)]'
hide p225
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1128672)]'
hide p1
$ update_portrait('st026_01 4', 'p225', [r(-14), light], 6)
c2253 '[convertstrid(1128673)]'
hide p2
$ update_portrait('st026_01 4', 'p225', [r(-14), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
c461 '[convertstrid(1128674)]'
$ update_portrait('sc039_01 2', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('st026_01 4', 'p225', [r(-14), light], 6)
c2253 '[convertstrid(1128675)]'
hide p46
$ update_portrait('st026_01 4', 'p225', [r(-14), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na16.ogg"
c11 '[convertstrid(1128676)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 6)
c2253 '[convertstrid(1128677)]'
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 6)
c2253 '[convertstrid(1128678)]'
hide p1
hide p225
c0 '[convertstrid(1128679)]'
return