label avg12356:

play music "ed9999.ogg"
scene avg_bg_074
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
$ update_narrator('c2311')
window show
with fade_in
play sfx2 "other_7048.ogg"
c2311 '[textdict[1133662]]'
$ update_portrait('st032_01 1', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133663]]'
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133664]]'
$ update_portrait('st032_01 5', 'p231', [l(2), dark, flip], 6)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li07.ogg"
c43 '[textdict[1133665]]'
hide p4
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
c13 '[textdict[1133666]]'
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 6', 'p231', [l(2), light, flip], 6)
c2311 '[textdict[1133667]]'
hide p231
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133668]]'
return