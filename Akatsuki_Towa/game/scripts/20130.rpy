label avg20130:

stop music
scene avg_bg_071
$ update_narrator('c11')
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [l_entrance(-2), light, flip], 6)
play sfxvoice "avg_vocal_na10.ogg"
c11 '[textdict[1006633]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch21.ogg"
c23 '[textdict[1006634]]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
c41 '[textdict[1006635]]'
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro19.ogg"
c33 '[textdict[1006636]]'
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 5)
play sfx2 "other_7071.ogg"
play sfxvoice "avg_vocal_ro05.ogg"
c33 '[textdict[1006637]]'
hide p4
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
play sfx2 "other_7072.ogg"
play sfxvoice "avg_vocal_ji05.ogg"
c7011 '[textdict[1006638]]'
c7011 '[textdict[1006639]]'
c7011 '[textdict[1006640]]'
return