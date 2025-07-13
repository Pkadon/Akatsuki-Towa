label avg25098:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1210273]]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6025.ogg"
c13 '[textdict[1210274]]'
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1210275]]'
return