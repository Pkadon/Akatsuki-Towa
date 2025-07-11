label avg20022:

play music "ed7150.ogg"
scene placeholderbackground
$ update_portrait('st004_01 2', 'p204', [mid(4), light], 5)
window show
with fade_in
c2043 '[textdict[1001637]]'
hide p204
$ update_portrait('sc043_01 1', 'p50', [mid(-20), light], 5)
c503 '[textdict[1001638]]'
hide p50
$ update_portrait('st004_01 1', 'p204', [mid(4), light], 5)
c2043 '[textdict[1001639]]'
hide p204
$ update_portrait('sc043_01 1', 'p50', [mid(-20), light], 5)
c503 '[textdict[1001638]]'
hide p50
$ update_portrait('st004_01 2', 'p204', [mid(4), light], 5)
c2043 '[textdict[1001641]]'
$ update_portrait('st004_01 5', 'p204', [mid(4), light], 5)
c2043 '[textdict[1001642]]'
$ update_portrait('st004_01 1', 'p204', [mid(4), light], 5)
c2043 '[textdict[1001643]]'
hide p204
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1001644]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1001645]]'
return