label avg25049:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch10.ogg"
c23 '[textdict[1210125]]'
hide p2
$ update_portrait('uc001_02 2', 'p2002', [mid(6), light], 5)
c20023 '[textdict[1210126]]'
hide p2002
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210127]]'
hide p1
$ update_portrait('uc001_02 1', 'p2002', [mid(6), light], 5)
c20023 '[textdict[1210128]]'
$ update_portrait('uc001_02 3', 'p2002', [mid(6), light], 5)
c20023 '[textdict[1210129]]'
hide p2002
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1210130]]'
return