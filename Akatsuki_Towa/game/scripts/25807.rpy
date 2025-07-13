label avg25807:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1211267]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211268]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6026.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1211269]]'
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
play sfx2 "elc_5001.ogg"
play sfxvoice "avg_vocal_na19.ogg"
c13 '[textdict[1211270]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1211271]]'
return