label avg12569:

play music "ED6200.ogg"
scene avg_bg_010
$ update_narrator('c41')
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
window show
with fade_in
$ update_portrait('oc004_01 5', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
c41 '[textdict[1155140]]'
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 5)
c23 '[textdict[1155141]]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[textdict[1155142]]'
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155143]]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1155144]]'
return