label avg10135:

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with fade_in
play sfx2 "other_7047.ogg"
c561 '[convertstrid(1007371)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 5)
c13 '[convertstrid(1007372)]'
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1007373)]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1007374)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1007681)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1007375)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1007376)]'
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(1007377)]'
return