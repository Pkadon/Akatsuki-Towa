label avg10202:

play music "ed7300.ogg"
scene placeholderbackground
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1004294)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6024.ogg"
c31 '[convertstrid(1004295)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st028_02 4', 'p666', [r(8), light], 6)
c6663 '[convertstrid(1004296)]'
$ update_portrait('st028_02 4', 'p666', [r(8), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), l_shake, light, flip], 6)
c31 '[convertstrid(1004297)]'
hide p3
hide p666
play sfx2 "other_7022.ogg"
c0 '[convertstrid(1004298)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1004299)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1004300)]'
stop music
hide p2
play sfx2 "elc_5005.ogg"
c6651 '[convertstrid(1004301)]'
play sfx2 "elc_5005.ogg"
c6651 '[convertstrid(1004302)]'
play sfx2 "elc_5005.ogg"
c6651 '[convertstrid(1004303)]'
play music "ed7511.ogg"
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1004304)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li09.ogg"
c41 '[convertstrid(1004305)]'
hide p1
$ update_portrait('oc004_01 23', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1004306)]'
hide p4
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('st028_02 4', 'p666', [l(8), light, flip], 6)
play sfx2 "other_7085.ogg"
c6661 '[convertstrid(1004307)]'
hide p666
hide p2
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
play sfxvoice "avg_vocal_ro15.ogg"
c31 '[convertstrid(1004308)]'
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1004309)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
c13 '[convertstrid(1004310)]'
hide p3
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1004311)]'
hide p2
play sfx2 "elc_5005.ogg"
c6651 '[convertstrid(1004312)]'
hide p1
$ update_portrait('sc038_01 3', 'p667', [r_entrance(-1), light], 6)
play sfx2 "fight_6010.ogg"
c6673 '[convertstrid(1004313)]'
hide p667
$ update_portrait('sc039_01 3', 'p668', [r(-13), light], 6)
play sfx2 "fight_6031.ogg"
c6683 '[convertstrid(1004314)]'
play music "ed7527.ogg"
$ update_portrait('sc039_01 3', 'p668', [r(-13), dark], 5)
play sfx2 "elc_5005.ogg"
c6651 '[convertstrid(1004315)]'
hide p668
$ update_portrait('oc001_01 2', 'p1', [r(-2), l_shake, light], 6)
c13 '[convertstrid(1004316)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 4', 'p667', [l(-1), light, flip], 6)
c6671 '[convertstrid(1004317)]'
$ update_portrait('sc038_01 4', 'p667', [l(-1), light, flip], 6)
c6671 '[convertstrid(1004318)]'
hide p1
$ update_portrait('sc038_01 4', 'p667', [l(-1), dark, flip], 5)
$ update_portrait('sc060_01 1', 'p669', [r(-16), light], 6)
c6693 '[convertstrid(1004319)]'
hide p667
$ update_portrait('sc060_01 1', 'p669', [r(-16), dark], 5)
$ update_portrait('sc045_01 4', 'p670', [l(-11), light, flip], 6)
c6701 '[convertstrid(1004320)]'
hide p669
$ update_portrait('sc045_01 4', 'p670', [l(-11), dark, flip], 5)
$ update_portrait('sc040_01 4', 'p671', [r(-9), light], 6)
c6713 '[convertstrid(1004321)]'
hide p670
$ update_portrait('sc040_01 4', 'p671', [r(-9), dark], 5)
$ update_portrait('sc041_01 1', 'p672', [l(-9), light, flip], 6)
c6721 '[convertstrid(1004322)]'
hide p671
$ update_portrait('sc041_01 1', 'p672', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1004323)]'
return