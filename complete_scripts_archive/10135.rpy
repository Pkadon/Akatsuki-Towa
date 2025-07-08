label avg10135:
stop music

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
window show
with fade_in
play sfx2 "other_7047.ogg"
c561 '[textdict[1007371]]'
hide p56
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1007372]]'
hide p1
hide p56
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[textdict[1007373]]'
hide p2
hide p56
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1007374]]'
hide p2
hide p56
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1007681]]'
hide p56
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007375]]'
hide p56
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007376]]'
hide p56
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007377]]'
return