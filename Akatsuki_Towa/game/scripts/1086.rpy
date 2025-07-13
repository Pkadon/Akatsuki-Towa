label avg1086:

play music "ed7202.ogg"
scene avg_bg_079
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
play sfxvoice "avg_vocal_li02.ogg"
c41 '[textdict[2101872]]'
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[2101873]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), l_shake, light, flip], 6)
c41 '[textdict[2101874]]'
$ update_portrait('oc004_01 23', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[2101875]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2101876]]'
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na17.ogg"
c13 '[textdict[2101877]]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 5)
c13 '[textdict[2101878]]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2101879]]'
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2101880]]'
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
c13 '[textdict[2101881]]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2101882]]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[2101883]]'
hide p4
hide p1
c0 '[textdict[2101884]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), r_shake, light], 5)
play sfxvoice "avg_vocal_na18.ogg"
c13 '[textdict[2101885]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2101886]]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 5)
c13 '[textdict[2101887]]'
return