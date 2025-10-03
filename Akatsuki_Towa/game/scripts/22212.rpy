label avg22212:

$ play_music("ed7161.ogg")
scene avg_bg_039
$ update_narrator('c2251')
window show
with fade_in
$ update_portrait('st026_01 1', 'p225', [l_entrance(-14), light, flip], 6)
c2251 '[convertstrid(1128689)]'
$ update_portrait('st026_01 1', 'p225', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1128690)]'
hide p225
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc040_01 1', 'p47', [l(-9), light, flip], 6)
c471 '[convertstrid(1128692)]'
hide p47
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128693)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[convertstrid(1128694)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na17.ogg"
c11 '[convertstrid(1128695)]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st026_01 5', 'p225', [r(-14), light], 6)
c2253 '[convertstrid(1128696)]'
return