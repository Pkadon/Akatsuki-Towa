label avg25052:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[textdict[1210144]]'
hide p1
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 5)
c20063 '[textdict[1210145]]'
return