label avg20081:

stop music
scene placeholderbackground
window show
with fade_in
c0 '[textdict[1004268]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1004269]]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1004270]]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 5)
c33 '[textdict[1004271]]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1004272]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 5)
c33 '[textdict[1004273]]'
hide p3
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1004274]]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [mid(-6), light], 5)
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[textdict[1004275]]'
hide p3
$ update_portrait('oc004_01 13', 'p4', [mid(-5), light], 5)
c43 '[textdict[1004276]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1004277]]'
return